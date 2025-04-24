-- Tạo bảng accounts
CREATE TABLE accounts (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    address_1 VARCHAR(100) NOT NULL,
    address_2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,  -- Đã sửa từ CHAR(2) -> VARCHAR(50)
    zip_code VARCHAR(10) NOT NULL,
    join_date DATE NOT NULL
);
CREATE INDEX idx_accounts_city ON accounts(city);

-- Tạo bảng products
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_code VARCHAR(10) NOT NULL,  -- Đã sửa từ CHAR(2) -> VARCHAR(10)
    product_description VARCHAR(255) NOT NULL
);
CREATE INDEX idx_products_code ON products(product_code);

-- Tạo bảng transactions
CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    transaction_date DATE NOT NULL,
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL CHECK (quantity > 0),
    account_id INT REFERENCES accounts(customer_id)
);
CREATE INDEX idx_transactions_date ON transactions(transaction_date);