## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == '1984'

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria" )
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

rep = world_alcohol[:,0] == "1986"
world_alcohol[rep,0] = "2014"

repe = world_alcohol[:,3] == "Wine"
world_alcohol[repe,3] = "Grog"



## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = 0

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol =  alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada")
canada_1986 = world_alcohol[is_canada_1986,:] 
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
year = "1989"
for val in countries:
    if val not in totals:
        ext = (world_alcohol[:,0] == "1989") & (world_alcohol[:,2] == val)
        country_consumption = world_alcohol[ext,4]
        emp = country_consumption == ''
        country_consumption[emp] = "0"
        count = country_consumption.astype(float)
        totals[val] = count.sum()

print(totals)
        
    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for tot in totals:
    if totals[tot] > highest_value:
        highest_value = totals[tot]
        highest_key = tot