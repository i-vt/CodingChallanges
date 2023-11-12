    --Use a CTE to simplify a complex query to find the total sales for each product category.

WITH SalesCTE AS (
    SELECT category, SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY category
)
SELECT category, total_sales
FROM SalesCTE;
