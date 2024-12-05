"""
ファイル名: stripe_customer_export.py

概要:
    Stripeの顧客情報を取得し、指定された形式（JSONまたはCSV）でファイルに保存するスクリプト。

使用例:
    JSON形式で顧客情報を保存:
        python stripe_customer_expor.py --format json --output stripe-customers.json

    CSV形式で顧客情報を保存:
        python stripe_customer_export.py --format csv --output stripe-customers.csv

注意:
    - STRIPE_SECRET_KEY の環境変数の設定が必要です。
    - このスクリプトを使用するには、Stripe Pythonライブラリが必要です。
      インストール方法: pip install stripe
"""

import stripe
import json
import csv
import argparse
import sys
from dotenv import load_dotenv


class JapaneseArgumentParser(argparse.ArgumentParser):
    """カスタムArgumentParserでエラーメッセージを日本語化"""

    def error(self, message):
        sys.stderr.write(f"エラー: {message}\n")
        self.print_help()
        sys.exit(2)


def fetch_customers(output_format, output_file):
    """顧客情報を取得し、指定された形式でファイルに出力"""
    load_dotenv()
    stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

    customers = stripe.Customer.list().auto_paging_iter()

    if output_format == "json":
        with open(output_file, "w", encoding="utf-8") as file:
            for customer in customers:
                json.dump(customer, file, ensure_ascii=False)
                file.write("\n")
        print(f"顧客情報をJSON形式で'{output_file}'に書き出しました。")

    elif output_format == "csv":
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # ヘッダー行を定義
            headers = [
                "id",
                "email",
                "name",
                "created",
                "invoice_prefix",
                "metadata_company_name",
            ]
            writer.writerow(headers)
            # データ行を記載
            for customer in customers:
                metadata = customer.get("metadata", {})
                writer.writerow(
                    [
                        customer.get("id", ""),
                        customer.get("email", ""),
                        customer.get("name", ""),
                        customer.get("created", ""),
                        customer.get("invoice_prefix", ""),
                        metadata.get(
                            "company_name", ""
                        ),  # metadataのcompany_nameを取得
                    ]
                )
        print(f"顧客情報をCSV形式で'{output_file}'に書き出しました。")


def main():
    # コマンドライン引数の定義
    parser = JapaneseArgumentParser(
        description="Stripeの顧客情報を取得してファイルに書き出します。",
        usage="python ts-stripe.py --format {json,csv} --output OUTPUT",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        required=True,
        help="出力形式を指定してください (json または csv)。",
    )
    parser.add_argument(
        "--output", required=True, help="出力ファイル名を指定してください。"
    )
    args = parser.parse_args()

    # 顧客情報の取得とファイル出力
    fetch_customers(args.format, args.output)


if __name__ == "__main__":
    main()
