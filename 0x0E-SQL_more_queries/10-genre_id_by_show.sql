-- list all shows contained in the hbtn_0d_tvshows database
SELECT CONCAT(tv_shows.title, '-', tv_show_genres.genre_id) AS record
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER  BY tv_shows.title  ASC, tv_show_genres.genre_id ASC;
