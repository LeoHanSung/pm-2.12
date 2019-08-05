import pymysql
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine
#위에 있는 것은 다 pip install 해야한다.
#pip install pymysql
#pip install sqlalchemy
#pymysql.install_as_MySQLdb()

connector = pymysql.connect(host='15.164.100.89', port=3306,
                           user='bigCon',passwd='12345678',
                           db='bigCon',
                           cursorclass=pymysql.cursors.DictCursor)

cursor = connector.cursor()
cursor.execute('sql구문')

# Selectd 명령문시, 데이터 가지고 오는 방법
item_one = cursor.fetchone() #한개만 
item_many = cursor.fetchmany(n) #n개
item_table = cursor.fetchall() # 전체

#pandas로 변환
tiem_table_df = pd.DataFrame(item_table)

#dataframe을 sql로 저장 프로세스
#create_engine("mysql+mysqldb://(username):(passwd)@(server주소)/(db명),encoding=)
engine = create_engine("mysql+mysqldb://bigCon:"+"12345678"+"@15.164.100.89/테이블명", encoding='utf-8')
#혹은

conn = engine.connect()
#dataframe을 sql에 저장
item_table_df.to_sql(name='item_table_df', con=engine)
conn.close()