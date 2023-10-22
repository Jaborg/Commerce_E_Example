CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    timestamp TIMESTAMP
);