import glob
import os
import pandas as pd

os.getcwd()

filenames = glob.glob('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\*.csv')

for i in range(len(filenames) - 1):

    if i == 0:
        aa = pd.read_csv(filenames[0])
        bb = pd.read_csv(filenames[1])

        if len(aa) >= len(bb):
            cc = aa
            dd = bb
        else:
            dd = aa
            cc = bb

        results = cc.merge(dd, on='DATE', how='outer')
        print('first')

    else:

        aa = pd.read_csv(filenames[i + 1])
        
        if len(aa) >= len(results):
            cc = aa
            dd = results
        else:
            dd = aa
            cc = results

        results = cc.merge(dd, on='DATE', how='outer')
        print(str(i+1))

results.to_csv('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\COUNT_T_MERGE.csv', index = False)


zz = pd.read_csv('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\COUNT_T_MERGE.csv')

zz = zz.fillna(0)

zz['COUNT_T'] = zz['COUNT_x']+zz['COUNT_y']+zz['COUNT_x.1']+zz['COUNT_y.1']+zz['COUNT_x.2']+zz['COUNT_y.2']+zz['COUNT_x.3']+zz['COUNT_y.3']

zz = zz.sort_values(by='DATE')

zz.to_csv('C:\\Users\\USER\\Downloads\\SNS\\COUNT_T\\COUNT_T_MERGE2.csv',index=False)

import matplotlib.pyplot as plt
plt.plot(list(zz['COUNT_T']))
plt.show()