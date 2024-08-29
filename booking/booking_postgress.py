def save_booking_details(booking_details, conn):
    insert_query = """
        INSERT INTO public.booking (id, passenger_name, flight_id, seat_count)
        VALUES (%s, %s, %s, %s)
    """
    cursor = conn.cursor()
    
    try:
        cursor.execute(insert_query, (
            booking_details["id"],
            booking_details["passenger_name"],
            booking_details["flight_id"],
            booking_details["count_seat"]
        ))
        conn.commit()
        print("Booking details saved successfully")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()  
        conn.close()   
