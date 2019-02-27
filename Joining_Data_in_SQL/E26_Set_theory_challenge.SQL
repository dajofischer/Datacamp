-- select the city name
select name
-- alias the table where city name resides
from cities AS c1
-- choose only records matching the result of multiple set theory clauses
WHERE country_code IN
(
    -- select appropriate field from economies AS e
    SELECT e.code
    FROM economies AS e
    -- get all additional (unique) values of the field from currencies AS c2
    UNION
    SELECT c.code
    FROM currencies AS c
    -- exclude those appearing in populations AS p
    EXCEPT
    SELECT p.country_code
    FROM populations AS p
);
