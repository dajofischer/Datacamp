select count(deathdate)*100.0/count(*) as percentage_dead from people
select max(release_year)-min(release_year) as difference from films


select (max(release_year)-min(release_year))/10
as number_of_decades
from films
