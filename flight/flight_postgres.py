
def find_flights_by_origin(origin, conn):
    select_query = '''
    SELECT * FROM flight
    WHERE origin = %s
    '''
    try:
        with conn.cursor() as curr:
            curr.execute(select_query, (origin,))
            result = curr.fetchall()
            flights = []
            for row in result:
                flights.append({
                    "id": row[0],
                    "origin": row[1],
                    "destination": row[2],
                    "departure_time": row[3],
                    "arrival_time": row[4],
                    "seat_count": row[5]
                })
            return flights
    except Exception as e:
        print(f"Error: {e}")
        return None



# # Uçuş bilgilerini güncelle
# def update_flight(flight_id, flight_update_details, conn):
#     update_query = """
#         UPDATE flight 
#         SET flight_number = %s,
#             date_flight = %s,
#             time_flight = %s,
#             origin = %s, 
#             destination = %s,
#             seats = %s
#         WHERE id = %s
#     """
#     cursor = conn.cursor()
#     try:
#         cursor.execute(update_query, (
#             flight_update_details["flight_number"],
#             flight_update_details["date"],
#             flight_update_details["time"],
#             flight_update_details["origin"],
#             flight_update_details["destination"],
#             flight_update_details["seats"],
#             flight_id
#         ))
#         conn.commit()
#         print("Flight updated successfully.")
#     except Exception as e:
#         print(f"Error: {e}")
#         conn.rollback()
#     finally:
#         cursor.close()


# # Uçuşu sil
# def delete_flight(flight_id, conn):
#     delete_query = "DELETE FROM flight WHERE id = %s;"
#     select_query = "SELECT COUNT(*) FROM flight WHERE id = %s;"
#     cursor = conn.cursor()
#     try:
#         cursor.execute(select_query, (flight_id,))
#         result = cursor.fetchone()

#         if result and result[0] > 0:
#             cursor.execute(delete_query, (flight_id,))
#             conn.commit()
#             print(f"Flight ID {flight_id} successfully deleted.")
#         else:
#             print(f"No flight found with ID {flight_id}.")
#     except Exception as e:
#         print(f"Error: {e}")
#         conn.rollback()
#     finally:
#         cursor.close()


# # Uçuşu ID'ye göre bul
# def find_flight_by_id(flight_id, conn):
#     select_query = "SELECT * FROM flight WHERE id = %s;"
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(select_query, (flight_id,))
#             result = cursor.fetchone()
#             if result:
#                 flight_data = {
#                     "id": result[0],
#                     "flight_number": result[1],
#                     "date_flight": result[2].isoformat(),  # Tarih bilgisi JSON uyumlu hale getiriliyor
#                     "time_flight": result[3].isoformat(),  # Saat bilgisi JSON uyumlu hale getiriliyor
#                     "origin": result[4],
#                     "destination": result[5],
#                     "seats": result[6]
#                 }
#                 return flight_data
#             else:
#                 print(f"No flight found with ID {flight_id}.")
#                 return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None



# # Tüm uçuşları getir
# def find_all_flights(conn):
#     select_query = "SELECT * FROM flight;"
#     try:
#         cursor = conn.cursor()
#         cursor.execute(select_query)
#         results = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]

#         flights = []
#         for row in results:
#             flight = {}
#             for col, val in zip(columns, row):
#                 if isinstance(val, (datetime.date, datetime.time)):
#                     flight[col] = val.isoformat()
#                 else:
#                     flight[col] = val
#             flights.append(flight)

#         cursor.close()
#         return flights
#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# def find_flights_by_origin(origin, conn):
#     select_query = "SELECT * FROM flight WHERE origin = %s;"
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(select_query, (origin,))
#             results = cursor.fetchall()
#             for row in results:
#                 print(row)
#     except Exception as e:
#         print(f"Error: {e}")


# def merge_sort_by_date(flights):
#     if len(flights) <= 1:
#         return flights

#     middle = len(flights) // 2
#     left = merge_sort_by_date(flights[:middle])
#     right = merge_sort_by_date(flights[middle:])

#     return merge_dates(left, right)


# def merge_dates(left, right):
#     sorted_flights = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i]['date_flight'] < right[j]['date_flight']:
#             sorted_flights.append(left[i])
#             i += 1
#         else:
#             sorted_flights.append(right[j])
#             j += 1

#     sorted_flights.extend(left[i:])
#     sorted_flights.extend(right[j:])
#     return sorted_flights

import datetime


# Uçuş bilgilerini veritabanına kaydet
def save_flight_details(flight_details, conn):
    insert_query = """
        INSERT INTO flight (id, flight_number, date_flight, time_flight, origin, destination, seats)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_query, (
            flight_details["id"],
            flight_details["flight_number"],
            flight_details["date_flight"],
            flight_details["time_flight"],
            flight_details["origin"],
            flight_details["destination"],
            flight_details["seats"]
        ))
        conn.commit()
        print("Flight saved to database.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()


# Uçuş bilgilerini güncelle
def update_flight(flight_id, flight_update_details, conn):
    update_query = """
        UPDATE flight 
        SET flight_number = %s,
            date_flight = %s,
            time_flight = %s,
            origin = %s, 
            destination = %s,
            seats = %s
        WHERE id = %s
    """
    cursor = conn.cursor()
    try:
        cursor.execute(update_query, (
            flight_update_details["flight_number"],
            flight_update_details["date_flight"],
            flight_update_details["time_flight"],
            flight_update_details["origin"],
            flight_update_details["destination"],
            flight_update_details["seats"],
            flight_id
        ))
        conn.commit()
        print("Flight updated successfully.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()


# Uçuşu sil
def delete_flight(flight_id, conn):
    delete_query = "DELETE FROM flight WHERE id = %s;"
    select_query = "SELECT COUNT(*) FROM flight WHERE id = %s;"
    cursor = conn.cursor()
    try:
        cursor.execute(select_query, (flight_id,))
        result = cursor.fetchone()

        if result and result[0] > 0:
            cursor.execute(delete_query, (flight_id,))
            conn.commit()
            print(f"Flight ID {flight_id} successfully deleted.")
        else:
            print(f"No flight found with ID {flight_id}.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()


# Uçuşu ID'ye göre bul
def find_flight_by_id(flight_id, conn):
    select_query = "SELECT * FROM flight WHERE id = %s;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(select_query, (flight_id,))
            result = cursor.fetchone()
            if result:
                flight_data = {
                    "id": result[0],
                    "flight_number": result[1],
                    "date_flight": result[2].isoformat(),  # Tarih bilgisi JSON uyumlu hale getiriliyor
                    "time_flight": result[3].isoformat(),  # Saat bilgisi JSON uyumlu hale getiriliyor
                    "origin": result[4],
                    "destination": result[5],
                    "seats": result[6]
                }
                return flight_data
            else:
                print(f"No flight found with ID {flight_id}.")
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Tüm uçuşları getir
def find_all_flights(conn):
    select_query = "SELECT * FROM flight;"
    try:
        cursor = conn.cursor()
        cursor.execute(select_query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        flights = []
        for row in results:
            flight = {}
            for col, val in zip(columns, row):
                if isinstance(val, (datetime.date, datetime.time)):
                    flight[col] = val.isoformat()
                else:
                    flight[col] = val
            flights.append(flight)

        cursor.close()
        return flights
    except Exception as e:
        print(f"Error: {e}")
        return None


def find_flights_by_origin(origin, conn):
    select_query = "SELECT * FROM flight WHERE origin = %s;"
    try:
        with conn.cursor() as cursor:
            cursor.execute(select_query, (origin,))
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            flights = []
            for row in results:
                flight = {}
                for col, val in zip(columns, row):
                    if isinstance(val, (datetime.date, datetime.time)):
                        flight[col] = val.isoformat()
                    else:
                        flight[col] = val
                flights.append(flight)
            cursor.close()
            return flights
    except Exception as e:
        print(f"Error: {e}")


def merge_sort_by_date(flights):
    if len(flights) <= 1:
        return flights

    middle = len(flights) // 2
    left = merge_sort_by_date(flights[:middle])
    right = merge_sort_by_date(flights[middle:])

    return merge_dates(left, right)


def merge_dates(left, right):
    sorted_flights = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]['date_flight'] < right[j]['date_flight']:
            sorted_flights.append(left[i])
            i += 1
        else:
            sorted_flights.append(right[j])
            j += 1

    sorted_flights.extend(left[i:])
    sorted_flights.extend(right[j:])
    return sorted_flights