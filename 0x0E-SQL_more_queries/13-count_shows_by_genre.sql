-- list all shows contained in the hbtn_0d_tvshows database
SELECT tv_shows.genres.genres_id As genre, 
    COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_shows_genres
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
