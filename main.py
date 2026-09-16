import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"

df = pd.read_csv(DATA_URL)

df["openDt"] = pd.to_datetime(
df["openDt"].astype(str),
format="%Y%m%d",
errors="coerce"
)

df["genre"] = df["genre"].fillna("").astype(str)
df["genre"] = df["genre"].str.split("|").str[0].str.strip()

# 그래프 1

st.header("1. 장르별 영화 편수")

genre_count = df["genre"].value_counts().reset_index()
genre_count.columns = ["장르", "영화 편수"]

fig1 = px.pie(
genre_count,
names="장르",
values="영화 편수",
hole=0.5,
title="장르별 영화 편수"
)

fig1.update_traces(
textinfo="label+percent",
hovertemplate="<b>%{label}</b><br>영화 편수: %{value}편<br>비율: %{percent}<extra></extra>"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")

st.write("특정 장르의 영화가 다른 장르보다 더 많이 있다는 것을 알 수 있다.")

# 그래프 2

st.divider()

st.header("2. 장르별 영화와 총 관객")

fig2 = px.treemap(
df,
path=["genre", "movieNm"],
values="total_audi",
title="장르별 영화와 총 관객"
)

fig2.update_traces(
hovertemplate="<b>%{label}</b><br>총 관객: %{value:,}명<extra></extra>"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")

st.write("같은 장르 안에서도 영화마다 총 관객 수에 큰 차이가 있다는 것을 알 수 있다.")

st.divider()
