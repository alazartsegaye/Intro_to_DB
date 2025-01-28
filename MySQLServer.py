import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',      
            user='root',           #
            password='password'  
        )

        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database only if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")  # Success message
    except Error as e:
        # Print error message if any exception occurs
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection to avoid resource leaks
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    create_database()
