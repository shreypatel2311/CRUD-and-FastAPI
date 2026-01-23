CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    price NUMERIC(10,2),
    status VARCHAR(20) DEFAULT 'PLACED',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION calculate_total_amount(
    qty INT,
    price NUMERIC
)
RETURNS NUMERIC AS $$
BEGIN
    RETURN qty * price;
END;
$$ LANGUAGE plpgsql;