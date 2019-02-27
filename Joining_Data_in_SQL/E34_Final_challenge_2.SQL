-- choose fields
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
-- left table
FROM countries AS c
-- right table
INNER JOIN populations AS p
-- join conditions
ON c.code = p.country_code
-- specific records matching a condition
WHERE year = 2015
-- aggregated for each what?
GROUP BY region, continent
-- how should we sort?
ORDER BY avg_fert_rate;
