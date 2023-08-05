"""
スクリプト名: fetch_bank_details.py
概要: このスクリプトは全銀行コード（Zengin Code）を用いて、
日本の各銀行とその支店の詳細情報を取得し、CSVファイルに書き出します。
また、定義されていない銀行コードについては、テキストファイルに記録します。
注意：
実行には同階層に「banks.csv」ファイルが必要です。
"""

from zengin_code import Bank
import pandas as pd
import jaconv
from typing import List, Dict, Tuple


def generate_bank_counts_csv(input_file: str, output_file: str) -> pd.DataFrame:
    """
    この関数は、入力のCSVファイルからデータを読み込み、'bank_code'でグループ化し、
    各銀行のエントリ数を数え、データを'bank_code'でソートし、結果を出力のCSVファイルに書き込む。

    引数:
        input_file (str): 入力CSVファイルへのパス
        output_file (str): 出力CSVファイルへのパス

    戻り値:
        df_grouped (pd.DataFrame): グループ化とカウントが適用されたDataFrame
    """
    try:
        # CSVファイルを読み込む（'bank_code'を文字列として扱う）
        df = pd.read_csv(input_file, dtype={'bank_code': str})

        # 'deleted_at'列がnullの行のみを保持する
        df = df[df['deleted_at'].isnull()]

        # 'bank_code'でグループ化し、それぞれのグループの数を数える
        df_grouped = df.groupby(['bank_code', 'bank_name']).size().reset_index(name='count')

        # データを'bank_code'でソート
        df_grouped = df_grouped.sort_values('bank_code')

        # 結果を新しいCSVファイルに書き込む
        df_grouped.to_csv(output_file, index=False)

        print(f"'{output_file}'file generated")
        return df_grouped

    except FileNotFoundError:
        print("指定されたファイルが存在しません。")
    except pd.errors.EmptyDataError:
        print("指定されたファイルにデータがありません。")
    except Exception as e:
        print("予期しないエラーが発生しました:", e)


def to_half_width_kana(full_width_str) -> str:
    """全角カタカナを半角カタカナに変換に－を-にする"""
    half_width_str = jaconv.z2h(full_width_str, kana=True, ascii=True, digit=False)
    return half_width_str.replace("－", "-")


def fetch_bank_details(bank_codes: List[str], undefined_file: str) -> Tuple[List[Dict], int]:
    """指定された銀行コードに基づいて銀行詳細を取得する。

    Args:
        bank_codes (List[str]): 銀行コードのリスト。
        undefined_file (str): 未定義の銀行コードを記録するファイルの名前。

    Returns:
        Tuple[List[Dict], int]: 銀行および支店の情報を格納したリストと未定義の銀行数。
    """
    data = []  # 銀行および支店の情報を格納するためのリスト
    undefined_bank_count = 0  # 存在しない銀行コードをカウント

    with open(undefined_file, "w") as f:  # 新規書き込みモードで開く
        for bank_code in bank_codes:
            try:
                # 銀行コードを用いて銀行情報を取得
                bank = Bank[bank_code]
                # 銀行の各支店情報を取得
                branches = bank.branches
                for code in branches:
                    branch = branches[code]

                    # 全角カタカナを半角カタカナに変換
                    bank_name_half_width_kana = to_half_width_kana(bank.kana)
                    bank_br_name_half_width_kana = to_half_width_kana(branch.kana)

                    # 銀行および支店の情報をリストに追加
                    data.append(
                        {
                            "bank_code": bank_code,  # Add the current bank_code
                            "bank_br_code": code,
                            "bank_name_full_width": bank.kana,
                            "bank_br_name_full_width": branch.name,
                            "bank_name_half_width_kana": bank_name_half_width_kana,
                            "bank_br_name_half_width_kana": bank_br_name_half_width_kana,
                        }
                    )
            except KeyError:
                # 定義されていない銀行コードはテキストファイルに記録
                f.write(f"Bank code {bank_code} not found\n")
                undefined_bank_count += 1

    return data, undefined_bank_count


def write_to_file(filename: str, undefined_bank_count: int, total_banks: int) -> None:
    """結果をファイルとコンソールに出力する。

    Args:
        filename (str): 書き込むファイル名。
        undefined_bank_count (int): 未定義の銀行数。
        total_banks (int): 取得した銀行の総数。
    """
    message1 = f"存在しない銀行数: {undefined_bank_count}件"
    message2 = f"最大銀行更新数: {total_banks}件"

    print(message1)
    print(message2)

    with open(filename, "a") as f:  # 追記モードで開く
        f.write(message1 + "\n")
        f.write(message2 + "\n")

    print(f"'{filename}' file generated")


def main() -> None:
    raw_date_csv = "banks.csv"
    out_put_csv = "bank_code_count.csv"
    # 各銀行のエントリ数を数えたCSVファイル出力
    df = generate_bank_counts_csv(raw_date_csv, out_put_csv)

    # 'bank_code'カラムのデータをリスト形式で取得し、変数に代入
    bank_codes = df["bank_code"].tolist()
    
    undefined_file = "undefined_bank_code.txt"
    data, undefined_bank_count = fetch_bank_details(bank_codes, undefined_file)

    df = pd.DataFrame(data)

    output_file_name = "update_target_bank_combination_list.csv"
    df.to_csv(output_file_name, index=False)
    print(f"'{output_file_name}' file generated")

    write_to_file(undefined_file, undefined_bank_count, len(df))


if __name__ == "__main__":
    main()
