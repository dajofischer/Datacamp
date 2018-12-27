select imdb_score, count(*)
from reviews
group by imdb_score
