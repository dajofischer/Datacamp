SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
INNER JOIN economies as e
ON c.code = e.code;
