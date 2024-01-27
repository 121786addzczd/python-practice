"""
backlog_task_entry.py

このスクリプトは、Backlog APIを利用して特定のプロジェクトの課題を登録するために使用されます。CSVファイルから課題データを読み込み、Backlogに登録します。

主な機能:
- 環境変数からBacklog APIキー、スペースキー、プロジェクトIDを取得。
- CSVファイルから課題データを読み込み、Backlogに登録。
- 課題登録のために必要なID（課題の種別、担当者、カテゴリーなど）をid_list.jsonファイルから取得。
- 登録が完了したら、処理した課題数を出力。

注意点:
- `BACKLOG_API_KEY`, `BACKLOG_SPACE_KEY`, `BACKLOG_PROJECT_ID` の3つの環境変数の設定が必要。
- id_list.json と issue.csv の2つのファイルが必要です。id_list.jsonはBacklogの各種IDを格納し、issue.csvは登録する課題のデータを含みます。
- APIリクエストは、設定された環境変数に基づいて構築されるため、これらの値が不正確または未設定の場合、スクリプトは正しく動作しない。

使用方法:
スクリプトを実行する前に、必要な環境変数を設定し、id_list.json と issue.csv ファイルを用意してください。その後、スクリプトを実行すると、CSVファイルの課題データがBacklogプロジェクトに登録されます。
"""

import requests
import csv
import json
import os
import sys
from typing import Dict, Any


def check_env_var(var_name: str) -> str:
    """
    指定された環境変数をチェックし、存在すればその値を返す。
    存在しない場合はプログラムを終了する。

    Parameters:
    - var_name (str): チェックする環境変数の名前

    Returns:
    - str: 環境変数の値
    """
    if var_name not in os.environ:
        print(f"環境変数 '{var_name}' が設定されていません。")
        sys.exit(1)
    return os.environ[var_name]


def check_file_exists(file_path: str) -> None:
    """
    指定されたファイルパスのファイルが存在するかチェックし、
    存在しない場合はプログラムを終了する。

    Parameters:
    - file_path (str): チェックするファイルのパス
    """
    if not os.path.exists(file_path):
        print(f"ファイル '{file_path}' が見つかりません。")
        sys.exit(1)


def get_issue_id(api_key: str, base_url: str, issue_key: str) -> int:
    """
    指定された課題キーに対応する課題IDを取得する。

    Parameters:
    - api_key (str): Backlog APIキー
    - base_url (str): BacklogのベースURL
    - issue_key (str): 課題キー

    Returns:
    - int: 課題ID
    """
    url = f"{base_url}/issues/{issue_key}"
    params = {'apiKey': api_key}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print('get_issue')
        return json.loads(response.text)["id"]
    except requests.RequestException as e:
        print(f"APIリクエストに失敗しました: {e}")
        print(f"ステータスコード: {e.response.status_code}")
        print(f"エラー内容: {e.response.text}")
        sys.exit(1)


def add_issue(api_key: str, base_url: str, project_id: str, payload: Dict[str, Any]) -> requests.Response:
    """
    指定されたプロジェクトに新しい課題を追加する。

    Parameters:
    - api_key (str): Backlog APIキー
    - base_url (str): BacklogのベースURL
    - project_id (str): プロジェクトID
    - payload (Dict[str, Any]): 課題のデータ

    Returns:
    - requests.Response: リクエストのレスポンス
    """
    url = f"{base_url}/issues"
    payload['projectId'] = project_id
    params = {'apiKey': api_key}
    try:
        response = requests.post(url, params=params, data=payload)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"APIリクエストに失敗しました: {e}")
        print(f"ステータスコード: {e.response.status_code}")
        print(f"エラー内容: {e.response.text}")
        sys.exit(1)


def prepare_payload(
    api_key: str, 
    base_url: str, 
    row: Dict[str, str], 
    id_list: Dict[str, Dict[str, int]], 
    issue_id_list: Dict[str, int]
) -> Dict[str, Any]:
    """
    CSVの行からpayloadを準備する。

    Parameters:
    - api_key (str): Backlog APIキー
    - base_url (str): BacklogのベースURL
    - row (Dict[str, str]): CSVファイルの行
    - id_list (Dict[str, Dict[str, int]]): IDリスト
    - issue_id_list (Dict[str, int]): 親課題IDリスト

    Returns:
    - Dict[str, Any]: Backlogに送信するためのpayload
    """
    payload = {}
    for key, value in row.items():
        if key == 'parentIssueId' and value and value not in issue_id_list:
            issue_id_list[value] = get_issue_id(api_key, base_url, value)
        payload[key] = issue_id_list.get(value, id_list.get(key, {}).get(value, value))
        # print(payload) // DEBUG
    return payload


def process_issues(
    api_key: str, 
    base_url: str, 
    project_id: str, 
    id_list: Dict[str, Dict[str, int]], 
    issue_file: str
) -> None:
    """
    CSVファイルから課題データを読み込み、Backlogに課題を登録する。

    Parameters:
    - api_key (str): Backlog APIキー
    - base_url (str): BacklogのベースURL
    - project_id (str): プロジェクトID
    - id_list (Dict[str, Dict[str, int]]): IDリスト
    - issue_file (str): 課題データが含まれるCSVファイル
    """
    issue_id_list = {}
    issue_count = 0

    with open(issue_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            payload = prepare_payload(api_key, base_url, row, id_list, issue_id_list)
            add_issue(api_key, base_url, project_id, payload)
            issue_count += 1

    print(f"処理完了。合計 {issue_count} 件の課題が登録されました。")


def main() -> None:
    # 環境変数の取得
    api_key = check_env_var('BACKLOG_API_KEY')
    space_key = check_env_var('BACKLOG_SPACE_KEY')
    project_id = check_env_var('BACKLOG_PROJECT_ID')
    base_url = f"https://{space_key}/api/v2"
    
    # 必要なファイルの存在チェック
    check_file_exists('output/id_list.json')
    check_file_exists('issue.csv')

    # idリストを取得
    with open('id_list.json', encoding='utf-8') as f:
        id_list = json.load(f)

    # CSVファイルからの課題データの処理
    process_issues(api_key, base_url, project_id, id_list, 'issue.csv')

if __name__=="__main__":
    main()
