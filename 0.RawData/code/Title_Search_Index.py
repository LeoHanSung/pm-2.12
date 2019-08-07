import glob
import os
import pandas as pd

zz = pd.read_csv('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\COUNT_T_MERGE2.csv')

import matplotlib.pyplot as plt
plt.plot(list(zz['COUNT_T']))
plt.show()

kk = pd.read_csv('C:\\Users\\USER\\Downloads\\SNS\\datalab.csv')

tt = list(kk['Date'])
tt = [t[:4]+t[5:7]+t[8:10] for t in tt]
kk['Date'] = tt

ddd = ['20180415','20180529','20180601','20190109','20190123','20190124','20190207','20190208','20190216','20190222','20190223','20190308','20190309','20190310','20190318','20190325']
len(ddd)

aa1 = list(kk.index)
aa2 = list(kk['Date'])

dic = dict(zip(aa1,aa2))

nulldate = []
for ind, dat in dic.items(): #mydict에 아이템을 하나씩 접근해서, key, value를 각각 name, age에 저장
    if dat in ddd:
        print(ind)
        nulldate.append(ind)
        
for n in nulldate :
    kk = kk.drop(n)
    
kk.dropna()
kk = kk.reset_index(drop=True)

ee = pd.read_excel('pm10_all4.xlsx')
for n in nulldate :
    ee = ee.drop(n)
ee = ee.reset_index(drop=True)

ee2 = pd.read_excel('pm10_all5.xlsx')
for n in nulldate :
    ee2 = ee2.drop(n)
ee2 = ee2.reset_index(drop=True)

df = pd.DataFrame()
df['Count'] = zz['COUNT_T']
df['Search'] = kk['Dust']
df['Index'] = ee['Index']
df['Mean'] = ee2['Mean']

df['Count_index'] = 100 * df['Count'] / df['Count'].iloc[0]
df['Search_index'] = 100 * df['Search'] / df['Search'].iloc[0]
df['Index_index'] = 100 * df['Index'] / df['Index'].iloc[0]
df['Mean_index'] = 100 * df['Mean'] / df['Mean'].iloc[0]

df.to_csv('compare.csv', index=False)
plt.plot(df['Index_index'], linewidth=1)
plt.plot(df['Mean_index'], linewidth=1)
plt.show()

plt.plot(df['Count_index'], linewidth=1)
plt.plot(df['Search_index'], linewidth=1)
plt.plot(df['Index_index'], linewidth=1)
plt.plot(df['Mean_index'], linewidth=1)
plt.show()

ddf = df[['Count','Search','Index','Mean']]
ddf.corr()

