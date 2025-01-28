This repository contains scripts to set up and manage the `alx_book_store` database, designed for an online bookstore. Below is a brief overview of each task and its purpose.

## Tasks Overview

### 1. `alx_book_store.sql`

This script creates the `alx_book_store` database and defines its schema.

- **Creates Tables:**
  - Authors
  - Books
  - Customers
  - Orders
  - Order\_Details
- **Relationships:** Establishes foreign key constraints between tables.

### 2. `MySQLServer.py`

A Python script to programmatically create the `alx_book_store` database.

- Verifies if the database exists; creates it if not.
- Prints success or error messages.
- Ensures proper connection handling.

### 3. `task_2.sql`

This script creates all necessary tables in the `alx_book_store` database.

- **Tables Created:**
  - Authors
  - Books
  - Customers
  - Orders
  - Order\_Details
- Includes primary keys and foreign key constraints.

### 4. `task_3.sql`

Lists all tables in the `alx_book_store` database.

- **Purpose:** Verifies the existence of tables.
- **Key Query:** `SHOW TABLES;`

### 5. `task_4.sql`

Retrieves column metadata for the `Books` table.

- **Purpose:** Displays column names and data types.
- **Key Query:**
  ```sql
  SELECT COLUMN_NAME, COLUMN_TYPE
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_NAME = 'Books'
    AND TABLE_SCHEMA = 'alx_book_store';
  ```

### 6. `task_5.sql`

Inserts a single row into the `customer` table.

- **Inserted Data:**
  - `customer_id`: 1
  - `customer_name`: Cole Baidoo
  - `email`: [cbaidoo@sandtech.com](mailto\:cbaidoo@sandtech.com)
  - `address`: 123 Happiness Ave.
- **Key Query:**
  ```sql
  INSERT INTO customer (customer_id, customer_name, email, address)
  VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
  ```

### 7. `task_6.sql`

Placeholder for additional tasks/scripts related to the `alx_book_store` database.