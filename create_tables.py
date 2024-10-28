import os
import psycopg2
from psycopg2 import sql

def create_tables():
    # Database connection parameters from environment variables
    user = os.getenv("DB2_USER")
    password = os.getenv("DB2_PASSWORD")
    host = os.getenv("DB2_HOST", "localhost")
    dbname = os.getenv("DB2_NAME")

    try:
        # Connect to the database
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            dbname=dbname
        )
        cursor = connection.cursor()
        
        # Create users table with full_name column
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            full_name VARCHAR(255) NOT NULL,
            password TEXT NOT NULL
        )
        """
        cursor.execute(create_users_table_query)
        
        # Create images table with a foreign key to the users table
        create_images_table_query = """
        CREATE TABLE IF NOT EXISTS images (
            id SERIAL PRIMARY KEY,
            image_name VARCHAR(255) UNIQUE NOT NULL,
            image_data BYTEA NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
        """
        cursor.execute(create_images_table_query)
        
        # Commit the transaction
        connection.commit()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        print("Tables created successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error while creating tables:", error)

if __name__ == "__main__":
    create_tables()