-- Use the alx_book_store database
USE alx_book_store;

-- Query to retrieve the column type information for the 'Books' table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Books'
  AND TABLE_SCHEMA = 'alx_book_store';
