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


def update_booking(id, booking_update_details, conn):
  update_query = """UPDATE booking
  SET
  passenger_name = %s,
  flight_id = %s,
  seat_count = %s
  WHERE id = %s"""
  cursor = conn.cursor()
  try:
    cursor.execute(update_query, (
      booking_update_details["passenger_name"],
      booking_update_details["flight_id"],
      booking_update_details["seat_count"],
      booking_update_details["id"]
      ))
    conn.commit()
    print("Updated successfully")
  except Exception as e:
    conn.rollback()
    print(f"Error: {e}")

def find_all_booking(conn):
  insert_query = """
  SELECT * FROM booking;
  """
  try:
    curr=conn.cursor()
    curr.execute(insert_query)
    results = curr.fetchall()
    for row in results:
      print(row)
  except Exception as e:
    print(f"Error: {e}")


def delete_booking(booking_id,conn):
  delete_query = """
  DELETE FROM booking
  WHERE id = %s;
  """
  cursor = conn.cursor()
  try:
    cursor.execute(delete_query, (booking_id,))
    conn.commit()
    print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")


  except Exception as e:
    conn.rollback()
    print(f"Error deleting booking: {e}")
  finally:
    conn.close()