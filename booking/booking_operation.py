def create_booking_details():
    booking_details = {}
    booking_details["id"] = input("Enter booking ID: ")
    booking_details["passenger_name"] = input("Enter passenger name: ")
    booking_details["flight_id"] = int(input("Enter flight ID: "))
    booking_details["count_seat"] =int(input("Enter count seat: "))
    return booking_details


def booking_update_details():
  booking_update_details = {}
  booking_update_details["passenger_name"] = input("Update passenger name: ")
  booking_update_details["flight_id"] = input("Update flight id: ")
  booking_update_details["seat_count"] = input("Update seat count: ")
  return booking_update_details

