-- Lists all cities contained in the DB hbtn_0d_usa
-- cities.id cities.name states.name

SELECT cities.id, cities.name, states.name FROM cities
	JOIN states WHERE states.id = state_id;
