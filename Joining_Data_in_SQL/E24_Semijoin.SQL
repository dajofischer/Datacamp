/*select code
from countries
where region ='Middle East'*/

select distinct name
from languages
where code in (select code
from countries
where region ='Middle East')
order by name
