-- Script that displays the average temperature(FAH) by city ordered by temp (desc)
-- SELECT
SELECT city AS city,
	SUM(value) / COUNT(city) AS "avg_temp"
	FROM temperatures
	GROUP BY city ORDER BY avg_temp DESC;
