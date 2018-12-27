select release_year,avg(budget) as avg_budget,avg(gross) as avg_gross
from films
where release_year>1990
group by release_year
having avg(budget) >60e6
order by avg_gross desc
