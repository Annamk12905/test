import pandas as pd

df = pd.DataFrame({

    "name": ["Amy", "Bob", "Cathy", "David", "Evan", "Fiona"],

    "age": [20, 21, 19, 22, 20, 23],

    "score": [88, 92, 79, 85, 90, 95]

})

print(df.info())

7. iloc 是 pandas 用來「依照位置（索引編號）取資料」的方法。
import pandas as pd

df = pd.DataFrame({

    "name": ["Amy", "Bob", "Cathy", "David", "Evan", "Fiona"],

    "age": [20, 21, 19, 22, 20, 23],

    "score": [88, 92, 79, 85, 90, 95]

})

print(df.iloc[0])  #第0列

print(df.iloc[0:2]) #前2列

print(df.loc[0])  #loc 是標籤（index名稱）



8. 篩選資料

import pandas as pd

df = pd.DataFrame({

    "name": ["Amy", "Bob", "Cathy", "David", "Evan", "Fiona"],

    "age": [20, 21, 19, 22, 20, 23],

    "score": [88, 92, 79, 85, 90, 95]

})

print(df[(df["score"] >= 80) & (df["age"] < 25)])



9.drop() 刪除資料 ，inplace 是否直接修改原資料（inplace=False預設）

寫法	意思
inplace=True	直接修改原本（不回傳新物件）
inplace=False	不修改原本，而是回傳新結果
import pandas as pd

df = pd.DataFrame({

    "name": ["A", "B"],

    "score": [80, 60]

})

print(df.drop("name", axis=1, inplace=False))


10.groupby依照某個欄位將資料分組，然後對每個分組做統計或計算
import pandas as pd

df = pd.DataFrame({

    "name": ["A", "B", "C", "D", "E"],

    "class": ["A01", "B01", "B01", "A01", "A01"],

    "score": [80, 60, 70, 90, 50]

})

print(df.groupby("class")["score"].mean())

print(df.groupby("class")["score"].sum())

#依照class進行分組，選score欄位進行計算


11.多欄位統計

import pandas as pd

df = pd.DataFrame({

    "name": ["A", "B", "C", "D", "E"],

    "class": ["A01", "B01", "B01", "A01", "A01"],

    "score": [80, 60, 70, 90, 50]

})

print(df.groupby(["class","score"])["score"].mean())