def create_flight_details ():
     flight_details = {}
     flight_details[id] = input("Enter flight ID: ")
     flight_details[flight_number] = input("Enter flight_number: ")
     flight_details[date] = input("Enter flight date:")
     flight_details[time] = input("Enter flight time: ")
     flight_details[origin] = input("Enter flight origin ")
     flight_details[seats] = input("Enter flight seat ")
     return flight_details