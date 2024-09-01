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
        # update_booking_save()
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


def delete_booking(booking_id,conn):
  delete_query = """
  DELETE FROM booking
  WHERE id = %s;
  """
  cursor = conn.cursor()
  try:
    cursor.execute(delete_query, (booking_id,))
    conn.commit()
    # update_seats_delete()
    print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")
  except Exception as e:
    conn.rollback()
    print(f"Error deleting booking: {e}")
  finally:
    conn.close()


from datetime import datetime

def merge_sort_by_date(dates, conn):
  cursor = conn.cursor()
  try:
    cursor.execute(dates,conn)
    if len(dates) <= 1:
     return dates

    middle = len(dates) // 2
    left_list = merge_sort_by_date(dates[:middle])
    right_list = merge_sort_by_date(dates[middle:])

    return merge_dates(left_list, right_list)
  except Exception as e:
    conn.rollback()
    print(f"Error deleting booking: {e}")
  finally:
    conn.close()

def merge_dates(left, right, conn):
  sorted_dates = []
  i = j = 0
  cursor = conn.cursor()
  cursor.execute(left,right, conn)

  while i < len(left) and j < len(right):
       if left[i] < right[j]:
         sorted_dates.append(left[i])
         i += 1
       else:
         sorted_dates.append(right[j])
         j += 1

  sorted_dates.extend(left[i:])
  sorted_dates.extend(right[j:])
  return sorted_dates


dates = [
  datetime ("YYYY-MM-DD"),
  datetime("YYYY-MM-DD"),
  datetime("YYYY-MM-DD"),
  datetime("YYYY-MM-DD"),
  datetime("YYYY-MM-DD")
]

sorted_dates = merge_sort_by_date(int(dates))
for date in sorted_dates:
       print(date.strftime('%Y-%M-%D'))     #"YYYY-MM-DD" string formata çevirmək üçün

def delete_booking(booking_id,conn):
 delete_query = """
 DELETE FROM booking
 WHERE id = %s;
 """
 cursor = conn.cursor()
 try:
  cursor.execute(delete_query, (booking_id,))
  a = conn.commit()
  if a == True:
    # update_delete_bookings()
    print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")
 except Exception as e:
  conn.rollback()
  print(f"Error deleting booking: {e}")
 finally:
  conn.close()





  def save_booking(booking_details, conn):
      insert_query = """
    INSERT INTO booking (id, passenger_name, flight_id, seat_count)
    VALUES (%s, %s, %s, %s)
        """

  cursor = conn.cursor()
  try:
    cursor.execute(insert_query, (
      booking_details["id"],
      booking_details["passenger_name"],
      booking_details["flight_id"],
      booking_details["seat_count"]
      # flight_id,
      # seat_count,
      ))
    conn.commit()
    update_save_bookings(flight_id, seat_count, conn)
    print("Saved successfully!")
  except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
  finally:
   cursor.close()

def update_save_bookings(flight_id, seat_count, conn):
  update_query = """UPDATE booking SET seat_count = seat_count - %s
  WHERE flight_id = %s"""
  cursor = conn.cursor()
  try:
    cursor.execute(update_query, (flight_id, seat_count))
    print("Count of seats updated successfully!")
    conn.commit()
  except Exception as e:
    conn.rollback()
    print(f"Error: {e}")


def update_delete_bookings(flight_id, seat_count, conn):
  insert_query = """UPDATE booking SET seat_count = seat_count + %s
  WHERE flight_id = %s"""
  cursor = conn.cursor()
  try:
    cursor.execute(insert_query, (flight_id, seat_count))
    print("Count of seats updated successfully!")
    conn.commit()
  except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
  

def delete_booking(booking_id, flight_id, seat_count, conn):
 delete_query = """
 DELETE FROM booking
 WHERE id = %s;
 """
 cursor = conn.cursor()
 try:
  cursor.execute(delete_query, (booking_id,))
  conn.commit()
  update_delete_bookings(flight_id, seat_count, conn)
  print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")
 except Exception as e:
  conn.rollback()
  print(f"Error deleting booking: {e}")
 finally:
  conn.close()