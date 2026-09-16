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

# 그래프 3

st.divider()

st.header("3. 총 관객 수의 분포")

fig3 = px.histogram(
df,
x="total_audi",
nbins=20,
title="영화별 총 관객 수 분포",
labels={
"total_audi": "총 관객 수",
"count": "영화 편수"
}
)

fig3.update_traces(
hovertemplate="총 관객 수: %{x:,}명<br>영화 편수: %{y}편<extra></extra>"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")
st.write("대부분의 영화는 총 관객이 비슷한 구간에 몰려 있고, 가장 관객이 많은 영화는 왕과 사는 남자이다.")

# 그래프 4

st.divider()

st.header("4. 개봉일 스크린수와 총 관객의 관계")

fig4 = px.scatter(
df,
x="first_scrn",
y="total_audi",
color="genre",
hover_name="movieNm",
title="개봉일 스크린수와 총 관객",
labels={
"first_scrn": "개봉일 스크린수",
"total_audi": "총 관객",
"genre": "장르"
}
)

fig4.update_traces(
hovertemplate=(
"<b>%{hovertext}</b><br>"
"개봉일 스크린수: %{x:,}개<br>"
"총 관객: %{y:,}명"
"<extra></extra>"
)
)

st.plotly_chart(fig4, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")
st.write("개봉일 스크린수가 많을수록 총 관객도 많아지는 경향이 있는지 확인할 수 있다.")

# 그래프 5

st.divider()

st.header("5. 장르별 총 관객 분포")

# 장르별 영화 편수가 10편 이상인 장르만 선택

genre_counts = df["genre"].value_counts()

valid_genres = genre_counts[genre_counts >= 10].index

df_box = df[df["genre"].isin(valid_genres)].copy()

fig5 = px.box(
df_box,
x="genre",
y="total_audi",
points="outliers",
hover_name="movieNm",
title="영화가 10편 이상인 장르의 총 관객 분포",
labels={
"genre": "장르",
"total_audi": "총 관객"
}
)

fig5.update_traces(
hovertemplate=(
"<b>%{hovertext}</b><br>"
"총 관객: %{y:,}명"
"<extra></extra>"
)
)

st.plotly_chart(fig5, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")
st.write("장르에 따라 총 관객 수의 분포와 차이가 다르게 나타나는 것을 알 수 있다.")

st.divider()
