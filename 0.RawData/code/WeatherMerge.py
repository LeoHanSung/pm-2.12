import glob
import os
import pandas as pd

os.getcwd()

filenames = glob.glob("C:/Users/user/test/Weather/*.csv")

for i in range(len(filenames) - 1):

    if i == 0:
        aa = pd.read_csv(filenames[0])
        aa = aa[['tm', 'serial', 'pm10', 'pm25']]
        bb = pd.read_csv(filenames[1])
        bb = bb[['tm', 'serial', 'pm10', 'pm25']]

        if len(aa) >= len(bb):
            cc = aa
            dd = bb
        else:
            dd = aa
            cc = bb

        results = cc.merge(dd, on='tm', how='outer')
        print('first')

    else:

        aa = pd.read_csv(filenames[i + 1])
        aa = aa[['tm', 'serial', 'pm10', 'pm25']]

        if len(aa) >= len(results):
            cc = aa
            dd = results
        else:
            dd = aa
            cc = results

        results = cc.merge(dd, on='tm', how='outer')
        print(i)

results.to_csv('C:/Users/user/test/Weather/weather_merge.csv', index = False)
pd.read_csv('C:/Users/user/test/Weather/weather_merge.csv')

