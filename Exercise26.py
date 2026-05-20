import pandas as pd
stock1 =pd.Series([120, 80, None , 60, 95, None , 110])
stock2=pd.Series([120, 80, None , 60, 95, None , 110],index=['Apple','Banana','Orange','Mango','Grape','Peach','Melon'])
stock2.to_csv("0502-1.csv", index=True)

stock3=stock2.to_dict()

#pd.Series({"Apple":120.0,"Banana":80.0,"Orange": None,"Mango":60.0,"Grape":95.0,"Peach":None,"Melon":110.0})

c=stock2.isnull()
d=stock2.isnull().sum()
print(f"stock1:\n{stock1}\n\nstock2:\n{stock2}\n\nstock3\n{stock3}\n\n{stock2.index[1]}庫存：{stock2.iloc[1]}\n\n缺失值檢查：\n{c}\n\n缺失值數量：{d}")
