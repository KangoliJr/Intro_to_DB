import mysql.connector


def create_database():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Xander.Joe321',
    }
    
    conn = None
    try:
        # Establishing a connection to the MySQL server 
        conn = mysql.connector.connect(**db_config)
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # SQL statement to create the database if it doesn't exist
            # The IF NOT EXISTS clause prevents an error if the database already exists.
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")
    finally:
        # Close the connection
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()