-- Lists all shows with their genre ids, NULL when a show has no genre
-- A LEFT JOIN keeps every show, filling missing genre ids with NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
