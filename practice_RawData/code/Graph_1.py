import glob
import os
import pandas as pd

os.getcwd()

filenames = glob.glob("C:\\Users\\USER\\test\\re_weather2\\*.csv")

aa = pd.read_csv(filenames[3])

mean_pm = aa.pivot_table('pm10',index = 'date', aggfunc='mean')
mean_pm

ee = list(mean_pm.index)
mean_pm['date'] = ee
mean_pm = mean_pm[['date','pm10']]

kk1 = list(mean_pm['date'])
kk2 = list(mean_pm['pm10'])

plt.plot(kk2)
plt.show()

mean_pm2 = aa.pivot_table(values=['pm10','pm25'],index = 'date', aggfunc='mean')
mean_pm2

import numpy as np
mean_pm3 = aa.pivot_table(values=['pm10','pm25'],index = 'date', aggfunc=[np.mean, np.min, np.max, np.std])
mean_pm3

