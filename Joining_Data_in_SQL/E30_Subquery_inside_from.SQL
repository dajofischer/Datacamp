select countries.local_name, subquery.lang_num
from (select code, count(name) as lang_num
from languages
group by code) as subquery, countries
where countries.code = subquery.code
order by lang_num desc;
