"""
backlog_get_project_data.py

概要:
このスクリプトは、Backlog APIを利用して特定のプロジェクトに関連するさまざまなID（課題の種別、
担当者、カテゴリー、バージョン、マイルストーン、優先度、カスタムフィールド）を取得し、それらを
コンソールに出力し、JSONファイルに保存します。

主な機能:
- 環境変数からBacklog APIキー、スペースキー、プロジェクトIDを取得。
- Backlogの特定のエンドポイントにリクエストを送り、応答データを取得。
- 取得したデータは、様々なIDとそれに対応する名前を辞書形式で保存し、コンソールに出力。
- 最終的に、このデータをJSON形式で指定されたディレクトリに保存。

注意点:
- `BACKLOG_API_KEY`, `BACKLOG_SPACE_KEY`, `BACKLOG_PROJECT_ID` の3つの環境変数の設定が必要。
- APIリクエストは、設定された環境変数に基づいて構築されるため、これらの値が不正確または
  未設定の場合、スクリプトは正しく動作しない。

使用方法:
スクリプトを実行する前に、必要な環境変数を設定してください。その後、スクリプトを実行すると、
指定したBacklogプロジェクトのID情報が取得され、出力および保存されます。
"""

import os
import sys
import requests
import json
import traceback
from typing import Dict, Any


def check_env_var(var_name: str) -> str:
    """
    指定された環境変数をチェックし、存在すればその値を返す。
    存在しない場合はプログラムを終了する。

    Parameters:
    - var_name (str): チェックする環境変数の名前

    Returns:
    -   str: 環境変数の値
    """
    if var_name not in os.environ:
        print(f"環境変数 '{var_name}' が設定されていません。")
        sys.exit(1)
    return os.environ[var_name]


def get_id(url: str, api_key: str) -> Any:
    """
    指定されたURLからデータを取得し、JSONとして返す。

    Parameters:
    - url (str): データを取得するURL
    - api_key (str): Backlog APIキー

    Returns:
    - Any: 取得したデータ（JSON形式）
    """
    params = {'apiKey': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return json.loads(response.text)


# 各種IDを取得して出力する関数
def fetch_and_output_ids(api_key: str, base_url: str, project_id: str) -> Dict[str, Dict[str, int]]:
    """
    Backlog APIを使用して、プロジェクトの各種IDを取得し、出力する。

    Parameters:
    - api_key (str): Backlog APIキー
    - base_url (str): BacklogのベースURL
    - project_id (str): プロジェクトID

    Returns:
    - Dict[str, Dict[str, int]]: 取得した各種ID
    """
    output: Dict[str, Dict[str, int]] = {}

    # issueTypeIdの取得と出力
    print('・issueTypeId(課題の種別のID)用')
    datas = get_id(f"{base_url}/projects/{project_id}/issueTypes", api_key)
    output['issueTypeId'] = {data['name']: data['id'] for data in datas}
    for name, id in output['issueTypeId'].items():
        print(f"{id}:{name}")

    # assigneeIdの取得と出力
    print('・assigneeId(課題の担当者のID)用')
    datas = get_id(f"{base_url}/projects/{project_id}/users", api_key)
    output['assigneeId'] = {data['name']: data['id'] for data in datas}
    for name, id in output['assigneeId'].items():
        print(f"{id}:{name}")

    # categoryIdの取得と出力
    print('・categoryId(課題のカテゴリーのID)用')
    datas = get_id(f"{base_url}/projects/{project_id}/categories", api_key)
    output['categoryId[]'] = {data['name']: data['id'] for data in datas}
    for name, id in output['categoryId[]'].items():
        print(f"{id}:{name}")

    # versionIdとmilestoneIdの取得と出力
    print('・versionId(課題の発生バージョンのID)、milestoneId(課題のマイルストーンのID)用')
    datas = get_id(f"{base_url}/projects/{project_id}/versions", api_key)
    output['versionId'] = {}
    output['milestoneId'] = {}
    for data in datas:
        output['versionId'][data['name']] = data['id']
        output['milestoneId'][data['name']] = data['id']
        print(f"{data['id']}:{data['name']}")

    # priorityIdの取得と出力
    print('・priorityId(課題の優先度のID)用')
    datas = get_id(f"{base_url}/priorities", api_key)
    output['priorityId'] = {data['name']: data['id'] for data in datas}
    for name, id in output['priorityId'].items():
        print(f"{id}:{name}")

    # customField_{id}の取得と出力
    datas = get_id(f"{base_url}/projects/{project_id}/customFields", api_key)
    for data in datas:
        field_key = f"customField_{data['id']}"
        print(f"・{field_key}({data['name']})用")
        output[field_key] = {item['name']: item['id'] for item in data['items']}
        for name, id in output[field_key].items():
            print(f"{id}:{name}")

    return output


def save_to_json(output: Dict[str, Dict[str, int]], file_name: str, directory: str) -> None:
    """
    指定されたディクショナリをJSONファイルとして保存する。

    Parameters:
    - output (Dict[str, Dict[str, int]]): 保存するデータ
    - file_name (str): 保存するファイルの名前
    - directory (str): データを保存するディレクトリ
    """
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(f"ディレクトリの作成中にエラーが発生しました: {e}")
            traceback.print_exc()
            sys.exit(1)

    # 出力ファイルパスの作成
    output_file_path = os.path.join(directory, file_name)

    # 出力結果をJSONファイルに保存
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
        print(f"データを '{output_file_path}' に保存しました。")
    except Exception as e:
        print(f"ファイルの保存中にエラーが発生しました: {e}")
        traceback.print_exc()


def main() -> None:
    # 環境変数を取得
    api_key = check_env_var('BACKLOG_API_KEY')
    space_key = check_env_var('BACKLOG_SPACE_KEY')
    project_id = check_env_var('BACKLOG_PROJECT_ID')
    base_url = f"https://{space_key}/api/v2"

    # IDの取得と出力
    output = fetch_and_output_ids(api_key, base_url, project_id)

    # 出力結果をJSONファイルに保存
    save_to_json(output, 'id_list.json', 'output')

if __name__=="__main__":
    main()