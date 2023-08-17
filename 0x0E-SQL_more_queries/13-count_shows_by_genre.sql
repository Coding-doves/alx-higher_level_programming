-- list all shows contained in the hbtn_0d_tvshows database
SELECT tv_genres.name As genre, 
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name, tv_genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
