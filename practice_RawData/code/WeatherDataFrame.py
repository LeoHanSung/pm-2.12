import pandas as pd
import datetime
import os

# ddd = datetime.datetime(2018,4,1,00)

b = pd.read_csv('../rawdata/환경기상데이터/종로구/V10O1611145.csv')

# print(b)
# print(b['tm'])
year = [int(str(i)[:4]) for i in b['tm'].values]
month = [int(str(i)[4:6]) for i in b['tm'].values]
day = [int(str(i)[6:8]) for i in b['tm'].values]
hour = [int(str(i)[8:10]) for i in b['tm'].values]
minute = [int(str(i)[10:12]) for i in b['tm'].values]

cols = [[],[]] #컬럼 이름들 모아놓은 것
colnames = ['pm10', 'pm25']
filenames = []
#파일 이름을 불러온다
for root, dirs, files in os.walk('../rawdata/환경기상데이터/종로구'):
    for file in files:
        filenames.append(file)
        for col in colnames:
            cols[0].append(file[:-4])
            cols[1].append(col)

a = pd.DataFrame(index=b['tm'], columns=cols)

print(filenames)

cnt = 0
for file in filenames:
    inp = pd.read_csv('../rawdata/환경기상데이터/종로구/'+file)
    filename = file[:-4]
    # print(inp.index)
    # print(inp.index[-1]+1)
    for i in range(int(inp.index[-1]+1)):
        tm = inp.iloc[i]['tm']
        a[filename, 'pm10'].loc[tm] = inp.iloc[i]['pm10']
        a[filename, 'pm25'].loc[tm] = inp.iloc[i]['pm25']
        print(i)
    cnt = cnt+1
    print(cnt)
print(a)
    # print(filename)
    # a[filename,'pm10'].ix[] =
    # print(inp)
    # cnt = cnt+1

# print(cnt)
# inp = pd.read_csv('../rawdata/환경기상데이터/종로구/V10O1611145.csv')
# print(inp.ix[0]['pm10'])
# a['V01o1610468', 'pm10'].ix[2018,4,1,0,0] = 1
# a['V01o1610468', 'pm25'].ix[2018,4,1,0,0] = 2
# print(a.loc(1))
# a['year'] = year
# a['month'] = month
# a['day'] = day
# a['hour'] = hour
# a['min'] = minute
# a['serial'] = b['serial']
# a['flag'] = b['flag']
# a['pm10'] = b['pm10']
# a['noise'] = b['noise']
# a['temp'] = b['temp']
# a['humi'] = b['humi']
# a['pm25'] = b['pm25']
# print(a)

# c = pd.DataFrame()
a.to_csv(index=False, path_or_buf='../rawdata/환경기상데이터/과제/종로구.csv')
# b.reindex = [b['tm'][:8], b['tm'][8:]]
# print(b)