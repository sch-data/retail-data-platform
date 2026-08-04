-- Draft PostgreSQL schema for Version 3

CREATE TABLE products (
    stock_code VARCHAR(20) PRIMARY KEY,
    description TEXT
);

CREATE TABLE invoices (
    invoice_id VARCHAR(20) PRIMARY KEY,
    invoice_date TIMESTAMP NOT NULL,
    customer_id INT,
    country VARCHAR(100) NOT NULL
);

CREATE TABLE invoice_items (
    invoice_item_id SERIAL PRIMARY KEY,
    invoice_id VARCHAR(20) NOT NULL,
    stock_code VARCHAR(20) NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC(12, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
    FOREIGN KEY (stock_code) REFERENCES products(stock_code)
);