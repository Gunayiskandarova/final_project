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
  
def find_booking_by_id(flight_id, conn):
  insert_query = '''
  SELECT * FROM booking
  WHERE id = %s
  '''
  try:
    with conn.cursor() as curr:
      curr.execute(insert_query, (flight_id,))
      result = curr.fetchone() 
      print(result)
  except Exception as e:
    print(f"Error: {e}")


def delete_booking(booking_id, conn):

 select_query = """
 SELECT COUNT(*) FROM booking
 WHERE id = %s;
 """
 delete_query = """
 DELETE FROM booking
 WHERE id = %s;
 """
 cursorr = conn.cursor()
 try:     
  cursorr.execute(select_query, (booking_id,))
  result = cursorr.fetchone()
  
  if result:
      count = int(result[0])  
  else:
      count = 0
  if count >0:
      cursorr.execute(delete_query, (booking_id,))
      conn.commit()
      print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")
  else:
      conn.close()
      print("wrong id again")    
 except Exception as e:
     conn.rollback()
     print(f"Error detected: {e}")
    


def update_save_bookings(flight_id, seat_count, conn):
    update_query = """UPDATE flight SET seats = seats - %s
                      WHERE id = %s"""
    cursor = conn.cursor()
    try:
        cursor.execute(update_query, (seat_count, flight_id))
        print("Count of seats updated successfully!")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()

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
        update_save_bookings(booking_details["flight_id"], booking_details["count_seat"], conn)
        
        print("Booking details saved successfully")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def update_delete_bookings(id, flight_id, seat_count, seat, conn):
    insert_query = """
    select id, seat
    from flight
    """
    update_query = """UPDATE flight SET seats = seats + %s
                      WHERE id = %s"""
    cursor = conn.cursor()
    try:
        cursor.execute (insert_query, ( id, flight_id,  seat))
        conn.commit()
        cursor.execute(update_query, (seat_count, flight_id))
        print("Count of seats updated successfully!")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()

def delete_booking(booking_id, conn):
    select_query = """
    SELECT flight_id, seat_count FROM booking
    WHERE id = %s;
    """
    delete_query = """
    DELETE FROM booking
    WHERE id = %s;
    """
    cursorr = conn.cursor()
    try:
        # Sifarişin uçuş və oturacaq məlumatlarını əldə edin
        cursorr.execute(select_query, (booking_id,))
        result = cursorr.fetchone()
        
        if result:
            flight_id, seat_count = result
            
            # Sifarişi silin
            cursorr.execute(delete_query, (booking_id,))
            conn.commit()
            
            # Oturacaq sayını yeniləyin
            update_delete_bookings(flight_id, seat_count, conn)
            
            print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETED!")
        else:
            print("wrong id again")
    except Exception as e:
        conn.rollback()
        print(f"Error detected: {e}")
    finally:
        cursorr.close()

def update_delete_bookings(flight_id, seat_count, conn):
    update_query = """UPDATE flight SET seats = seats + %s
                      WHERE id = %s"""
    cursor = conn.cursor()
    try:
        cursor.execute(update_query, (seat_count, flight_id))
        print("Count of seats updated successfully!")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()