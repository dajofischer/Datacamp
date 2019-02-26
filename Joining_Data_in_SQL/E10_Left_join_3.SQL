-- Select region, average gdp_percapita (alias avg_gdp)
SELECT region,  avg(gdp_percapita) as avg_gdp
-- From countries (alias c) on the left
FROM countries AS c
-- left join with economies (alias e)
LEFT JOIN economies AS e
-- match on code fields
ON c.code = e.code
-- focus on 2010 entries
WHERE year = 2010
-- Group by region
GROUP BY region
-- Order by avg_gdp, descending
ORDER BY avg_gdp desc;
