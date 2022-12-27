-- Lists all the cities of California on the DB - hbtn_0d_usa
-- WHERE is in use

SELECT id, name FROM cities
	WHERE state_id =
	(SELECT id FROM states
		WHERE name = 'California');
