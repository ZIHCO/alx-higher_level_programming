-- script that lists the number of records with the same score
-- select fixes this
SELECT score AS score,
	COUNT(id) AS "number"
	FROM second_table
	GROUP BY  score ORDER BY 'number' DESC;
