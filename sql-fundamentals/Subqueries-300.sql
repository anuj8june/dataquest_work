## 2. Subqueries ##

select Major , Unemployment_rate from recent_grads where Unemployment_rate < (select AVG(Unemployment_rate) from recent_grads) order by Unemployment_rate ;

## 3. Subquery In SELECT ##

SELECT cast(COUNT(*) as float)/ cast((SELECT COUNT(*) FROM recent_grads) as float)  as proportion_abv_avg FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads);

## 4. Returning Multiple Results In Subqueries ##

select Major , Major_category from recent_grads where Major_category in (SELECT Major_category FROM recent_grads
GROUP BY Major_category
ORDER BY SUM(Total)
LIMIT 5);

## 5. Building Complex Subqueries ##

select AVG(cast(Sample_size as float)/cast(Total as float)) avg_ratio from recent_grads;

## 6. Practice Integrating A Subquery With The Outer Query ##

select Major, Major_category, cast(Sample_size as float)/cast(Total as float) ratio from recent_grads where ratio > (select AVG(cast(Sample_size as float)/cast(Total as float)) avg_ratio from recent_grads);