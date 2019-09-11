import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

os.getcwd()

filenames = glob.glob("C:\\Users\\student\\finance\\weather2\\*.csv")

for i in range(len(filenames)) :
    try :
        aa = pd.read_csv(filenames[i])
        mean_pm = aa.pivot_table('pm10',index = 'date', aggfunc='mean')

        ee = list(mean_pm.index)
        mean_pm['date'] = ee
        mean_pm = mean_pm[['date','pm10']]

        kk1 = list(mean_pm['date'])
        kk2 = list(mean_pm['pm10'])
        
        plt.title(filenames[i][34:-4])
        plt.plot(kk2)
        plt.show(kk2)
        
        print(str(i+1)+'번째 완료')
    except :
        print(str(i+1)+'번째 오류')
