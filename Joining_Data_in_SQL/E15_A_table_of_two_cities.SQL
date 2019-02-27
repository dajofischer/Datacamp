SELECT c.name AS city, l.name AS language
FROM cities AS c
CROSS JOIN languages AS l
WHERE c.name LIKE 'Hyder%';


SELECT c.name AS city, l.name AS language
FROM cities AS c
INNER JOIN languages AS l
ON c.country_code = l.code
WHERE c.name LIKE 'Hyder%';
