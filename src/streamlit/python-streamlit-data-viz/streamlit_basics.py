import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk
from PIL import Image
import time

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [40, 30, 20, 10]
# })

# df

# x = 100
# x


"""
# マジックコマンドを使用
文字列の表示

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

print("Hello Python!")
```
"""


# # マジックコマンドでのグラフ生成
# df = pd.DataFrame(np.random.randn(20, 3),
#                 columns=['a', 'b', 'c'])
# df


# # Streamlitが用意しているグラフ生成(インタラクティブな動作ができる)
# st.line_chart(df)
# st.area_chart(df) # 麺グラフ
# st.bar_chart(df) # 棒グラフ

fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]
ax.plot(x, y) # 折れ線グラフ

# Streamlitでpyplotをそのまま呼び出す
st.pyplot(fig) # 注意点としてmatplotlibで生成したグラフはインタラクティブな動作ができない

"""
## 東京の県庁所在地付近のランダムなデータ
"""
# 東京の県庁所在地緯度経度
tokyo_lat = 35.69
tokyo_lon = 139.69

df_tokyo = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [tokyo_lat, tokyo_lon],
    columns=['lat', 'lon']
)
df_tokyo

"""
## 東京の県庁所在地を中心にランダムなデータを地図にプロット
"""
st.map(df_tokyo)

"""
## 地図グラフの表示（3次元）
"""
# 東京の県庁所在地周辺にこのヘキサゴンのレイヤーを描く
view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

hexagon_layeer = pdk.Layer('HexagonLayer', # どの可視化方法か
                           data=df_tokyo,
                           get_position = ['lon', 'lat'],
                           elevation_scale=6,
                           radius=200,
                           extruded=True
                           )

layer_map = pdk.Deck(layers=hexagon_layeer, initial_view_state=view)

st.pydeck_chart(layer_map)



"""
## 画像の表示
"""
image = Image.open('images/cat0045-026.jpg')

st.image(image, caption='子猫', use_column_width=True)


"""
## インタラクティブ機能
"""
option_button = st.button('ボタン')

if option_button == True:
    st.write('ボタンが押されました')
else:
    st.write('ボタンを押してください')
    
# ラジオボタン
option_radio_button = st.radio(
    "好きな食べ物を選択してください",
    ('りんご', 'バナナ', 'オレンジ', 'その他')
)

st.write('あなたが選んだ果物は：', option_radio_button)


option_checkbox = st.checkbox('DataFreamの表示')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

if option_checkbox == True:
    st.write(df)
    
option_selectbox = st.selectbox(
    'どれか一つ選択してください',
    ('A', 'B', 'C'))
st.write('あなたが選んだのは；', option_selectbox)

# マルチセレクト
option_multi_select = st.multiselect(
    '好きな色を選択してください',
    ['緑', '黄色', '赤', '青'],
    ['黄色', '赤'] # デフォルトの選択
)

# スライダー
age = st.slider('あなたの年齢を教えてください', min_value=0, max_value=130, step=1, value=20)
st.write('私の年齢は', age, 'です')

values = st.slider(
    '数値の範囲を入力してください',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)


# サイドバー
height = st.sidebar.slider('あなたの身長(cm)を入力してください', min_value=0, max_value=200, step=1, value=170)
st.write('私の身長は', height, 'cmです')

gender = st.sidebar.selectbox(
    'あなたの性別を教えてください',
    ['男性', '女性']
)
st.write('あなたの性別は：', gender)

# プログレスバー
progres_button = st.button('プログレスボタン')
if progres_button == True:
    st.write('処理を開始します')
    my_bar = st.progress(0)
    for percent_comlete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_comlete + 1)
    st.text('処理が終了しました')
else:
    st.write('プログレスボタンを押してください')