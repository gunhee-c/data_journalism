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
gold_data = data.transpose()
gold_data.rename(columns=gold_data.iloc[0], inplace=True)
gold_data = gold_data.drop(gold_data.index[0])
st.line_chart(gold_data)

# install these

from bs4 import BeautifulSoup
from IPython.utils.path import target_update
from urllib.request import urlopen 

from urllib.error import URLError, HTTPError


#Data Analysis Main Function
def data_master(url_tournament):
  #search tournament-ranking 
  url_pblist = url_tournament.replace("stats", "picksandbans")
  #print(url_pblist)
  url_teamlist = url_tournament.replace("stats", "ranking")

  teamlist = teams_finder(url_teamlist)
  team_names = teamlist[1]
  team_links = teamlist[0]
  
  pickban_url = urlopen(url_pblist)
  pickban_dict = pb_datamaker(pickban_url)
  #해당 대회 픽밴 경향성 파악
  #print(pickban_dict)

  PB = [];
  KP = [];
  DMG = [];
  GOLD = []


  for i in range(len(team_links)):
    #print(team_names[i])
    #print(team_links[i]);
    team_url = urlopen(team_links[i])
    team_url2 = urlopen(team_links[i])

    team_picks_dict = team_picks(team_url)
    #print(team_picks_dict)
    pickban_grade = team_pb_grade(pickban_dict, team_picks_dict)
    #print("pick-ban evaluation: " + str(pickban_grade))   
    
    balance_data = KPDMGGOLD(team_url2)


    #print("KP: " + str(balance_data[0]))
    #print("DMG%: " + str(balance_data[1]))
    #print("GOLD%: " + str(balance_data[2]))
    #print()

    PB.append(pickban_grade)
    KP.append(balance_data[0])
    DMG.append(balance_data[1])
    GOLD.append(balance_data[2])
    #print(PB)
  return [team_names, PB, KP, DMG, GOLD]
    
# find all team links in a certain tournament
# returns [teamlinks[], teamnames[]]
def teams_finder(url):
  addme = "https://gol.gg"
  ans = [[],[]]

  parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
  resp = urllib.request.urlopen(url)
  soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

  for link in soup.find_all('a', href=True):
    if 'team-stats' in link['href']:
      ans[0].append(str(addme + link['href'][2:]))
      ans[1].append(str(link.get_text()))
  return ans

# get KP%, DMG%, GOLD% of each teammates
#return in formate [KP%[], DMG%[], GOLD%[]]
def KPDMGGOLD(url):
  soup = BeautifulSoup(url, "html.parser")
  parseme = soup.find_all('td', class_="text-center")
  treatme = []
  for i in range(len(parseme)):
    if "a href" not in str(parseme[i]):
      if "%" in str(parseme[i]):
        treatme.append(parseme[i])
  treatme.pop(0)
  KP = [];
  DMG = [];
  GOLD = [];
  for i in range(15):
    if len(str(treatme[i]))<40:
      data = re.findall(">.*?<", str(treatme[i]))
      data[0] = float(data[0][1:-2])
      KP.append(data[0])
    else:
      data = re.findall("x\">.*?</s", str(treatme[i]))
      data[0] = float(data[0][3:-4])
      if (i%3 ==1):
        DMG.append(data[0])
      else:
        GOLD.append(data[0])
  return [KP,DMG,GOLD]

# get tournament pickban dict, team's pick dict
# returns a float number that shows the team's pick-ban performance
# result is dependent to total # of games in a tournament
def team_pb_grade(tournament, team):
  evaluator = 0;
  counter  = 0;
  for key in team:
    counter += team[key]
    evaluator += team[key] * math.sqrt(tournament[key])
  return evaluator/counter

#Receive pick-ban data of a tournament in a form of dictionary
#score = sum of picks and bans from all lines
def pb_datamaker(url):
  #url_open = urlopen(url)
  #soup = BeautifulSoup(url_open, "html.parser")
  soup = BeautifulSoup(url, "html.parser")
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

#Receive the data of champions picked by a certain team in a tournament

def team_picks(url):
  #team_url = urlopen(url)
  #soup = BeautifulSoup(team_url, "html.parser")
  soup = BeautifulSoup(url, "html.parser")
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

worlds2022 = data_master("https://gol.gg/tournament/tournament-stats/World%20Championship%202022/")
st.subheader("list of teams")
st.write(worlds2022[0])
st.subheader("their pick-ban score")
st.write(worlds2022[1])
st.subheader("their kill participation distribution")
st.write(worlds2022[2])
st.subheader("their DMG distribution")
st.write(worlds2022[3])
st.subheader("their Gold distribution")
st.write(worlds2022[4])
