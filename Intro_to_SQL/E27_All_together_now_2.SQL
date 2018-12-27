-- select country, average budget, average gross
select country, avg(budget) as avg_budget, avg(gross) as avg_gross
-- from the films table
from films
-- group by country
group by country
-- where the country has more than 10 titles
having count(*)>10
-- order by country
order by country
-- limit to only show 5 results
limit 5
