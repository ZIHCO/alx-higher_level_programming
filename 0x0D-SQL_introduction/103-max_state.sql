-- Scrript that displays the max temp of each state ordered by state
-- SELECT does it all
SELECT state AS state,
	MAX(value) as max_temp
	FROM temperatures
	GROUP BY state
	ORDER BY state;
