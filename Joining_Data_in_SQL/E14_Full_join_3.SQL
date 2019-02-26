SELECT c.name AS country, region, l.name AS language,
       basic_unit, frac_unit
FROM countries AS c
FULL JOIN languages AS l
USING (code)
FULL JOIN currencies AS cu
USING (code)
WHERE region LIKE 'M%esia';
