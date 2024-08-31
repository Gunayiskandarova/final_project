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
  cursor = conn.cursor()
  try:
    cursor.execute(delete_query, (flight_id,))
    conn.commit()
    print(f"FLİGHT ID {flight_id} SUCCESSFULLY DELETE!")
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
      result = curr.fetchone() 
      print(result)
  except Exception as e:
    print(f"Error: {e}")

def update_seat(seat_number, is_available, conn):
  update_query = """
  UPDATE seats
  SET is_available = %s
  WHERE seat_number = %s;
  """
  cursor = conn.cursor()
  try:
    cursor.execute(update_query, (is_available, seat_number))
    conn.commit()
    print(f"SEATS {seat_number} UPDATE SUCCESSFULLY !")
  except Exception as e:
    conn.rollback()
    print(f"Error Detected: {e}")
    
# def merge (list):
#   if len (list) > 1:
#     print ("break list" + str (list) )
#     middle=len (list)//2
#     left_list= list[: middle]
#     right_list =list [middle:]

#     merge(left_list)
#     merge (right_list)
#     mergeSort(list, left_list, right_list)

# def mergeSort (list, left_list, right_list):
#   i=0
#   j=0
#   k=0

#   while i< len(left_list) and j< len (right_list):
#     if left_list[i] < right_list[j]:
#       list[k]=left_list[i]
#       i+=1
#     else:
#       list [k] =right_list[j] 
#       j+=1
#     k+=1
#   while i< len(left_list):
#     list [k]=left_list[i]
#     i+=1
#     k+=1
#   while j< len(right_list):
#     list [k]=right_list[j]
#     j+=1
#     k+=1  
#   print ("combine list" + str (list) )


  
# input_list=input("Give own list please:") 
# shuffle_list=list(map(int, input_list.split()))
# merge(shuffle_list)
# print (shuffle_list)


