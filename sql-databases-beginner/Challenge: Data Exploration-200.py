## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select avg(population) , avg(population_growth) , avg(birth_rate) , avg(death_rate) from facts;"
data = conn.execute(query).fetchall()
pop_avg = data[0][0]
pop_growth_avg = data[0][1]
birth_rate_avg = data[0][2]
death_rate_avg = data[0][3]

## 2. Find Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select min(population),max(population), min(population_growth),max(population_growth), min(birth_rate),max(birth_rate),  min(death_rate), max(death_rate) from facts;"
avg_results = conn.execute(averages).fetchall()

pop_min = avg_results[0][0]
pop_max = avg_results[0][1]
pop_growth_min = avg_results[0][2]
pop_growth_max = avg_results[0][3]
birth_rate_min = avg_results[0][4]
birth_rate_max = avg_results[0][5]
death_rate_min = avg_results[0][6]
death_rate_max = avg_results[0][7]

## 3. Filter Values ##

conn = sqlite3.connect("factbook.db")

averages = "select min(population),max(population), min(population_growth),max(population_growth), min(birth_rate),max(birth_rate),  min(death_rate), max(death_rate) from facts where population < 2000000000 and population > 0;"
avg_results = conn.execute(averages).fetchall()

pop_min = avg_results[0][0]
pop_max = avg_results[0][1]
pop_growth_min = avg_results[0][2]
pop_growth_max = avg_results[0][3]
birth_rate_min = avg_results[0][4]
birth_rate_max = avg_results[0][5]

## 4. Predict Future Population Growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select round(population * ( 1 + population_growth / 100),0) from facts where population is not NULL and population_growth is not NULL and population < 7000000000 and population > 0;"
projected_population = conn.execute(query).fetchall()


## 5. Explore Projected Population ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query = "select min(round(population * ( 1 + population_growth / 100),0)),max(round(population * ( 1 + population_growth / 100),0)),avg(round(population * ( 1 + population_growth / 100),0)) from facts where population is not NULL and population_growth is not NULL and population < 7000000000 and population > 0;"
projected_population = conn.execute(query).fetchall()
pop_proj_min = projected_population[0][0]
pop_proj_max = projected_population[0][1]
pop_proj_avg = projected_population[0][2]
