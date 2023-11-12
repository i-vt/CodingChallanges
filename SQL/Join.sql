-- Perform a self-join to find employees who share the same manager.
SELECT e1.employee_name, e2.employee_name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.employee_id;
