SELECT c.name AS country, region, p.life_expectancy AS life_exp
FROM countries AS c
LEFT JOIN populations as p
ON c.code = p.country_code
WHERE p.year = 2010
ORDER BY life_exp asc
LIMIT 5;
