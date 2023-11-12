-- Calculate the total sales for each product category.

SELECT category, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY category;
