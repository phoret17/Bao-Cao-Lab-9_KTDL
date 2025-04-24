-- Tạo bảng accounts
CREATE TABLE IF NOT EXISTS accounts (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address_1 TEXT,
    address_2 TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(20),
    join_date DATE
);

-- Tạo bảng products
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_code VARCHAR(50),
    product_description TEXT
);

-- Tạo bảng transactions
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(100) PRIMARY KEY,
    transaction_date DATE,
    product_id INT,
    product_code VARCHAR(50),
    product_description TEXT,
    quantity INT,
    account_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (account_id) REFERENCES accounts(customer_id)
);
