import streamlit as st
import pandas as pd

st.title('タイトル表示')
st.header('ヘッダーの表示')
st.subheader('サブヘッダーの表示')
st.text('テキストの表示')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

st.write(df)

# 縦と横の長さ指定ができる
st.dataframe(df, width=400, height=400)
# 各列の最大値をハイライトさせる
st.dataframe(df.style.highlight_max(axis=0))

# 動きが固定されたテーブルになる
st.table(df)