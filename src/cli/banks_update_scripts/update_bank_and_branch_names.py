# update_bank_and_branch_names.py

"""
スクリプト概要：
このスクリプトは、銀行名と支店名を更新するためのもの
2つのCSVファイル（'update_target_bank_combination_list.csv'と'banks.csv'）を読み込み、そのデータを比較・処理して、SQL更新文を出力する

注意点：
1. スクリプトを実行する前に、'update_target_bank_combination_list.csv'と'banks.csv'という2つのCSVファイルが必要
2. このスクリプトを動作させるためには、'pandas'と'jaconv'というPythonライブラリが必要となる。これらはpipを使ってインストールすること
3. pythonのバージョンは3.9以上であること
"""


import os
import pandas as pd
import jaconv
from typing import Tuple


# データフレーム抽出条件

# 更新が必要ないもの
BOTH_MATCH = (
    '(bank_name_match == "〇") & '
    '(bank_br_name_match == "〇")'
)

# 片方しか一致しておらず更新が必要
ONE_MATCH = (
    '((bank_name_match == "〇") & (bank_br_name_match == "×")) | '
    '((bank_name_match == "×") & (bank_br_name_match == "〇"))'
)

# 更新データがなく今は存在していない
BOTH_EMPTY = (
    'bank_name_half_width_kana_update.isna() & '
    'bank_br_name_half_width_kana_update.isna()'
)

# 銀行名と支店名両方とも変更がある
MISMATCH_NEEDS_UPDATE = (
    '((bank_name_match == "×") & (bank_br_name_match == "×") & '
    'bank_name_half_width_kana_update.notna() & '
    'bank_br_name_half_width_kana_update.notna())'
)


def to_half_width_kana(full_width_str: str) -> str:
    """
    全角カタカナとハイフンを半角に変換
    """
    half_width_str = jaconv.z2h(full_width_str, kana=True, ascii=True, digit=False)
    return half_width_str.replace("－", "-")


def load_and_prepare_dataframes() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    CSVファイルを読み込み、データフレームを準備する
    """
    try:
        df_update_target = pd.read_csv(
            "update_target_bank_combination_list.csv",
            dtype={"bank_code": str, "bank_br_code": str},
        )[
            [
                "bank_code",
                "bank_br_code",
                "bank_name_half_width_kana",
                "bank_br_name_half_width_kana",
            ]
        ]
        df_banks = pd.read_csv(
            "banks.csv", dtype={"bank_id": str, "bank_code": str, "bank_br_code": str}
        )[["bank_id", "bank_code", "bank_br_code", "bank_name", "bank_br_name"]]
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("No data found in the file. Please check the file content and try again.")
        exit(1)
    except pd.errors.ParserError:
        print(
            "Error while parsing the file. Please check the file content and try again."
        )
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

    # 銀行名を全角カタカナから半角カタカナに変換
    df_banks["bank_name_half_width_kana"] = df_banks["bank_name"].apply(
        to_half_width_kana
    )
    df_banks["bank_br_name_half_width_kana"] = df_banks["bank_br_name"].apply(
        to_half_width_kana
    )
    
    # df_update_targetの重複を削除
    df_update_target = df_update_target.drop_duplicates(subset=["bank_code", "bank_br_code"])

    return df_banks, df_update_target


def merge_and_compare_dataframes(
    df_banks: pd.DataFrame, df_update_target: pd.DataFrame
) -> pd.DataFrame:
    """
    データフレームをマージし、名前を比較する
    """

    # データフレームをマージ
    df = pd.merge(
        df_banks,
        df_update_target,
        on=["bank_code", "bank_br_code"],
        how="left",
        suffixes=("_banks", "_update"),
    )

    # 銀行名と支店名を比較
    df["bank_name_match"] = (
        df["bank_name_half_width_kana_banks"] == df["bank_name_half_width_kana_update"]
    )
    df["bank_br_name_match"] = (
        df["bank_br_name_half_width_kana_banks"]
        == df["bank_br_name_half_width_kana_update"]
    )

    # 結果を "〇" と "×" にマッピング
    df["bank_name_match"] = df["bank_name_match"].map({True: "〇", False: "×"})
    df["bank_br_name_match"] = df["bank_br_name_match"].map({True: "〇", False: "×"})

    # 不要なカラムを削除
    df = df.drop(
        columns=[
            "bank_name_half_width_kana_banks",
            "bank_br_name_half_width_kana_banks",
        ]
    )

    return df


def output_and_count(
    df: pd.DataFrame, file_name: str, condition: str = None
) -> pd.DataFrame:
    """
    DataFrameをCSVファイルとして出力し、行数をカウントする関数
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # ディレクトリが存在しない場合に新たに作成

    if condition:
        df = df.query(condition)

    if df.empty:
        print(f"No rows matching condition: {condition}")
        return pd.DataFrame()

    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)
    print(f"Count of rows for condition '{condition}' in '{file_name}': {len(df)}")
    return df


def generate_sql(
    df: pd.DataFrame, output_file_name: str = "update_banks_and_branches.sql"
) -> None:
    """
    SQL文を生成して出力する
    """
    with open(output_file_name, "w") as f:
        for i, row in df.iterrows():
            f.write(
                f"UPDATE banks SET bank_name = '{row['bank_name_half_width_kana_update']}', bank_br_name = '{row['bank_br_name_half_width_kana_update']}' WHERE bank_id = '{row['bank_id']}' AND bank_code = '{row['bank_code']}' AND bank_br_code = '{row['bank_br_code']}';\n"
            )

    print(
        f"Successfully generated update queries for {len(df)} banks, saved to {output_file_name}."
    )
    print(f"{len(df)} bank updates are necessary.")


def main() -> None:
    df_banks, df_update_target = load_and_prepare_dataframes()
    df = merge_and_compare_dataframes(df_banks, df_update_target)

    # 全データを出力
    output_and_count(df, "bunks_all.csv")

    # 条件に合致するデータを出力
    output_and_count(df, "bunks_both_match.csv", BOTH_MATCH)
    output_and_count(df, "bunks_one_match.csv", ONE_MATCH)
    output_and_count(df, "bunks_both_empty.csv", BOTH_EMPTY)
    output_and_count(df, "bunks_mismatch_needs_update.csv", MISMATCH_NEEDS_UPDATE)

    # 複合条件でデータをフィルタリング
    combined_condition = ONE_MATCH + ' | ' + MISMATCH_NEEDS_UPDATE
    filtered_df = df.query(combined_condition)
    df_update_needed = output_and_count(filtered_df, "bunks_update_needed.csv")

    # 更新が必要なデータのSQLを生成
    generate_sql(df_update_needed)


if __name__ == "__main__":
    main()
