SELECT name
FROM cities
EXCEPT
SELECT capital
FROM countries
ORDER BY name;
