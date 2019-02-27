SELECT DISTINCT c.name, e.total_investment, e.imports
FROM countries AS c
LEFT JOIN economies AS e
ON (c.code = e.code
  AND c.code IN (
    SELECT l.code
    FROM languages AS l
    WHERE official = 'true'
  ) )
WHERE year = 2015 AND region = 'Central America'
ORDER BY name;
