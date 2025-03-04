-- dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)
SELECT genres.name AS genre, COUNT(*) AS number_of_shows 
FROM genres 
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id 
GROUP BY genres.name 
HAVING number_of_shows > 0 
ORDER BY number_of_shows DESC;