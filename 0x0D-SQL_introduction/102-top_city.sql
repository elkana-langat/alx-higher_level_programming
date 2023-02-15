-- displays the top 2 of cities temperatures during july and,
-- august ordered by temperature(descending)
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
