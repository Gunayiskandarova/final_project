import psycopg2
from final_project.flight.flight_postgres import connection_to_database

def find_flight_by_id():
    conn = None
    cursor = None
    
    # İstifadəçidən uçuş ID-sini daxil etməsini xahiş edirik
    flight_id = input("Zəhmət olmasa uçuş ID-sini daxil edin: ")

    try:
        conn = connection_to_database()
        conn.autocommit = False  # Auto-commit'i söndürmək üçün
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights WHERE id = %s", (flight_id,))
        
        flight = cursor.fetchone()
        
        if flight:
            conn.commit()  # Uğurlu əməliyyat olarsa commit et
        else:
            conn.rollback()  # Uçuş tapılmadıqda rollback et
        
        return flight

    except psycopg2.Error as e:
        if conn:
            conn.rollback()  # Xəta baş verərsə rollback et
        print(f"PostgreSQL xəta baş verdi: {e}")
        return None

    except Exception as e:
        if conn:
            conn.rollback()  # Digər xətalar üçün də rollback et
        print(f"Xəta baş verdi: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Funksiyanı işlədərək uçuşu tapmaq
flight = find_flight_by_id()
if flight:
    print(f"Uçuş tapıldı: {flight}")
else:
    print("Uçuş tapılmadı.")