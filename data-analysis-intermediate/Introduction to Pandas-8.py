## 3. Read in a CSV file ##

import pandas as pd
food_info = pd.read_csv("food_info.csv")
print(type(food_info))

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty = food_info.head(20)

## 7. Selecting a row ##

hundredth_row = food_info.loc[99]
print(hundredth_row)

## 8. Data types ##

print(food_info.dtypes)

## 9. Selecting multiple rows ##

print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

limit = len(food_info)
last_rows = food_info.loc[(limit-5):limit]

## 10. Selecting individual columns ##

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]
print(saturated_fat)
print(cholesterol)


## 11. Selecting multiple columns by name ##

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
selenium_thiamin = food_info[["Selenium_(mcg)","Thiamin_(mg)"]]

## 12. Practice ##

print(food_info.columns)
print(food_info.head(2))
temp = food_info.columns.tolist()
gram = [val.endswith("(g)") for val in temp]
print(gram)
gram_columns = []
for num,val in enumerate(gram):
    if val == True:
        gram_columns.append(temp[num])
gram_df = food_info[gram_columns]
print(gram_df.head(2))