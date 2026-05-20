import pandas as pd
#mac dinh se la
#0 10
#1 20
#3 30
#s=pd.Series([10,20,30],index=['a','b','c'])
#ket qua
#a   10
#b   20
#c    30
s=pd.Series({"A":10,"B":20,"C":30,"D":40})
#ket qua
#A    10
#B    20
#C    30
#D    40
#dtype: int64
#print(s)
print(s[0:2]) # in tu vi tri 0,vi tri 2 khong lay

#isnull=s.isnull()# kiem tra xem du lieu co trong hay khong,tra ve Truse/False
s=pd.read_csv('data.csv')
c=s.isnull().sum()
c.to_csv("0502-1.csv")
#print(s.isnull().sum())
