-- Temporary tables are typically session-specific, meaning they are only available within the current database session. They are automatically dropped when the session ends.

-- Create a temporary table to store employee data
CREATE TEMPORARY TABLE temp_employee (
    employee_id INT,
    employee_name VARCHAR(255),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert data into the temporary table
INSERT INTO temp_employee (employee_id, employee_name, department, salary)
VALUES
    (1, 'John Doe', 'HR', 55000.00),
    (2, 'Jane Smith', 'Marketing', 60000.00),
    (3, 'Bob Johnson', 'IT', 65000.00);
