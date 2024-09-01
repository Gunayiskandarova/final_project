from booking.booking_operation import create_booking_details,booking_update_details
from booking.booking_postgress import save_booking_details,update_booking, find_all_booking, delete_booking, find_booking_by_id, save_booking, update_delete_bookings, update_save_bookings
from flight.flight_operation import create_flight_details, flight_update_details 
from flight.flight_postgres import save_flight_details, uptade_flight, find_flight_by_id, delete_flight,find_all_flights, find_flights_by_origin
from config.connect_postgres import connect_to_database

def console_menu():
    print("Welcome to FLIGHT")
    print("Please select option:")
    print("Press 1 for add new flight")
    print("Press 2 for add new booking")
    print("Press 3 for find flight by id")
    print("Press 4 for find all booking")
    print("Press 5 for booking update") 
    print("Press 6 for flight update") 
    print("Press 7 for delete flight")  
    print("Press 8 for delete booking") 
    print("Press 9 for find all flight")   
    print("Press 10 for find flight by origin")    
    print("Press 11 for find booking by id")     
    choise = input("Please choice your option: ")
    return choise


def main():
    while True:
        print("Welcome to Booking Menyu!!!!")
        choise = console_menu()
        postgres = connect_to_database()
 
        if choise == "1":
            print("------")
            flight_details = create_flight_details()
            save_flight_details (flight_details, postgres)
        elif choise=="2":
            booking_details=create_booking_details()
            save_booking_details(booking_details,postgres)
            
        elif choise == "3":
            flight_id = int(input("Enter id: "))
            find_flight_by_id(flight_id, postgres)
        elif choise== "4":
            find_all_booking(postgres)
        elif choise == "5":
            update_details = booking_update_details()
            update_for_id = int(input("Enter update id: "))
            update_booking(update_for_id, update_details, postgres)
        elif choise=="6":
            uptade_details = flight_update_details()
            update_for_id = int(input("Enter update ID: "))
            uptade_flight(update_for_id, uptade_details, postgres)
        elif choise == "7":
            flight_id= int(input("Enter id: "))
            delete_flight(flight_id, postgres)
        elif choise == "8":
            booking_id = int(input("Enter id: "))
            delete_booking(booking_id,postgres)
        elif choise == "9":
             find_all_flights(postgres)
        elif choise == "10":
            origin = input("Enter origin city: ")
            find_flights_by_origin(origin, postgres)
        elif choise =="11":
            flight_id = int(input("Enter id: "))
            find_booking_by_id(flight_id, postgres)            
        else:
            print("Please choise correct variant:")







