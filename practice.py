import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import datetime

data = pd.read_csv("practice1.csv")


st.title('受講者数可視化アプリ')

st.sidebar.write("""## 表示年度選択""")
s_year, e_year = st.sidebar.slider(
    '範囲を指定してください。',
    2010, 2022, (2010, 2022)
)
domain_pd = pd.to_datetime(
    [str(s_year)+'-01-01', str(e_year)+'-01-01']).astype(int) / 10 ** 6


st.sidebar.write("""## 人数の範囲""")
ymin, ymax = st.sidebar.slider(
    '範囲を指定してください。',
    0, 15, (0, 12)
)


shiken = st.multiselect(
    '試験を選択してください。',
    list(data["試験名称"].unique().tolist()),
    ['ITﾊﾟｽﾎﾟｰﾄ', '支援士']
)
data = data[data["試験名称"].isin(shiken)]
chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8, clip=True)
    .encode(
        x=alt.X("年度:T",
                scale=alt.Scale(domain=list(domain_pd))),
        y=alt.Y("人数:Q", stack=None,
                scale=alt.Scale(domain=[ymin*10000, ymax*10000])),
        color='試験名称:N'
    )
)
st.altair_chart(chart, use_container_width=True)
