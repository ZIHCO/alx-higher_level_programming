-- script that computes the score average of all records in table
-- select and aggregate
SELECT SUM(score) / COUNT(id) AS average FROM second_table;
