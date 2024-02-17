"""
slack_user_lookup.py

このスクリプトは、Slack APIを利用してメールアドレスに基づいてSlackユーザー情報を検索するために使用されます。
ユーザーは標準入力を通じてメールアドレスを入力し、該当するユーザーがSlack上に存在する場合、そのユーザーのIDと名前が表示されます。

主な機能:
- 環境変数からSlack APIトークンを取得。
- 標準入力からユーザーにメールアドレスの入力を求める。
- 入力されたメールアドレスの形式が有効かどうかを確認する。
- 有効なメールアドレスであれば、Slack APIを呼び出してメールアドレスに該当するユーザー情報を検索。
- 該当するユーザー情報（ユーザーIDとユーザー名）を表示。

注意点:
- SLACK_APP_USER_TOKEN_ID の環境変数の設定が必要です。
- メールアドレスの形式は正規表現を用いて簡易的に検証されますが、実際のメールアドレスの存在や有効性は確認しません。
- Slack APIの使用制限や権限によっては、検索機能が期待通りに動作しない可能性があります。

使用方法:
スクリプトを実行する前に、必要な環境変数を設定してください。その後、スクリプトを実行し、プロンプトに従って検索したいメールアドレスを入力します。
入力されたメールアドレスに該当するユーザーが見つかった場合、その情報が表示されます。
"""
import os
import re
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def is_valid_email(email):
    # 簡単なメールアドレスの正規表現パターン
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

load_dotenv()
token = os.environ.get("SLACK_APP_USER_TOKEN_ID")
user_client = WebClient(token=token)

try:
    # 標準入力からメールアドレスを受け取る
    target_email = input("検索するSlackユーザーのメールアドレスを入力してください: ")

    # メールアドレスの形式を確認
    if not is_valid_email(target_email):
        print("無効なメールアドレス形式です。")
    else:
        # メールアドレスからユーザー情報を検索
        response = user_client.users_lookupByEmail(email=target_email)

        user = response['user']
        profile = user['profile']
        slack_user_id = user['id']  # ユーザーIDを取得
        display_name = profile.get('display_name', '')  # display_nameがない場合は空文字を返す
        real_name = profile.get('real_name', '')  # real_nameがない場合は空文字を返す
        slack_user_name = display_name or real_name  # display_nameが空の場合、real_nameを使用

        print("-- 指定されたメールアドレスのSlackユーザー情報 --")
        print(f"slack_user_id={slack_user_id}, slack_user_name={slack_user_name}")

except SlackApiError as e:
    if e.response["error"] == "users_not_found":
        print("メールアドレスに該当するユーザーが見つかりませんでした。")
    else:
        print(f"Slack APIエラーが発生しました: {e.response['error']}")

except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
