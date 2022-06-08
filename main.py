import streamlit as st
import time

st.title('steramlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40]
# })

# st.dataframe(df.style.highlight_max(axis=0)) # 動的な表
# st.table(df.style.highlight_max(axis=0)) # 静的な表

# マークアップ言語も対応
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# # st.line_chart(df)
# # st.area_chart(df)
# # st.bar_chart(df)

# st.map(df)

st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='toshi', use_column_width=True)

st.sidebar.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です'

text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'
