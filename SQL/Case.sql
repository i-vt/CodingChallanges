-- Create a query that categorizes products as "High" or "Low" based on their prices.

SELECT product_name,
    CASE
        WHEN price > 100 THEN 'High'
        ELSE 'Low'
    END AS price_category
FROM products;
