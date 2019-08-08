import os
import pandas as pd
import xlrd

os.getcwd()

path ="C:\\Users\\USER\\Downloads\\Card\\CARD_SPENDING"
os.chdir(path)

os.getcwd()

transaction = pd.read_csv('CARD_SPENDING.txt', sep="\t", header=None)
# 텍스트 파일 가져오기


aa = pd.DataFrame()
aa['STD_DD'] = transaction[0]
aa['GU_CD'] = transaction[1]
aa['DONG_CD'] = transaction[2]
aa['MCT_CAT_CD'] = transaction[3]
aa['SEX_CD'] = transaction[4]
aa['AGE_CD'] = transaction[5]
aa['USE_CNT'] = transaction[6]
aa['USE_AMT'] = transaction[7]

# 바로 저장하면 엑셀 행 제한 떄문에 데이터 손실, 새로운 데이터프레임에 옮기기

aa = aa.drop(0)
# 인덱스 0에 해당하는 행 제거

aa = aa.reset_index(drop=True)
# 인덱스 재설정

vv = list(aa['MCT_CAT_CD'])
# 업종코드 데이터 리스트

set(vv)
# 중복값 체크

vv2 = [int(v) for v in vv]
# 문자, 숫자로 데이터 형식이 통일되지 않음, 숫자로 통일

aa['MCT_CAT_CD'] = vv2
# 데이터프레임에 바꾼 값 설정 (분류 위해서 해주는 작업)

aa = aa[aa.MCT_CAT_CD==21]
# 업종코드 21인 데이터만 출력

bb = aa[['STD_DD','USE_AMT']]
# 데이터프레임에서 특정 열만 가져오기

jj = list(bb['STD_DD'])
jj3 = [str(j) for j in jj]
# 날짜데이터 string 형식으로 통일
bb['STD_DD'] = jj3
# 데이터프레임에 바꾼 값 설정

cc = list(bb["USE_AMT"])
cc2 = [int(c) for c in cc]
bb["USE_AMT"]=cc2
# 평균 구하기 위해 이용금액 숫자 형식으로 변경

import numpy as np
tt = pd.pivot_table(bb, index =['STD_DD'], values=['USE_AMT'], aggfunc=[np.mean])
# 날짜별 이용금액 평균 구하기

ttt = list(tt.index)
# 현재 날짜가 인덱스이므로, 리스트에 담아서 새로운 행으로 추가
tt['DATE'] = ttt
tt.to_csv('cardamount_21.csv',index=False)
# 저장하면 인덱스 없어지므로 날짜데이터 보존 위해 위와 같은 작업

tt2 = pd.read_csv('cardamount_21.csv') 

tt2 = tt2.drop(0)
tt2 = tt2.reset_index(drop=True)
tt2 = tt2.rename(columns = {'mean': 'USE_AMT21'})
# 컬럼명 변경

tt3 = list(tt2['USE_AMT21'])
tt4 = [round(float(t),2) for t in tt3]
# 소수점 2자리까지 제한
tt2['USE_AMT21'] = tt4

tt2 = tt2[['DATE', 'USE_AMT21']]
vv = list(tt2['DATE'])
vv2 = [str(v)[:8] for v in vv]
# 날짜데이터 형식 변경

tt2['DATE'] = vv2

tt2.to_csv('cardamount21_2.csv', index=False)
# 업종코드 21번의 날짜별 이용금액 평균 최종적으로 구함, 파일로 저장


