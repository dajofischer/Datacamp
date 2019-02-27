SELECT country_code as code, year
FROM populations
INTERSECT
SELECT code, year
FROM economies
ORDER BY code, year asc;
