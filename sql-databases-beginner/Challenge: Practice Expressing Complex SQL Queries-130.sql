## 2. Use SELECT and LIMIT to Filter Results ##

select College_jobs,Median,Unemployment_rate
from recent_grads
limit 20;

## 3. Use WHERE to Filter Results ##

select Major
from recent_grads
where Major_category = 'Arts'
limit 5;


## 4. Express Criteria With Operators ##

select Major,Total,Median,Unemployment_rate
from recent_grads
where (Major_category != 'Engineering') and (Median <= 50000 or Unemployment_rate > 0.065);

## 5. Order Your Results ##

select Major
from recent_grads
where Major_category != 'Engineering'
order by Major desc
limit 20;