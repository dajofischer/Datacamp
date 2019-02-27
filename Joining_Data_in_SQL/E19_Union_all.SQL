SELECT country_code as code, year
FROM populations
UNION ALL
SELECT code, year
FROM economies
ORDER BY code, year;
