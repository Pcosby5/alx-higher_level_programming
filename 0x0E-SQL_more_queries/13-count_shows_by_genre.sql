-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.

SELECT genres.name AS genre, COUNT(show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;

