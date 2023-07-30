import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib


# データを読み込み
df = pd.read_csv('csv_files/send3.csv', parse_dates=['target_date'])

# バーの幅とバー間の間隔を指定
bar_width = 0.25
bar_interval = 0.5  # 時間帯間の間隔

# データを日付でグループ化
grouped = df.groupby(df['target_date'].dt.date)

# グループごとにグラフを生成
fig, axs = plt.subplots(len(grouped), 1, figsize=(12, 6 * len(grouped)))

# 色を定義
colors = ['lightgreen', 'skyblue', 'lightslategray']

for ax, (date, group) in zip(axs, grouped):
    # cpnameの一覧を取得
    cpnames = group['cpname'].unique()

    # データを時間ごとにプロット
    for j, cpname in enumerate(cpnames):
        df_cpname = group[group['cpname'] == cpname]
        bars = ax.bar(df_cpname['target_date'].dt.hour + j*bar_width, df_cpname['count'], width=bar_width, label=cpname, color=colors[j])
        
        # バーの上に個数を表示
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.05, yval, ha='center', va='bottom')
    
    # 合計の棒グラフを追加
    df_total = group.groupby(group['target_date'].dt.hour)['count'].sum().reset_index()
    bars = ax.bar(df_total['target_date'] + len(cpnames)*bar_width, df_total['count'], width=bar_width, label='合計', color=colors[2], alpha=0.5)
    
    # バーの上に個数を表示
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.05, yval, ha='center', va='bottom')

    # グラフのラベルを設定
    ax.set_xlabel('配信時間', fontsize=15)
    ax.set_ylabel('配信数', fontsize=15)
    ax.set_title(f'シナリオ③ {date}', fontsize=18)
    
    # 凡例の位置を図の右上隅に設定
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    # x軸のティックを調整
    ax.set_xticks(np.arange(10, 23) * (bar_width * len(cpnames) + bar_interval))
    ax.set_xticklabels([f'{k}:00' for k in range(10, 23)])

# グラフを表示
plt.tight_layout()
plt.subplots_adjust(right=0.8)
plt.savefig('シナリオ配信③グラフ.png')