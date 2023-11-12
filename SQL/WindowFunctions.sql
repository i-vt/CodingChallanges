-- Rank employees by their sales performance within each department.
SELECT employee_name, department, sales_amount,
    RANK() OVER (PARTITION BY department ORDER BY sales_amount DESC) AS sales_rank
FROM employees;
