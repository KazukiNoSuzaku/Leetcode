-- Compare each department's monthly average salary with the company average for that month.
-- Author: Kaustav Ghosh

SELECT d.pay_month, d.department_id,
    CASE WHEN d.dept_avg > c.company_avg THEN 'higher'
         WHEN d.dept_avg < c.company_avg THEN 'lower'
         ELSE 'same' END AS comparison
FROM (
    SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, department_id, AVG(amount) AS dept_avg
    FROM Salary JOIN Employee USING(employee_id)
    GROUP BY pay_month, department_id
) d
JOIN (
    SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, AVG(amount) AS company_avg
    FROM Salary GROUP BY pay_month
) c USING(pay_month)
ORDER BY pay_month DESC, department_id;
