import glob
import os
import pandas as pd

os.getcwd()

filenames = glob.glob("C:\\Users\\USER\\test\Weather\\*.csv")
aa2 = pd.read_csv(filenames[1])

cc2 = aa2[aa2.pm10==-999]
dd2 = list(cc2.index)
aa2 = aa2.drop(dd2,0)

tt2 = aa2[aa2.pm10>500]
kk2 = list(tt2.index)
aa2 = aa2.drop(kk2,0)

ee2 = list(aa2['tm'])
ee2 = [str(i)[:8] for i in ee2]
aa2['date'] = ee2

aa2 = aa2[['date','serial', 'pm10', 'pm25']]
aa2