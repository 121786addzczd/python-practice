import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk

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