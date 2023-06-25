-- A script that uses hbtn_0d_tvshows DB to list all genres not linked to
-- the show Dexter

SELECT tv_genres.name FROM tv_genres
	WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_shows LEFT
		OUTER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
		LEFT OUTER JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
		WHERE tv_shows.title = 'Dexter') ORDER BY tv_genres.name;
