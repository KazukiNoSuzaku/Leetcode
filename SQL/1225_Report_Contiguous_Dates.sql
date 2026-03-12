-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Union failed and succeeded periods, find contiguous date ranges

WITH all_dates AS (
    SELECT fail_date AS dt, 'failed' AS period_state FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT success_date AS dt, 'succeeded' AS period_state FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),
ranked AS (
    SELECT dt, period_state,
           ROW_NUMBER() OVER (ORDER BY dt) - ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY dt) AS grp
    FROM all_dates
)
SELECT period_state, MIN(dt) AS start_date, MAX(dt) AS end_date
FROM ranked
GROUP BY period_state, grp
ORDER BY start_date;
