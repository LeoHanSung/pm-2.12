import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

os.getcwd()

filenames = glob.glob("C:\\Users\\USER\\test\\Weather2\\*.csv")

for i in range(len(filenames)) : 
    aa = pd.read_csv(filenames[i])
    cc = aa[aa.pm10==-999]
    dd = list(cc.index)
    aa = aa.drop(dd,0)
    tt = aa[aa.pm10>500]
    kk = list(tt.index)
    aa = aa.drop(kk,0)
    ee = list(aa['tm'])
    ee = [str(i)[:10] for i in ee]
    aa['date'] = ee
    aa = aa[['date','serial', 'pm10', 'pm25']]
    aa.to_csv('C:/Users/USER/test/re_weather2/'+str(i+1)+filenames[i], index=False)
    print(str(i+1)+'번째 완료')