## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees["Year"],women_degrees["Biology"])
plt.show()

## 4. Visualizing The Gender Gap ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees["Year"],women_degrees["Biology"],c='blue',label='Women')
women_degrees["Men_biology"] = 100 - women_degrees["Biology"] 
plt.plot(women_degrees["Year"],women_degrees["Men_biology"],c='green',label='Men')
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = "upper right")
plt.show()

## 6. Hiding Tick Marks ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
fig,ax = plt.subplots()
ax.plot(women_degrees["Year"],women_degrees["Biology"],c='blue',label='Women')
women_degrees["Men_biology"] = 100 - women_degrees["Biology"] 
ax.plot(women_degrees["Year"],women_degrees["Men_biology"],c='green',label='Men')
ax.set_title("Percentage of Biology Degrees Awarded By Gender")
ax.legend(loc = "upper right")
ax.tick_params(bottom="off",top="off",left="off",right="off")
plt.show()

## 7. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

## 8. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))
title = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_title(title[sp])
    # Add your code here.
    
ax.set_xlim(1968,2011)
ax.set_ylim(0,100)

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()