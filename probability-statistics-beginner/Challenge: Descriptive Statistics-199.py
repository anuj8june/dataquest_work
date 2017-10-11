## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig , ax = plt.subplots(nrows=4,ncols=1,figsize=(5,12))

ax1 = plt.subplot(4,1,1)

ax1.set_xlim([0, 5])


ax2 = plt.subplot(4,1,2)

ax2.set_xlim([0, 5])


ax3 = plt.subplot(4,1,3)

ax3.set_xlim([0, 5])


ax4 = plt.subplot(4,1,4)

ax4.set_xlim([0, 5])

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)


plt.show()

## 2. Mean ##

def calc_mean(series):
    return series.mean()

array = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']

user_reviews = movie_reviews[array]

rt_mean,mc_mean,fg_mean,id_mean = user_reviews.apply(calc_mean)

print(rt_mean,mc_mean,fg_mean,id_mean )




## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    return sum(j**2 for j in [i - calc_mean(series) for i in series])/len(series)
 
rt_var = calc_variance(movie_reviews["RT_user_norm"])
mc_var = calc_variance(movie_reviews["Metacritic_user_nom"])
fg_var = calc_variance(movie_reviews["Fandango_Ratingvalue"])
id_var = calc_variance(movie_reviews["IMDB_norm"])

rt_stdev = rt_var ** 0.5
mc_stdev = mc_var ** 0.5
fg_stdev = fg_var ** 0.5
id_stdev = id_var ** 0.5

## 4. Scatter plots ##

import matplotlib.pyplot as plt
fig,ax = plt.subplots(nrows = 3, ncols =1,figsize = (4,8))

ax1 = plt.subplot(3,1,1)
ax1.scatter(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
ax1.set_xlim(0,5)

ax2 = plt.subplot(3,1,2)
ax2.scatter(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
ax2.set_xlim(0,5)

ax3 = plt.subplot(3,1,3)
ax3.scatter(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])
ax3.set_xlim(0,5)

plt.show()



## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def cal_covariance(xseries,yseries):
    xmean = sum(xseries)/len(xseries)
    ymean = sum(yseries)/len(yseries)
    xlist = [val - xmean for val in xseries]
    ylist = [val - ymean for val in yseries]
    prod = 0
    for i,val in enumerate(xlist):
        prod = prod + val * ylist[i]
     
    return prod/len(xlist)
    
rt_fg_covar = cal_covariance(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = cal_covariance(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = cal_covariance(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])


## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
def calc_correlation(series_one, series_two):
    numerator = calc_covariance(series_one, series_two)
    series_one_std = calc_variance(series_one) ** (1/2)
    series_two_std = calc_variance(series_two) ** (1/2)
    denominator = series_one_std * series_two_std
    correlation = numerator / denominator
    return correlation

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)