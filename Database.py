import psycopg2
from psycopg2 import sql
import bcrypt

class Database:
    def __init__(self, user, password, host, dbname):
        self.user = user
        self.password = password
        self.host = host
        self.dbname = dbname

    # Save user name, full name, and hashed password to database
    def saveCredentials(self, username, full_name, password):
        try:
            # Connect to the database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                dbname=self.dbname
            )
            cursor = connection.cursor()
            
            # Check if the username already exists
            check_query = sql.SQL("SELECT 1 FROM users WHERE username = %s")
            cursor.execute(check_query, (username,))
            if cursor.fetchone():
                print("Username already taken!")
                return
            
            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Insert credentials into the database
            insert_query = sql.SQL("INSERT INTO users (username, full_name, password) VALUES (%s, %s, %s)")
            cursor.execute(insert_query, (username, full_name, hashed_password))
            
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            print("Credentials saved successfully.")
        except psycopg2.IntegrityError as error:
            print(f"Error while saving credentials: {error}")
            if connection:
                connection.rollback()
        except (Exception, psycopg2.Error) as error:
            print("Error while saving credentials:", error)

    # Validate password against the stored hash for a given username
    def validatePassword(self, username, password):
        try:
            # Connect to the database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                dbname=self.dbname
            )
            cursor = connection.cursor()
            
            # Retrieve hashed password from the database
            select_query = sql.SQL("SELECT password FROM users WHERE username = %s")
            cursor.execute(select_query, (username,))
            result = cursor.fetchone()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            if result:
                stored_hashed_password = result[0].encode('utf-8')
                # Validate the provided password against the stored hash
                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                    return True
                else:
                    print("Invalid password.")
                    return False
            else:
                print("No password found for the given username.")
                return False
        except (Exception, psycopg2.Error) as error:
            print("Error while validating password:", error)
            return False

    # Save image to the database for a specific user
    def saveImage(self, username, image_name, image_data):
        try:
            # Connect to the database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                dbname=self.dbname
            )
            cursor = connection.cursor()
            
            # Retrieve user_id from the database
            select_user_query = sql.SQL("SELECT id FROM users WHERE username = %s")
            cursor.execute(select_user_query, (username,))
            user_id = cursor.fetchone()[0]
            
            # Insert image into the database
            insert_query = sql.SQL("INSERT INTO images (image_name, image_data, user_id) VALUES (%s, %s, %s)")
            cursor.execute(insert_query, (image_name, psycopg2.Binary(image_data), user_id))
            
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            print("Image saved successfully.")
        except (Exception, psycopg2.Error) as error:
            print("Error while saving image:", error)

    # Retrieve image from the database for a specific user
    def retrieveImage(self, username, image_name):
        try:
            # Connect to the database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                dbname=self.dbname
            )
            cursor = connection.cursor()
            
            # Retrieve user_id from the database
            select_user_query = sql.SQL("SELECT id FROM users WHERE username = %s")
            cursor.execute(select_user_query, (username,))
            user_id = cursor.fetchone()[0]
            
            # Retrieve image from the database
            select_query = sql.SQL("SELECT image_data FROM images WHERE image_name = %s AND user_id = %s")
            cursor.execute(select_query, (image_name, user_id))
            result = cursor.fetchone()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            if result:
                return result[0]
            else:
                print("No image found with the given name for the specified user.")
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error while retrieving image:", error)
            return None

    # Clear test data from the database
    def clearTestData(self):
        try:
            # Connect to the database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                dbname=self.dbname
            )
            cursor = connection.cursor()
            
            # Delete test data from the database
            cursor.execute("DELETE FROM images")
            cursor.execute("DELETE FROM users")
            
            # Commit the transaction
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            
            print("Test data cleared successfully.")
        except (Exception, psycopg2.Error) as error:
            print("Error while clearing test data:", error)