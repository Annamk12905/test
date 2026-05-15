import csv
import unittest

import numpy as np
products_name=[]
stock_quantity=[]
unit_price=[]
sales_volume=[]

with open("grocery_inventory_and_sales_dataset.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader: #doc du lieu
            products_name.append(row["Product_Name"])
            stock_quantity.append(float(row["Stock_Quantity"]))
            unit_price.append(float(row["Unit_Price"].replace("$","")))
            sales_volume.append(float(row["Sales_Volume"]))


products_name=np.array(products_name)
stock_quantity=np.array(stock_quantity)
unit_price=np.array(unit_price)
sales_volume=np.array(sales_volume)


inventory_value=stock_quantity*unit_price #gia tri ton kho=hang ton kho*don gia

#for i in range(len(products_name)):
  # print(products_name[i],":",inventory_value[i])


max_value=np.max(sales_volume)       #ban chay nhat argmax chi tra ve mot gia tri duy nhat
max_indices = np.where(sales_volume == max_value)[0]

#print("\n====BEST-SELLING PRODUCT=====")
#print("PRODUCTS NAME: ",products_name[max_index])
#print("BEST SALES: ",sales_volume[max_index])

revenue=sales_volume*unit_price*0.9  #doanh thu khi giam 10%= so ban ra*don gia*0.9

#for i in range(len(products_name)):
   #print(products_name[i],":",revenue[i])


#total_price=np.sum(revenue)  #
#print("TOTAL PRICE",total_price)

with open("results.csv","w",encoding="utf-8",newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["Product_Name", "Inventory_Value", "Revenue","Best_Seller"])
    for i in range(len(products_name)):
        writer.writerow([products_name[i],
                        round( inventory_value[i],2),
                        round(revenue[i],2),
                         i in max_indices])