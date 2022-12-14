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

#
# ans[0] = team url links, ans[1] = team names
def teams_finder(url):
  addme = "https://gol.gg"
  ans = [[],[]]

  parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
  resp = urllib.request.urlopen(url)
  soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

  for link in soup.find_all('a', href=True):
    if 'team-stats' in link['href']:
      ans[0].append(addme + link['href'][2:])
      ans[1].append(link.get_text())
      print(addme + link['href'][2:])
      print(link.get_text())

#make dictionary of pick-ban of certain tournament
def pb_datamaker(url):
  url_open = urlopen(url)
  soup = BeautifulSoup(url_open, "html.parser")
  pb = soup.find_all('td')
  pickbans = {}
  pbs = [pb[5], pb[7], pb[9], pb[11], pb[13], pb[15]] 
  for i in range(len(pbs)):
    if i == 0:
      nums = re.findall("\r\n.*?</span>", str(pbs[i]))
    else:
      nums = re.findall("</div>.*?</div>", str(pbs[i]))
    champs = re.findall("title=.*? stats", str(pbs[i]))
    for j in range(len(champs)):
      if i == 0:
        numdata = int(nums[j][9:-7])
      else: 
        numdata = int(nums[j][6:-6])
      champdata = champs[j][7:-6]
      if champdata in pickbans:
        pickbans[champdata] += numdata
      else:
        pickbans.update({champdata : numdata})
  return pickbans


#get team's pick record
def team_picks(url):
  team_url = urlopen(url)
  soup = BeautifulSoup(team_url, "html.parser")
  parseme = soup.find_all('span', class_="text-center")
  dictout = {}
  for i in range(len(parseme)):
    num = re.findall("</a><br/>\r\n.*?</span>", str(parseme[i]))
    champ = re.findall("title=.*? stats", str(parseme[i]))
    numdata = int(num[0][18:-7])
    champdata = champ[0][7:-6]
    if champdata[0] in dictout:
      dictout[champdata] += numdata
    else:
      dictout.update({champdata : numdata})

  return dictout
      
#get team's pick ban grade
def team_pb_grade(url_tournament, url_team):
  pb_data = pb_datamaker(url_tournament)
  pb_team = team_picks(url_team)
  evaluator = 0;
  counter  = 0;
  for key in pb_team:
    counter += pb_team[key]
    evaluator += pb_team[key] * math.sqrt(pb_data[key])
  return evaluator/counter

#

#
def

#
