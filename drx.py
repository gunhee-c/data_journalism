import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

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
st.write("※ 본 연구에서 사용되는 모든 데이터는 https://gol.gg/tournament/tournament-stats/World%20Championship%202022/ 에서 발췌되었다.")
st.write("")
st.write("")
st.write("")

st.subheader("1. 챔피언 픽, 킬 비중, 데미지 비중 중심의 분석")
st.write("e스포츠는 패치가 지속적으로 행해지는 인터넷 게임의 특성상, 2~3주마다 서로 다른 버전으로 게임을 진행하게 된다.")
st.write("특히 LOL은 패치가 매우 자주, 그리고 가끔씩 과감하게 이루어지기 때문에, 게임 플레이어가 사용하는 캐릭터인 '챔피언'들이 선택되는 횟수 또한 패치 버전에 따라 자주 바뀐다.")
st.write("따라서 LOL 프로 팀의 선전 요인 중의 하나로 '메타 적합성', 다시 말해 패치 버전에 맞는 챔피언을 얼마나 잘 사용하는가를 이용할 수 있을 것이다.")
st.write("이에 따라 본 연구에서는 2022년 월드 챔피언십에서의 팀별 챔피언 선호도와, 대회의 전반적인 챔피언 선택 빈도를 연동하여 어떤 팀이 해당 대회의 패치 버전에 가장 적합한 챔피언들을 사용했는지 산술식을 만들어 계산해 보았다.")
st.write("sum(경기 내 해당 챔피언의 픽+밴횟수 * 해당 팀의 해당 챔피언 픽 횟수)/총 경기 횟수 로 계산하였다.")
#픽밴값을 구하는 과정
st.image("https://i.ibb.co/k9jJF6V/image.png")

st.write("")
st.write("킬 참여(KP%)와 데미지 비중(DMG%) 또한 중요한 데이터가 될 수 있다 생각했다.") 
st.write("한 두명의 선수에게 부담이 집중되는것 보다 모두가 돌아가면서 경기를 이끌 수 있는 팀이 더 좋은 성적을 내는 경향이 있다는 가정이 있었다.")

#SUM & VAR
st.image("https://i.ibb.co/LdFZFgb/DMGbalance.png")
st.write("실제로 DMG%를 비교하면 강력한 우승후보였지만 예상보다 일찍 떨어진 TES와 JDG의 경우보다 우승과 준우승을 나눈 DRX와 T1의 밸런스가 대회의 평균과 더 근접한다")
st.write("팀이 얼마나 많은 어시스트를 나누었는지 알 수 있는 Sum of Kill Participation")
st.write("각 라인의 밸런스를 가늠할 수 있는 DMG%, GOLD%, KP%의 각 라인별 대회 내 평균을 구한 뒤 평균과의 오차의 제곱을 합한 값을 구하였다.")
st.write("이를 앞으로 평균오차라고 부르기로 한다.")
st.write("KP%의 경우 총합이 나머지와 같이 100%가 되도록 추가로 조정하였다.")
st.write("")
st.write("승패의 비율과 관련이 적고, 최상위부터 최하위까지 팀 성향의 공정한 비교를 진행할 수 있는 데이터들로 선별하였다.")
         
st.write("픽밴과 각종 팀 단위 밸런스 수치들을 기록하고, 이를 순위로 나타낼 수 있게 하였다.")
st.write("각 대회마다 모든 팀의 정보에 대해 접근할 수 있도록 한 뒤,")
st.write("3강으로 분류되는 한국,중국,유럽의 Spring과 Summer 데이터와 5년간의 롤드컵 데이터들을 크롤링하여 데이터프레임의 리스트를 만들었다.")
#데이터프레임 형성
st.image("https://i.ibb.co/34TF6TF/datatable.png")
#results
st.write("모든 대회의 데이터들을 합친 뒤, 각 요인에 대한 Least Square Method를 통한 일차함수 근사를 통해 trend graph를 만들었다")
st.image("https://i.ibb.co/k4CbXfJ/All-Datas.png")
st.write("그 결과 픽밴, 킬관여율의 평균오차, 킬관여 총합, 데미지의 평균오차 순으로 연관성이 있는것으로 드러났고, 골드수급의 평균오차의 경우 연관성이 희미하다고 드러났다.")
st.write("이제 DRX의 픽밴 랭킹값과 킬관여 총합값의 변동을 LCK의 다른 세 팀 (T1, DRX, GENG)과 함께 비교해보자.")
st.image("https://i.ibb.co/2y4Bz7q/Comparison.png")
st.write("")
st.write("")
st.write("")
st.subheader("2. 경기 시간과 골드 변동 그래프를 통해 확인된 DRX의 끈질김")
st.write("여기")

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
#lst2의 값에 따라 lst1의 값을 sorting함. 오름차순.
def sortedpair(lst1, lst2):
  #print(lst2)
  lst2sort = lst2.copy()
  Z = [x for _,x in sorted(zip(lst2,lst1))]
  lst2sort.sort()
  return [Z,lst2sort]

#worlds2022 = data_master("https://gol.gg/tournament/tournament-stats/World%20Championship%202022/")
#st.subheader("list of teams")
#st.write(worlds2022[0])
#st.subheader("their pick-ban score")
#st.write(worlds2022[1])
#st.subheader("their kill participation distribution")
#st.write(worlds2022[2])
#st.subheader("their DMG distribution")
#st.write(worlds2022[3])
#st.subheader("their Gold distribution")
#st.write(worlds2022[4])




plt.title('Playtime of the Winner',fontsize=20) ## 타이틀 출력
plt.xlabel('Team',fontsize=15) ## x축 라벨 출력
plt.ylabel('seconds',fontsize=15) ## y축 라벨 출력
plt.show()


###
winner_team = ['DRX', 'EDG', 'DWG','FPX', 'IG', 'DRX_total', 'DRX_from_Korea']

winner_time = [43068, 41244, 31841, 33768, 32490, 52063, 71803]
colors = ['#62F2EC', '#C9D7DB', '#F05627', '#636363', '#3E95D6', '#B1C7F2','#B1C7F2']

sortme = sortedpair(winner_team, winner_time)
print(sortme[0])
print(sortme[1])
data = {"team": sortme[0], "seconds" : sortme[1], "colorme" : colors}

data = pd.DataFrame(data)

st.write(data)
st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('team', sort=None),
    y='seconds',
    color=alt.Color('colorme', scale=None)
    ).properties(
    width=600,
    height=600
    
)
)
###

rge_1 = [0,0,-24,-53,-7,-448,-540,337,-366,-205,150,289,408,15,-20,16,-257,-385,-1027,-1032,-1411,-1373,-2079,-2193,-1922,-1687,-1009,-1200,-2277,-3715,-5561,-4943,-4837,-4941,-4964,-5139,-9363,-9414,"","","","","","","","","",""]
tes_1 = [0,-5,-95,-238,-9,-52,-98,-115,363,172,-128,1446,3168,3166,4001,3941,4158,3723,4251,4524,5310,5517,5380,5331,5903,7399,7092,7637,10093,11262,13942,13992,"","","","","","","","","","","","","","","",""]
gam_1 = [0,0,943,1338,1538,1548,797,1024,1088,1326,1423,2451,2672,3130,3274,3548,4657,5045,5222,5086,5582,5388,6920,7930,9186,"","","","","","","","","","","","","","","","","","","","","","",""]
rge_2 = [0,-5,132,-191,119,245,236,103,474,2273,2558,2469,3078,3060,3507,4861,4661,5327,5447,6413,6820,6526,6549,7163,7184,9148,9010,9837,10250,12869,15033,16129,"","","","","","","","","","","","","","","",""]															
gam_2 = [0,0,-58,89,-704,-226,-66,-195,1116,1368,465,465,1519,844,1880,1976,2402,2464,3470,4252,3643,6099,7121,8314,8304,9019,8640,8509,9328,10730,11448,13209,16293,"","","","","","","","","","","","","","",""]													
tes_2 = [0,0,80,75,30,209,157,209,292,598,914,1390,1028,901,973,1826,1114,1741,2556,2600,1740,1480,1622,92,-1243,-1218,-1744,-2820,-2509,-2480,-2688,-2931,-2732,-5467,-10050,-10102,"","","","","","","","","","","",""]
rge_tie = [0,20,12,348,359,-569,-484,-338,-36,381,-503,-56,401,559,1099,2145,2450,3011,3066,4310,4601,5786,5768,7664,7870,10264,"","","","","","","","","","","","","","","","","","","","","",""]																					
edg_1 = [0,15,110,169,158,-116,45,156,405,-227,38,264,-83,-50,363,109,626,1205,2099,1759,1493,1737,771,771,1712,1434,1347,1409,1160,-781,-2912,-3464,-3579,-2541,-2848,-2066,-2066,"","","","","","","","","","",""]
edg_2 = [0,0,-35,-90,350,-394,-336,278,439,117,-42,164,1133,1342,939,830,586,1302,1827,4363,4521,4683,6095,6394,5673,5891,6528,6886,6415,6281,6723,7717,9243,10496,9606,9557,9788,8399,7516,6355,4461,2731,1610,-854,"","","",""]				
edg_3 = [0,0,23,67,84,29,-35,79,65,-648,-892,6,-356,-367,423,70,282,363,614,1367,991,-66,-378,-568,-1007,-1123,-1283,-1460,-1514,-2013,-2375,-2283,-1936,-2472,-3650,-12,1866,3863,4186,3737,4005,3445,5298,"","","","",""]
edg_4 = [0,0,58,412,644,511,766,0,-61,19,42,-421,-930,-1596,-1674,-1099,546,455,1624,1776,2175,2698,2815,2557,2942,2668,1979,1614,2000,50,872,2135,2283,4108,5028,4282,5296,7675,8182,11300,"","","","","","","",""]
edg_5 = [0,0,70,182,236,65,353,-370,43,-123,890,1017,977,1004,648,847,88,-275,-157,68,3600,3444,4442,4335,6059,6860,6582,6621,6698,8278,7215,7789,7763,6850,7247,7325,7381,6579,10610,"","","","","","","","",""]
gen_1 = [0,0,131,-7,42,-123,-285,167,552,302,139,188,37,-612,-1524,-2673,-2984,-3611,-3092,-3229,-4419,-4164,-4562,-4573,-4393,-4698,-7357,-7397,-9954,-10508,-13592,"","","","","","","","","","","","","","","","",""]
gen_2 = [0,0,75,22,-770,-803,-787,-1018,-570,-908,-456,-62,-292,-461,-645,-1230,-1399,-1900,-2282,-2323,-2428,-2454,-2471,-1400,-1340,-526,-250,-675,-870,-38,-133,27,490,2558,4380,4605,5028,5089,5181,6887,7520,"","","","","","",""]							
gen_3 = [0,-20,0,-142,441,709,556,1847,1768,1259,980,1411,1079,1877,3519,2980,3231,3088,3108,3260,3306,4378,4069,4179,6885,6807,7085,7458,7350,7189,11091,11140,"","","","","","","","","","","","","","","",""]																
gen_4 = [0,0,-21,-48,337,289,90,63,-61,728,-137,302,704,583,371,138,153,214,-695,-1024,-1034,-1417,-1466,-1621,-2047,-1923,-2100,-1364,271,938,1440,1678,1675,1653,1674,3533,4821,6913,9602,"","","","","","","","",""]									
t1_1 = [0,0,-23,-134,-216,290,-21,-398,-50,-602,-718,-717,-746,-1194,-1270,-1475,-1688,-1753,-1563,-2505,-3471,-4111,-7952,-8957,-7839,-6802,-7116,-6484,-8381,-8044,-8559,-8985,-11069,"","","","","","","","","","","","","","",""]															
t1_2 = [0,0,54,-30,128,197,230,207,236,533,176,-2141,-3032,-2053,-3079,-2626,-1843,-1855,-796,-984,-865,-63,461,418,286,521,139,-27,-56,242,-224,-944,-617,-1033,-708,2898,3871,3476,2247,912,-372,-624,-1028,-1893,-1612,-2440,631,931]
t1_3 = [0,0,55,26,11,-123,-669,-695,-944,-1130,-553,-1811,-1858,-1553,-867,-796,-162,-373,417,263,442,1147,80,-12,1028,-3073,-3749,-4936,-4083,-5427,-5169,-3793,-6531,-6285,"","","","","","","","","","","","","",""]	
t1_4 = [0,0,50,-91,-603,-352,-559,-251,-622,-473,-624,-43,-151,1105,1143,1289,4744,4400,3923,4131,5443,5866,6068,6223,6729,5511,7028,6396,6114,8367,"","","","","","","","","","","","","","","","","",""]																		
t1_5 = [0,0,47,-261,-796,-557,-632,-407,-334,-9,123,540,152,-512,269,-433,-547,-1486,-627,-1728,-968,-1657,-1166,-1587,-1215,-1401,-1801,-1714,-1755,-1392,-2553,-2133,-2251,-696,-16,-1865,-2329,-2865,-2730,-3578,-3439,-865,2422,2633,"","","",""]				      
index = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48']

df_rge_1 = pd.DataFrame({'vs RGE Game 1 (L)': rge_1}, index=index)
df_tes_1 = pd.DataFrame({'vs TES Game 1 (W)': tes_1}, index=index)
df_gam_1 = pd.DataFrame({'vs GAM Game 1 (W)': gam_1}, index=index)
df_rge_2 = pd.DataFrame({'vs RGE Game 2 (W)': rge_2}, index=index)
df_gam_2 = pd.DataFrame({'vs GAM Game 2 (W)': gam_2}, index=index)
df_tes_2 = pd.DataFrame({'vs TES Game 2 (L)': tes_2}, index=index)
df_rge_tie = pd.DataFrame({'vs RGE Tiebreaker (W)': rge_tie}, index=index)
df_edg_1 = pd.DataFrame({'vs EDG Game 1 (L)': edg_1}, index=index)
df_edg_2 = pd.DataFrame({'vs EDG Game 2 (L)': edg_2}, index=index)
df_edg_3 = pd.DataFrame({'vs EDG Game 3 (W)': edg_3}, index=index)
df_edg_4 = pd.DataFrame({'vs EDG Game 4 (W)': edg_4}, index=index)
df_edg_5 = pd.DataFrame({'vs EDG Game 5 (W)': edg_5}, index=index)
df_gen_1 = pd.DataFrame({'vs GEN Game 1 (L)': gen_1}, index=index)
df_gen_2 = pd.DataFrame({'vs GEN Game 2 (W)': gen_2}, index=index)
df_gen_3 = pd.DataFrame({'vs GEN Game 3 (W)': gen_3}, index=index)
df_gen_4 = pd.DataFrame({'vs GEN Game 4 (W)': gen_4}, index=index)
df_t1_1 = pd.DataFrame({'vs T1 Game 1 (L)': t1_1}, index=index)
df_t1_2 = pd.DataFrame({'vs T1 Game 2 (W)': t1_2}, index=index)
df_t1_3 = pd.DataFrame({'vs T1 Game 3 (L)': t1_3}, index=index)
df_t1_4 = pd.DataFrame({'vs T1 Game 4 (W)': t1_4}, index=index)
df_t1_5 = pd.DataFrame({'vs T1 Game 5 (W)': t1_5}, index=index)

fig_rge_1 = px.line(df_rge_1)
fig_tes_1 = px.line(df_tes_1)
fig_gam_1 = px.line(df_gam_1)
fig_rge_2 = px.line(df_rge_2)
fig_gam_2 = px.line(df_gam_2)
fig_tes_2 = px.line(df_tes_2)
fig_rge_tie = px.line(df_rge_tie)
fig_edg_1 = px.line(df_edg_1)
fig_edg_2 = px.line(df_edg_2)
fig_edg_3 = px.line(df_edg_3)
fig_edg_4 = px.line(df_edg_4)
fig_edg_5 = px.line(df_edg_5)
fig_gen_1 = px.line(df_gen_1)
fig_gen_2 = px.line(df_gen_2)
fig_gen_3 = px.line(df_gen_3)
fig_gen_4 = px.line(df_gen_4)
fig_t1_1 = px.line(df_t1_1)
fig_t1_2 = px.line(df_t1_2)
fig_t1_3 = px.line(df_t1_3)
fig_t1_4 = px.line(df_t1_4)
fig_t1_5 = px.line(df_t1_5)

st.plotly_chart(fig_rge_1)
st.plotly_chart(fig_tes_1)
st.plotly_chart(fig_gam_1)
st.plotly_chart(fig_rge_2)
st.plotly_chart(fig_gam_2)
st.plotly_chart(fig_tes_2)
st.plotly_chart(fig_rge_tie)
st.plotly_chart(fig_edg_1)
st.plotly_chart(fig_edg_2)
st.plotly_chart(fig_edg_3)
st.plotly_chart(fig_edg_4)
st.plotly_chart(fig_edg_5)
st.plotly_chart(fig_gen_1)
st.plotly_chart(fig_gen_2)
st.plotly_chart(fig_gen_3)
st.plotly_chart(fig_gen_4)
st.plotly_chart(fig_t1_1)
st.plotly_chart(fig_t1_2)
st.plotly_chart(fig_t1_3)
st.plotly_chart(fig_t1_4)
st.plotly_chart(fig_t1_5)


