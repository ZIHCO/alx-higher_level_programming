-- import the DB hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows

SELECT tv_genres.name AS 'genre',
	COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
	FROM tv_show_genres
	JOIN tv_genres
	WHERE tv_show_genres.genre_id = tv_genres.id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
