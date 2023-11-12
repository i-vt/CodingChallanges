-- Assuming you have a large dataset, you can create an index on a column to improve query performance. For example, to speed up searching for products by name.
CREATE INDEX idx_product_name ON products(product_name);
