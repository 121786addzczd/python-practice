"""
generate_bank_data_update.py

このスクリプトは、以下の操作を行う：
1. banks.csvとupdate_target_bank_combination_list.csvという2つのCSVファイルからデータを読み込む。
2. 読み込んだデータを元に、2つのDataFrameを作成し、それらを特定の列を基準に結合。
3. 結合されたDataFrameを元に、banksテーブルのbank_name_full_widthとbank_br_name_full_width列を更新するためのSQLクエリを生成し、それをupdate_banks.sqlというファイルに書き出す。
4. 最終的に、DataFrameのbank_name_full_widthとbank_br_name_full_width列の値の存在・非存在の数を出力する。

注意：
このスクリプトは例外処理を含んでおり、ファイルの読み込み、DataFrameの結合、SQLファイルの生成、値の数の出力において例外が発生した場合、
適切なエラーメッセージが出力され、その後の処理がスキップされる。
"""

import pandas as pd
from pandas import DataFrame


def load_dataframes() -> tuple[DataFrame, DataFrame]:
    """
    CSVファイルからデータを読み込み、pandasのDataFrameを生成
    """
    try:
        df_banks = pd.read_csv(
            "banks.csv", dtype={"bank_id": str, "bank_code": str, "bank_br_code": str}
        )
        df_updates = pd.read_csv(
            "update_target_bank_combination_list.csv",
            dtype={"bank_code": str, "bank_br_code": str},
        )
    except Exception as e:
        print(f"Error occurred while reading CSV files: {e}")
        return None, None

    return df_banks, df_updates


def merge_dataframes(df_banks: DataFrame, df_updates: DataFrame) -> DataFrame:
    """
    二つのDataFrameを特定の列に基づいて結合
    """
    try:
        df_merged = pd.merge(
            df_banks, df_updates, on=["bank_code", "bank_br_code"], how="left"
        )
        df_merged.drop_duplicates(inplace=True)  # 重複行を削除
    except Exception as e:
        print(f"Error occurred while merging DataFrames: {e}")
        return None

    return df_merged[
        [
            "bank_id",
            "bank_code",
            "bank_br_code",
            "bank_name",
            "bank_br_name",
            "bank_name_full_width",
            "bank_br_name_full_width",
        ]
    ]


def generate_sql_file(df: DataFrame) -> None:
    """
    DataFrameからSQLファイルを生成
    """
    try:
        sql_file = "update_banks.sql"
        df_sql_gen = df[
            df["bank_name_full_width"].notna() & df["bank_br_name_full_width"].notna()
        ]

        with open(sql_file, "w", encoding="utf8") as f:
            # もし列が存在しない場合、列を作成する指示を追加
            f.write(
                "-- bank_name_full_widthとbranch_br_name_full_widthという列がbanksテーブルに存在しない場合、以下のクエリを実行して追加します:\n"
            )
            f.write("-- ALTER TABLE banks\n")
            f.write(
                "-- ADD COLUMN bank_name_full_width VARCHAR(255) COMMENT '銀行名全角' AFTER bank_br_name,\n"
            )
            f.write(
                "-- ADD COLUMN bank_br_name_full_width VARCHAR(255) COMMENT '支店名全角' AFTER bank_name_full_width;\n\n"
            )

            for index, row in df_sql_gen.iterrows():
                sql = f"UPDATE banks SET bank_name_full_width = '{row['bank_name_full_width']}', bank_br_name_full_width = '{row['bank_br_name_full_width']}' WHERE bank_id = {row['bank_id']} AND bank_code = {row['bank_code']} AND bank_br_code = {row['bank_br_code']};\n"
                f.write(sql)

        print(f"'{sql_file}' File generated successfully.")
    except Exception as e:
        print(f"Error occurred while generating SQL file: {e}")


def print_value_counts(df: DataFrame) -> None:
    """
    指定された列の値の数を出力
    """
    try:
        value_counts_branch = df["bank_br_name_full_width"].notna().value_counts()

        print("Bank and bank branch name mapping information")
        print(
            "Number of data registrations in bank master: ",
            df["bank_br_name_full_width"].shape[0],
        )
        print("Number of existing values: ", value_counts_branch[True])
        print("Number of non-existing values: ", value_counts_branch[False])
    except Exception as e:
        print(f"Error occurred while printing value counts: {e}")


def main() -> None:
    df_banks, df_updates = load_dataframes()

    if df_banks is None or df_updates is None:
        print("Unable to continue, data loading failed.")
        return

    df_merged = merge_dataframes(df_banks, df_updates)

    if df_merged is None:
        print("Unable to continue, DataFrame merging failed.")
        return
    # CSV出力
    df_merged.to_csv("merge_bank_data.csv", index=False)

    print_value_counts(df_merged)
    # 銀行更新用SQLファイル出力
    generate_sql_file(df_merged)


if __name__ == "__main__":
    main()
