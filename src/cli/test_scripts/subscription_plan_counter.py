"""
subscription_plan_counter.py

このスクリプトは、ユーザーのサブスクリプションプランの状態を分析し、free、basic、premiumの各プランごとにユーザー数を集計します。擬似的なユーザーデータを用いて、現在アクティブなプランと終了したプランのユーザー数を計算します。

主な機能:
- UserクラスとSubscribingPlanクラスを定義し、ユーザー情報とサブスクリプションプランの状態を表現。
- 現在の日時（JSTを想定）を基準にして、サブスクリプションプランの終了状態を判定。
- サブスクリプションが終了しているユーザーはfreeプランにカウントし、それ以外のユーザーをそれぞれのプラン（basic、premium）にカウント。
- 最終的な各プランごとのユーザー数を集計し、出力。

注意点:
- このスクリプトは擬似的なデータを使用しており、実際のユーザーデータベースやサブスクリプション管理システムと連携していません。
- 現在の日時はJSTで計算されていますが、タイムゾーンの設定には注意してください。
- サブスクリプションプランの状態変更やユーザーデータの更新には対応していません。

使用方法:
スクリプトを実行すると、定義された擬似的なユーザーデータに基づいて、各プランごとのユーザー数が集計され、結果が出力されます。実行確認やテスト用途に適しています。
"""
from datetime import datetime, timedelta

# 擬似的なUserとSubscribingPlanのクラスを定義
class User:
    def __init__(self, id, plan_kind, subscribingplans):
        self.id = id
        self.plan_kind = plan_kind
        self.subscribingplans = subscribingplans

class SubscribingPlan:
    def __init__(self, ended_date, status):
        self.ended_date = ended_date
        self.status = status

# 現在の日時を取得（JSTを想定）
current_time_jst = datetime.now() + timedelta(hours=9)

# 擬似的なユーザーデータのリストを作成
user_list = [
    User(id=1, plan_kind='basic', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
    User(id=2, plan_kind='premium', subscribingplans=[SubscribingPlan(ended_date=current_time_jst + timedelta(days=1), status=9)]),
    User(id=3, plan_kind='basic', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
    User(id=4, plan_kind='premium', subscribingplans=[SubscribingPlan(ended_date=current_time_jst + timedelta(days=15), status=9)]),
    User(id=5, plan_kind='basic', subscribingplans=[SubscribingPlan(ended_date=current_time_jst - timedelta(days=200), status=9)]),
    User(id=6, plan_kind='premium', subscribingplans=[SubscribingPlan(ended_date=current_time_jst - timedelta(days=20), status=9)]),
    User(id=7, plan_kind='premium', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
    User(id=8, plan_kind='basic', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
    User(id=9, plan_kind='basic', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
    User(id=10, plan_kind='premium', subscribingplans=[SubscribingPlan(ended_date=None, status=0)]),
]


def count_user_plans(user_list, current_time):
    plan_counts = {'free': 0, 'basic': 0, 'premium': 0}
    
    for user in user_list:
        # まずはユーザーのプランタイプに基づいてカウント
        plan_counts[user.plan_kind] += 1
        print(plan_counts[user.plan_kind], user.plan_kind)
        
        # サブスクリプションプランをチェックして、条件に応じてカウントを調整
        for plan in user.subscribingplans:
            if plan.ended_date and plan.ended_date < current_time:
                # サブスクリプションが終了している場合、freeにカウントを移動
                plan_counts['free'] += 1
                plan_counts[user.plan_kind] -= 1
                break  # 1ユーザーにつき1カウントのみを移動

    return plan_counts

# 関数を実行して結果を表示
plan_counts = count_user_plans(user_list, current_time_jst)
print(f"{plan_counts=}")