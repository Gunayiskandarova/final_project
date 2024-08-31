import psycopg2
from final_project.config.connect_postgres import connect_to_database

def find_all_flights():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights")
        flights = cursor.fetchall()  

        return flights

    except psycopg2.Error as e:
        print(f"PostgreSQL ilə əlaqədar xəta baş verdi: {e}")
        return None

    except Exception as e:
        print(f"Xəta baş verdi: {e}")
        return None

    finally:
              cursor.close()
              conn.close()













import psycopg2
from final_project.config.connect_postgres import connect_to_database

def find_flight_by_id(flight_id):
        flight_id=input("enter flight id:")
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            conn = connection_to_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE id = %s", (flight_id,))
            flight = cursor.fetchone()
            
            if flight:
                return flight
            else:
                print("Belə bir uçuş yoxdur.")
                return None
                
        except Exception as e:
            print(f"Xəta baş verdi: {e}")
            return None
            
        finally:
                cursor.close()
                conn.close()



    
from final_project.config.connect_postgres import connect_to_database
def find_flights_by_origin(origin):
        conn = connect_to_database()
        cursor = conn.cursor
        try:
            conn = connection_to_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE origin = %s", (origin,))
            flights = cursor.fetchall()
            return flights
        
        except psycopg2.Error as e:
            print(f"PostgreSQL xəta baş verdi: {e}")
            return None
            
        except Exception as e:
            print(f"Xəta baş verdi: {e}")
            return None
            
        finally:
                cursor.close()
                conn.close()


from final_project.config.connect_postgres import connect_to_database
def find_flights_by_origin(origin):
        conn = connect_to_database()
        cursor = conn.cursor
        try:
            conn = connection_to_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE origin = %s", (origin,))
            flights = cursor.fetchall()
            return flights
        
        except psycopg2.Error as e:
            print(f"PostgreSQL xəta baş verdi: {e}")
            return None
            
        except Exception as e:
            print(f"Xəta baş verdi: {e}")
            return None
            
        finally:
                cursor.close()
                conn.close()
