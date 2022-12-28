-- import the DB hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows

SELECT  tv_shows.title, tv_show_genres.genre_id FROM tv_genres JOIN tv_show_genres, tv_shows WHERE genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
