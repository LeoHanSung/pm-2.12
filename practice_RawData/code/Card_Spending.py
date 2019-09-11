import os
import pandas as pd
import xlrd

os.getcwd()

path ="C:\\Users\\student\\Desktop\\bigcontest\\carddata"
os.chdir(path)

os.getcwd()



transaction = pd.read_csv('CARD_SPENDING.txt', sep="\t", header=None)

transaction