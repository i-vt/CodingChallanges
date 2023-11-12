-- Pivot a table to display sales data by month as columns.

SELECT *
FROM (
    SELECT product, month, sales_amount
    FROM sales
) AS SourceTable
PIVOT (
    SUM(sales_amount)
    FOR month IN (January, February, March)
) AS PivotTable;
