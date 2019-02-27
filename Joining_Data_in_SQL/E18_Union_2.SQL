SELECT country_code
FROM cities
UNION 
SELECT code
from currencies
ORDER BY country_code;
