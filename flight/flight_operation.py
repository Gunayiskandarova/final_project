def create_flight_details ():
     flight_details = {}
     flight_details["id"] = input("Enter flight ID: ")
     flight_details["flight_number"] = input("Enter flight_number: ")
     flight_details["date"] = input("Enter flight date (YYYY-MM-DD): ")
     flight_details["time"] = input("Enter flight time (HH:MM): ")
     flight_details["origin"] = input("Enter flight origin: ")
     flight_details["destination"]=input("Enter flight destination: ")
     flight_details["seats"] = input("Enter flight seat: "); 
     return flight_details

def flight_update_details():
     flight_update_details = {}
     flight_update_details["flight_number"] = input("Update flight number: ")
     flight_update_details["date"] = input("Update a date: ")
     flight_update_details["time"] = input("Update time: ")
     flight_update_details["origin"] = input("Update origin: ")
     flight_update_details["destination"] = input("Update destination: ")
     flight_update_details["seats"] = input("Update seats: ")
     return flight_update_details



# def flight_delete_details ():
#       flight_delete = {}
#       flight_delete['id']=input ("Enter flight_id: ")     
#       flight_delete['flight_number']=input ("Enter flight_number: ")
#       flight_delete['date']=input ("Enter flight_date (YYY.MM.DD): ")
#       flight_delete['time']=input ("Enter flight_time (HH:MM): ")
#       flight_delete['origin']=input ("Enter flight_origin: ")
#       flight_delete['destination']=input ("Enter flight_destination: ")
#       flight_delete['seats']= input ("Enter flight_seats: ")
#       return flight_delete






























