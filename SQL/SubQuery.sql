SELECT employee_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees GROUP BY department);

-- Retrieve all employees who earn more than the average salary in their department.
