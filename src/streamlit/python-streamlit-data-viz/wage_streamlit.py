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
df_pref_map


