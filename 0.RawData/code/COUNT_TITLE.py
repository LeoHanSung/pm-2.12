import glob
import os
import pandas as pd
from konlpy.tag import Okt
okt = Okt()

os.getcwd()

filenames = glob.glob('C:\\Users\\USER\\Downloads\\SNS\\*.xlsx')

for i in range(len(filenames)):
    aa = pd.read_excel(filenames[i])
    aa = aa[aa.SECTION == '뉴스']
    
    
    dd = []
    for j in range(len(aa)) :
        dd.append(okt.morphs(aa['TITLE'].iloc[j]))
    aa['MORPH_T1'] = dd
    
    
    aa2 = aa['MORPH_T1']
    aa3 = [','.join(j) for j in aa2]
    aa['MORPH_T'] = aa3
    
    
    bb = list(aa['DATE'])
    bb= [str(bb[j])[:8] for j in range(len(bb))]
    aa['DATE'] = bb
    
    
    cc = []
    for j in range(len(aa)) :
        kk = aa['MORPH_T1'].iloc[j]
        if '미세먼지' in kk :
            cc.append('1')
        else :
            cc.append('0')
    aa['COUNT'] = cc
    
    
    lis = aa[['DATE','COUNT']]
    co = [int(lis['COUNT'].iloc[j]) for j in range(len(lis))]
    lis['COUNT']=co
    
    
    groups = lis.groupby(lis.DATE)
    gr = groups.sum()
    grl = list(gr.index)
    gr['DATE'] = grl
    
    gr = gr[['DATE', 'COUNT']]
    gr.to_csv('countsnstitle'+str(i+1)+'.csv',index=False)
    
    print(str(i+1)+'번째 파일 완료')
