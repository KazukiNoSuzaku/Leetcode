-- Author: Kaustav Ghosh
-- Problem: Average Time of Process per Machine
-- Approach: The problem defines the answer as the total of the per-process durations divided by the number of processes, so the query pairs each start row with its own end row through a self-join on the machine and process, and averages those differences directly. It is tempting to collapse this into the average of the end timestamps minus the average of the start timestamps, which is mathematically identical because every process contributes exactly one of each, but it reassociates floating-point arithmetic and can therefore round to a different third decimal when the true average sits exactly on a half-way boundary. Averaging the differences keeps each subtraction on its own pair, which is both the stated definition and the stabler computation.

SELECT a.machine_id,
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b
  ON b.machine_id = a.machine_id
 AND b.process_id = a.process_id
WHERE a.activity_type = 'start'
  AND b.activity_type = 'end'
GROUP BY a.machine_id;
