"""
stripe_customer_list.py

このスクリプトは、Stripe APIを利用して顧客一覧を取得し、各顧客のID、名前、メールアドレスを表示します。

主な機能:
- 環境変数からStripe APIキーを取得。
- Stripe APIを呼び出して全顧客の一覧を取得。
- 取得した顧客情報（ID、名前、メールアドレス）を集計し、表示。

注意点:
- STRIPE_SECRET_KEY の環境変数の設定が必要です。
- 顧客情報の取得には `auto_paging_iter` を使用していますが、データ量が多い場合、処理に時間がかかる可能性があります。
- Stripe APIの使用制限に注意してください。大量のデータを取得する場合、レートリミットに達する可能性があります。

使用方法:
スクリプトを実行する前に、必要な環境変数を設定してください。その後、スクリプトを実行すると、Stripeに登録されている顧客の一覧が表示されます。
"""

import os
from dotenv import load_dotenv
import stripe

load_dotenv()
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

try:
    # Stripe APIを使用して顧客一覧を取得
    customers = stripe.Customer.list()

    # 顧客数のカウンター
    customer_count = 0

    print("顧客情報の集計を開始します。集計に時間がかかる場合があります。")

    # 取得した顧客一覧をループして表示
    customer_info_list = []  # 顧客情報を格納するリスト
    for customer in customers.auto_paging_iter():
        # 顧客情報をリストに追加
        customer_info_list.append(f"顧客ID: {customer.id}, 名前: {customer.name}, メールアドレス: {customer.email}")
        customer_count += 1

    print(f"ユーザー一覧（合計 {customer_count} 件）:")

    # 各顧客の情報を表示
    for customer_info in customer_info_list:
        print(customer_info)

except stripe.error.StripeError as e:
    print(f"Stripeエラー: {e}")

except Exception as e:
    print(f"エラー: {e}")
