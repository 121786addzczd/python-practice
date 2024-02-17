"""
stripe_invoice_user_detail.py

このスクリプトは、Stripe APIを利用して特定の顧客IDに紐づくインボイス情報を取得し、顧客のメールアドレスと共に表示するために使用されます。
環境変数からStripe APIキーと顧客IDを取得し、指定された顧客に対するインボイスのリストを取得して詳細情報を出力します。

主な機能:
- 環境変数からStripe APIキーとテスト用の顧客IDを取得。
- 指定された顧客IDに紐づくStripeの顧客情報を取得し、メールアドレスを表示。
- 同じ顧客IDに紐づくインボイス情報を取得し、各インボイスの作成日、金額、請求書番号、期日を表示。

注意点:
- STRIPE_SECRET_KEY および STRIPE_CUSTOMER_TEST_ID の環境変数の設定が必要です。
- スクリプトはテスト用顧客IDを使用しており、実運用時には適切な顧客IDに変更してください。
- Stripe APIの使用制限に注意し、大量のリクエストを短時間に送らないようにしてください。

使用方法:
スクリプトを実行する前に、.env ファイルまたは環境変数を通じて STRIPE_SECRET_KEY と STRIPE_CUSTOMER_TEST_ID を設定してください。
その後、スクリプトを実行すると、指定された顧客IDに紐づくインボイス情報が表示されます。出力には、インボイスの作成日、金額、請求書番号、期日のほか、顧客のメールアドレスが含まれます。
"""
import os
from dotenv import load_dotenv
import stripe
from datetime import datetime

load_dotenv()
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# 特定の顧客ID
customer_id = os.environ.get("STRIPE_CUSTOMER_TEST_ID") # 必要に応じてcustomer_idは変更

# 参考 https://stripe.com/docs/api/invoices/upcoming_invoice_lines
try:
    customer = stripe.Customer.retrieve(customer_id)
    # 顧客のメールアドレスを取得
    customer_email = customer.email

    # 特定の顧客に対するインボイスを取得
    invoices = stripe.Invoice.list(customer=customer_id)

    for invoice in invoices.auto_paging_iter():
        # インボイスの情報を表示
        created_date = datetime.fromtimestamp(invoice.created).strftime('%m/%d %H:%M')
        amount_due = f"¥{invoice.amount_due:,}"
        due_date = datetime.fromtimestamp(invoice.due_date).strftime('%m/%d') if invoice.due_date else '-'
        print(f"作成日: {created_date}, 金額: {amount_due}, 請求書番号: {invoice.number}, 期日: {due_date}")

    print(f"顧客のメールアドレス: {customer_email}")

except Exception as e:
    print(f"エラーが発生しました: {e}")
