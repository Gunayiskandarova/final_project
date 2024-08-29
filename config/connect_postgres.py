from psycopg2 import connect, OperationalError


def connect_to_database():

    try:
        conn = connect(
            dbname = "postgres",
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = 5050
        )
        print("Connected to Database")
        return conn
    except OperationalError as e:
        print(f"Error: {e}")
        return None


connect_to_database()
    


