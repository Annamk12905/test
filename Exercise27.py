import pandas as pd
data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}
df = pd.DataFrame(data_dict, columns=["Product", "Price", "Sales"])

print(df.head())
print(df.tail())
print(df.shape) #列與欄
print(df.columns) #欄位名稱
print(df.dtypes)
print(df.count())
a=df.describe().round(2)
print(a)
a.to_csv("0520_stock2.csv")

