def save_booking_details (booking_details, conn):
    insert_query = """
    insert into public.booking(id, passenger_name, flight_id, count_seat
    values(%s, %s, %s, %s)"""
    cursor = conn.cursor
    try:
        cursor.execute(insert_query(
            booking_details["id"],
            booking_details["passengger_name"],
            booking_details["flight_id"],
            booking_details["count_seats"]
        ))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        con.close()
