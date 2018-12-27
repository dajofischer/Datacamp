select country,release_year,min(gross)
from films
group by release_year, country
order by country,release_year
