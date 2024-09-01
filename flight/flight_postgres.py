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

def uptade_flight(id, flight_update_details, conn):
  uptade_query = """Update flight 
  SET 
  flight_number = %s,
  date_flight = %s,
  time_flight = %s,
  origin = %s, 
  destination = %s,
  seats = %s
  WHERE id = %s"""
  cursor = conn.cursor()

  try:
    cursor.execute(uptade_query, (
      flight_update_details["flight_number"],
      flight_update_details["date"],
      flight_update_details["time"],
      flight_update_details["origin"],
      flight_update_details["destination"],
      flight_update_details["seats"],
      id
      ))
    conn.commit()
    print("Uptaded successfully!")
  except Exception as e:
    conn.rollback()
    print(f"error detected {e}")

def delete_flight(flight_id, conn):
 delete_query = """
 DELETE FROM flights
 WHERE id = %s;
 """
 select_query = """
 SELECT COUNT(*) FROM flight
 WHERE id = %s;
 """
 cursorr = conn.cursor()
 try:     
  cursorr.execute(select_query, (flight_id,))
  result = cursorr.fetchone()
  
  if result:
      count = int(result[0])  
  else:
      count = 0
  if count >0:
      cursorr.execute(delete_query, (flight_id,))
      conn.commit()
      print(f"FLİGHT ID {flight_id} SUCCESSFULLY DELETE!")
  else:
      conn.close()
      print("wrong id again")    
 except Exception as e:
  conn.rollback()
  print(f"Error detected: {e}")

def find_flight_by_id(flight_id, conn):
  insert_query = '''
  SELECT * FROM flight
  WHERE id = %s
  '''
  try:
    with conn.cursor() as curr:
      curr.execute(insert_query, (flight_id,))
      result = curr.fetchone() 
      print(result)
  except Exception as e:
    print(f"Error: {e}")

def find_all_flights(conn):
  insert_query = """
  SELECT * FROM flight;
  """
  try:
    curr=conn.cursor()
    curr.execute(insert_query)
    results = curr.fetchall()
    for row in results:
      print(row)
  except Exception as e:
    print(f"Error: {e}")

  except Exception as e:
      print(f"Xəta baş verdi: {e}")
      conn.rollback()

  finally:
    curr.close()
    conn.close()

def find_flights_by_origin(origin, conn):
    insert_query = '''
    SELECT * FROM flight
    WHERE origin = %s
    '''
    try:
        with conn.cursor() as curr:
         curr.execute(insert_query, (origin,))
         result = curr.fetchall() 
         for row in result:
             print(row)
    except Exception as e:
        print(f"Error: {e}")


def merge_sort_by_date(flight):
    if len(flight) <= 1:
        return flight

    middle = len(flight) // 2
    left_list = merge_sort_by_date(flight[:middle])
    right_list = merge_sort_by_date(flight[middle:])

    return merge_dates(left_list, right_list)

def merge_dates(left, right):
    sorted_flight = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]['date_flight'] < right[j]['date_flight']:
            sorted_flight.append(left[i])
            i += 1
        else:
            sorted_flight.append(right[j])
            j += 1

    sorted_flight.extend(left[i:])
    sorted_flight.extend(right[j:])
    return sorted_flight

