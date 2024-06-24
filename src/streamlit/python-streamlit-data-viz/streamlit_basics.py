import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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