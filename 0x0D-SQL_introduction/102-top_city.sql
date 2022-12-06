-- script that displays the top 3 cities temp during July and August
-- SELECT does it
SELECT city AS city,
	SUM(value) / COUNT(city) AS "avg_temp"
	FROM temperatures
	WHERE month = 7 or month = 8
	GROUP BY city ORDER BY avg_temp DESC
	LIMIT 3;
