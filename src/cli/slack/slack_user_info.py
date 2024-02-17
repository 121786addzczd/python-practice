"""
slack_user_info.py

このスクリプトは、SlackのAPIを使用してユーザー情報を取得し、表示します。
コンソールで「python slack_user_info.py」と入力すると実行できます。

注意事項:
このスクリプトを実行するには、以下の要件が必要です:
- Python 3.9以上のバージョンが必要です。
- dotenv ライブラリが必要です。インストール方法: 「pip install python-dotenv」
- slack_sdk ライブラリが必要です。インストール方法: 「pip install slack-sdk」
- Slack APIトークンが環境変数 SLACK_APP_USER_TOKEN_ID に設定されている必要があります。

このスクリプトはSlackの全ユーザー情報を取得し、display名が設定されている場合はそれを表示し、設定されていない場合はユーザー名を表示します。
"""
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()
token = os.environ.get("SLACK_APP_USER_TOKEN_ID")
user_client = WebClient(token=token)

# ユーザー一覧を取得
response = user_client.users_list()

total_users = 0
users_with_display_name = 0

for user in response['members']:
    # ボットや削除されたユーザーをカウントしない
    if user.get('is_bot') or user.get('deleted'):
        continue

    total_users += 1
    profile = user['profile']
    slack_user_id = user['id']  # ユーザーIDを取得
    display_name = profile.get('display_name')
    real_name = profile.get('real_name')
    slack_user_name = display_name or real_name
    email = profile.get('email')  # メールアドレスを取得
    is_display_name = bool(display_name) and display_name != ''

    if is_display_name:
        users_with_display_name += 1

    # ユーザーIDを含めて出力
    print(f"slack_user_id={slack_user_id}, slack_user_name={slack_user_name}, email={email} 設定: {is_display_name=}")

print(f"ユーザー総数: {total_users}")
print(f"display_nameを設定しているユーザー数: {users_with_display_name}")
