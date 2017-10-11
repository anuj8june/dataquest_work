## 2. Introduction ##

select * from recent_grads limit 5;

## 4. Calculating Group-Level Summary Statistics ##

SELECT Major_category, AVG(ShareWomen) FROM recent_grads GROUP BY Major_category;

## 5. Renaming Columns With the AS Statement ##

select SUM(Men) as total_men,SUM(Women) as total_women from recent_grads;

## 6. Practice: Using GROUP BY ##

select Major_category,AVG(Employed)/AVG(Total) as share_employed from recent_grads group by Major_category;

## 7. Querying Virtual Columns With the HAVING Statement ##

select Major_category, AVG(Low_wage_jobs)/AVG(Total) as share_low_wage
from recent_grads
group by Major_category 
having share_low_wage > 0.1;


## 8. Rounding Results With the ROUND Function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 9. Nesting functions ##

select Major_category, round(AVG(College_jobs) / AVG(Total),3) as share_degree_jobs
from recent_grads
group by Major_category
having share_degree_jobs < 0.3;