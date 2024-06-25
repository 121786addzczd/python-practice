import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px


st.title('日本の賃金データダッシュボード')

df_jp_ind = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_全国_全産業.csv', encoding='shift_jis')
df_jp_category = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_全国_大分類.csv', encoding='shift_jis')
df_pref_ind = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_都道府県_全産業.csv', encoding='shift_jis')

st.header('■2019年：一人当たり平均賃金のヒートマップ')

jp_lat_lon = pd.read_csv('./csv_data/pref_lat_lon.csv') # 47都道府県の県庁所在地の全ての情報が格納されているファイル
jp_lat_lon = jp_lat_lon.rename(columns={'pref_name': '都道府県名'}) # 読み込んだCSVのデータフレームの列名を日本語版名にリネーム

df_pref_map = df_pref_ind[(df_pref_ind['年齢'] == '年齢計') & (df_pref_ind['集計年'] == 2019)]
df_pref_map = pd.merge(df_pref_map, jp_lat_lon, on='都道府県名') 
# 最小値0, 最大値1とする正規化処理
df_pref_map['一人当たり賃金（相対値）'] = ((df_pref_map['一人当たり賃金（万円）'] - df_pref_map['一人当たり賃金（万円）'].min()) / (df_pref_map['一人当たり賃金（万円）'].max() - df_pref_map['一人当たり賃金（万円）'].min()))

# longitude,latitudeは東京の県庁所在地
view = pdk.ViewState(
    longitude=139.691648,
    latitude=35.689185,
    zoom=4,
    pitch=40.5,
)
# レイヤー
layer = pdk.Layer(
    "HeatmapLayer",
    data=df_pref_map,
    opacity=0.4,
    get_position=["lon", "lat"],
    threshold=0.3,
    get_weight = '一人当たり賃金（相対値）'
)
# レンダリング
layer_map = pdk.Deck(
    layers=layer,
    initial_view_state=view,
)
# 表示
st.pydeck_chart(layer_map)

show_df = st.checkbox('データフレームを表示する')
if show_df == True:
    st.write(df_pref_map)



st.header('■集計年別の一人当たり賃金（万円）の推移')

df_ts_mean = df_jp_ind[(df_jp_ind["年齢"] == "年齢計")]
df_ts_mean = df_ts_mean.rename(columns={'一人当たり賃金（万円）': '全国_一人当たり賃金（万円）'})

df_pref_mean = df_pref_ind[(df_pref_ind["年齢"] == "年齢計")]
pref_list = df_pref_mean['都道府県名'].unique()
option_pref = st.selectbox(
    '都道府県',
    (pref_list))
df_pref_mean = df_pref_mean[df_pref_mean['都道府県名'] == option_pref]

df_mean_line = pd.merge(df_ts_mean, df_pref_mean, on='集計年')
df_mean_line = df_mean_line[['集計年', '全国_一人当たり賃金（万円）', '一人当たり賃金（万円）']] # 必要な列だけに絞る
df_mean_line = df_mean_line.set_index('集計年') # 集計年をインデックスにする
st.line_chart(df_mean_line)



st.header('■年齢階級別の全国一人あたり平均賃金（万円）')

df_mean_bubble = df_jp_ind[df_jp_ind['年齢'] != '年齢計'] # 年齢計の行は除外
# バルチャートで表示する
fig = px.scatter(df_mean_bubble,
                x="一人当たり賃金（万円）",
                y="年間賞与その他特別給与額（万円）",
                range_x=[150,700],
                range_y=[0,150],
                size="所定内給与額（万円）",
	            size_max = 38, # 2010〜2019年の所定内給与額（万円）の最大に近い数値を設定
                color="年齢", # 色分けする
                animation_frame="集計年", # 集計年ごとの推移をみたい
                animation_group="年齢")

st.plotly_chart(fig)
