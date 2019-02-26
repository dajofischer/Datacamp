SELECT countries.name, code, languages.name AS language
FROM languages
FULL JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;
