def save_flight_details(flight_details, conn):
    insert_query = """
        INSERT INTO flight (id, flight_number, date_flight, time_flight, origin, destination, seats)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    # cursor() fonksiyonunu çağırarak bir cursor oluşturuyoruz
    cursor = conn.cursor()
    
    try:
        # execute fonksiyonunu çağırarak veriyi sorguya ekliyoruz
        cursor.execute(insert_query, (
            flight_details["id"],
            flight_details["flight_number"],
            flight_details["date"],
            flight_details["time"],
            flight_details["origin"],
            flight_details["destination"],
            flight_details["seats"]
        ))
        print("save to database")
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
