import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("2022 LOL 월드 챔피언십 우승 팀 DRX의 경기 데이터 리뷰 및 승리 요인 분석")
st.write("2022-2학기 데이터 저널리즘 과제전 9조")
st.write("자유전공학부 조건희")
st.write("언론정보학과 허현준")
st.write("")
st.write("")
st.write("")
st.write("LOL 월드 챔피언십은 세계 최대 규모의 e스포츠 대회로 알려져 있다.")
st.write("올해 10월 펼쳐진 통산 12번째 대회에서, 한국의 e스포츠 팀 DRX가 한국의 4번시드로 출전하여, 모두의 예상을 뒤엎고 우승하는 일이 벌어졌다.")
st.write("그 과정에서 기존 우승 후보들을 모두 꺾고 우승한 만큼, 이는 LOL e스포츠 역사상 최고의 업셋이라고 평가받는다.")
st.write("본 보고서에서는 LOL e스포츠 대회 통계 사이트의 데이터를 크롤링 및 분석하여, DRX가 다른 우승 후보들을 제치고 우승할 수 있었던 요인에 대해 알아보고, 그 과정에서 특별했던 점들은 무엇인지 살펴볼 것이다.")
st.write("")
st.write("")
st.write("")
st.write("먼저,")

st.subheader("골드")
data = pd.read_excel("Gold.xlsx")
data = data.fillna("")
data.index = data.Time
data = data.drop(["Time"], axis=1)
st.dataframe(data)
#RGE1 = data.
#gold_df = pd.DataFrame
