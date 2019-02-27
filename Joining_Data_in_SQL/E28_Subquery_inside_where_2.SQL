-- select the appropriate fields
select name, country_code, urbanarea_pop
-- from the cities table
from cities
-- with city name in the field of capital cities
where name IN
  (select capital
   from countries)
ORDER BY urbanarea_pop DESC;
