select name, continent, inflation_rate
from countries
inner join economies
on countries.code = economies.code
where year = 2015 AND  inflation_rate in
(select max(inflation_rate) as max_inf
from (select name, continent, inflation_rate
from countries
inner join economies
on countries.code = economies.code
where year = 2015) as subquery
group by continent)
