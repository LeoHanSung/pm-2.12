import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

zz = pd.read_csv('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\COUNT_T_MERGE2.csv')
# 날짜별 뉴스기사 개수
kk = pd.read_csv('C:\\Users\\USER\\Downloads\\SNS\\datalab.csv')
# 날짜별 미세먼지 검색률

tt = list(kk['Date'])
tt = [t[:4]+t[5:7]+t[8:10] for t in tt]
kk['Date'] = tt
# 날짜 형식 통일

ddd = ['20180415','20180529','20180601','20190109','20190123','20190124','20190207','20190208','20190216','20190222','20190223','20190308','20190309','20190310','20190318','20190325']
# 결측치에 해당하는 날짜 리스트

aa1 = list(kk.index)
aa2 = list(kk['Date'])
dic = dict(zip(aa1,aa2))
# 인덱스, 날짜를 각각 리스트로 만들어 딕셔너리 형식 생성

nulldate = []
for ind, dat in dic.items(): # 딕셔너리 아이템 하나씩 접근해서, key, value를 각각 idx, dat에 저장
    if dat in ddd:
        print(ind)
        nulldate.append(ind)
# 결측치 해당 날짜의 인덱스를 리스트 nulldate에 append
    
for n in nulldate :
    kk = kk.drop(n)
# for문 돌면서 nulldate 안의 인덱스에 해당하는 행 drop    
kk.dropna()
# 결측치 있다면 제거
kk = kk.reset_index(drop=True)
# 인덱스 리셋

ee = pd.read_excel('pm10_all6.xlsx')
# 전국 pm10 미세먼지 지수화

for n in nulldate :
    ee = ee.drop(n)
ee = ee.reset_index(drop=True)

ee2 = pd.read_csv('C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING\\cardamount2.csv')
# 총 카드이용금액
for n in nulldate 
    ee2 = ee2.drop(n)
ee2 = ee2.reset_index(drop=True)

ee3 = pd.read_csv('C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING\\cardamount21_2.csv')
# 레저업소 업종 카드이용금액
for n in nulldate :
    ee3 = ee3.drop(n)
ee3 = ee3.reset_index(drop=True)

ee4 = pd.read_csv('C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING\\cardamount22_2.csv')
# 문화취미 업종 카드이용금액
for n in nulldate :
    ee4 = ee4.drop(n)
ee4 = ee4.reset_index(drop=True)

ee5 = pd.read_csv('C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING\\cardamount70_2.csv')
# 의료기관 업종 카드이용금액
for n in nulldate :
    ee5 = ee5.drop(n)
ee5 = ee5.reset_index(drop=True)

ee6 = pd.read_csv('C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING\\cardamount71_2.csv')
# 보건위생 업종 카드이용금액
for n in nulldate :
    ee6 = ee6.drop(n)
ee6 = ee6.reset_index(drop=True)

df = pd.DataFrame()
df['Count'] = zz['COUNT_T']
df['Search'] = kk['Dust']
df['Index'] = ee['Index']
df['USE_AMT'] = ee2['USE_AMT']
df['USE_AMT21'] = ee3['USE_AMT21']
df['USE_AMT22'] = ee4['USE_AMT22']
df['USE_AMT70'] = ee5['USE_AMT70']
df['USE_AMT71'] = ee6['USE_AMT71']
# 새로운 데이터프레임 생성

df['Count_index'] = 100 * df['Count'] / df['Count'].iloc[0]
df['Search_index'] = 100 * df['Search'] / df['Search'].iloc[0]
df['Index_index'] = 100 * df['Index'] / df['Index'].iloc[0]
df['AMT_index'] = 100 * df['USE_AMT'] / df['USE_AMT'].iloc[0]
df['AMT21_index'] = 100 * df['USE_AMT21'] / df['USE_AMT21'].iloc[0]
df['AMT22_index'] = 100 * df['USE_AMT22'] / df['USE_AMT22'].iloc[0]
df['AMT70_index'] = 100 * df['USE_AMT70'] / df['USE_AMT70'].iloc[0]
df['AMT71_index'] = 100 * df['USE_AMT71'] / df['USE_AMT71'].iloc[0]
# 그래프의 시작점이 동일하게 맞추는 작업

plt.plot(df['Count_index'], linewidth=1)
plt.plot(df['Search_index'], linewidth=1)
plt.plot(df['Index_index'], linewidth=1)
plt.plot(df['AMT_index'], linewidth=1)
plt.plot(df['AMT21_index'], linewidth=1)
plt.plot(df['AMT22_index'], linewidth=1)
plt.plot(df['AMT70_index'], linewidth=1)
plt.plot(df['AMT71_index'], linewidth=1)
plt.show()
# 그래프로 한 번에 나타내기

plt.plot(df['AMT_index'], linewidth=1)
# 한 개씩 그래프로 확인

ddf = df[['Count','Search','Index','USE_AMT','USE_AMT21','USE_AMT22','USE_AMT70','USE_AMT71']]
# 필요한 열만 가져오기
ddf.corr()
# 상관계수 구하기
