import os
#파일 이름 다 불러왔다.

cols = [[],[]]

colnames = ['pm10', 'pm25']

for root, dirs, files in os.walk('../rawdata/환경기상데이터/종로구'):
    for file in files:
        for col in colnames:
            cols[0].append(file[:-4])
            cols[1].append(col)

print(cols)

