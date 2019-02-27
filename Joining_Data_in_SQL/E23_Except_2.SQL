select capital
from countries
except
select name
from cities
order by capital
