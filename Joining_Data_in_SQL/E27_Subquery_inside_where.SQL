select *
from populations
where life_expectancy > 1.15 * (select avg(life_expectancy)
from populations
where year = 2015)
and year =2015
