import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv")

@st.cache_data
def load_data():
df = pd.read_csv(DATA_URL)

```
df["openDt"] = pd.to_datetime(
    df["openDt"].astype(str),
    format="%Y%m%d",
    errors="coerce"
)

# 여러 장르가 있는 경우 첫 번째 장르만 사용
df["genre"] = df["genre"].fillna("").astype(str)
df["genre"] = df["genre"].str.split("|").str[0].str.strip()

return df
```

df = load_data()

st.header("1. 장르별 영화 편수")

genre_count = df["genre"].value_counts().reset_index()
genre_count.columns = ["장르", "영화 편수"]

fig = px.pie(
genre_count,
names="장르",
values="영화 편수",
hole=0.5,
title="장르별 영화 편수"
)

fig.update_traces(
textinfo="label+percent",
hovertemplate=(
"<b>%{label}</b><br>"
"영화 편수: %{value}편<br>"
"비율: %{percent}"
"<extra></extra>"
)
)

fig.update_layout(
legend_title_text="장르"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("이 그래프로 알 수 있는 것")

st.write(
"특정 장르의 영화가 다른 장르보다 더 많이 있다는 것을 알 수 있다."
)

st.divider()
