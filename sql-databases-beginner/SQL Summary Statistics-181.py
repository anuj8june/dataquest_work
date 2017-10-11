## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select * from facts"
facts = conn.execute(query).fetchall()
print(facts[0:2])
facts_count = len(facts)

## 2. Counting the Number of Rows in SQL ##

conn = sqlite3.connect("factbook.db")
query = "SELECT COUNT(birth_rate) FROM facts"
birth = conn.execute(query).fetchall()
birth_rate_count = birth[0][0]
print(birth_rate_count)



## 3. Finding a Column's Minimum and Maximum Values in SQL ##

conn = sqlite3.connect("factbook.db")

query = "select min(population_growth) from facts;"
min_population_growth = conn.execute(query).fetchall()[0][0]

query = "select max(death_rate) from facts;"
max_death_rate = conn.execute(query).fetchall()[0][0]

## 4. Calculating Sums and Averages in SQL ##

conn = sqlite3.connect("factbook.db")

query = "select sum(area_land) from facts;"
total_land_area = conn.execute(query).fetchall()[0][0]
print(total_land_area)

query = "select avg(area_water) from facts;"
avg_water_area = conn.execute(query).fetchall()[0][0]
print(avg_water_area)

## 5. Combining Multiple Aggregation Functions ##

conn = sqlite3.connect("factbook.db")
query = "select avg(population),sum(population),max(birth_rate) from facts;"
var = conn.execute(query).fetchall()
mean_pop = var[0][0]
sum_pop = var[0][1]
max_birth_rate = var[0][2]




## 6. Aggregating Values for a Subset of the Data ##

conn = sqlite3.connect("factbook.db")
query = "select avg(population_growth) from facts where population > 10000000;"
population_growth = conn.execute(query).fetchall()[0][0]
print(population_growth)

## 7. Selecting Unique Rows ##

conn = sqlite3.connect("factbook.db")
query = "select distinct birth_rate from facts;"
unique_birth_rates = conn.execute(query).fetchall()
print(unique_birth_rates)

## 8. Aggregating Unique Values ##

conn = sqlite3.connect("factbook.db")

query = "select avg(distinct birth_rate) from facts where population > 20000000;"
average_birth_rate = conn.execute(query).fetchall()[0][0]
print(average_birth_rate)

query = "select sum(population) from facts where area_land > 1000000;"
sum_population = conn.execute(query).fetchall()[0][0]
print(sum_population)

## 9. Performing Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")

query = "select population_growth/1000000 from facts ;"
population_growth_millions = conn.execute(query).fetchall()
print(population_growth_millions)

## 10. Performing Arithmetic Between Columns ##

conn = sqlite3.connect("factbook.db")

query = "select population*(1 + population_growth/100) from facts ;"
next_year_population= conn.execute(query).fetchall()
print(next_year_population)