def create_booking_details():
    booking_details = {}
    booking_details["id"] = input("Enter booking ID: ")
    booking_details["passenger_name"] = input("Enter passenger name: ")
    booking_details["flight_id"] = int(input("Enter flight ID: "))
    booking_details["count_seat"] =int(input("Enter count seat: "))
    return booking_details