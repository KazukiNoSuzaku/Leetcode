-- Report for each player the device id and date when they first logged in, along with the
-- number of games played so far up to and including that date.
-- Author: Kaustav Ghosh

SELECT player_id, event_date,
       SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity;
