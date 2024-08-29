from booking.booking_operation import create_booking_details
from booking.booking_postgress import save_booking_details
from flight.flight_operation import create_flight_details
from flight.flight_postgres import save_flight_details
from config.connect_postgres import connect_to_database

def console_menu():
    print("Welcome to FLIGHT")
    print("Please select option:")
    print("Press 1 for add new flight")
    print("Press 2 for add new booking")
    print("Press 3 for display all flight")
    print("Press 4 for exit")
    choise = input("Please choice your option: ")
    return choise


def main():
    while True:
        print("Welcome to Booking Menyu!!!!")
        choise = console_menu()
        postgres = connect_to_database()
        # postgres = postgres_connection.connect_to_database()
        if choise == "1":
            print("------")
            flight_details = create_flight_details()
            save_flight_details (flight_details, postgres)
        elif choise=="2":
            booking_details=create_booking_details()
            save_booking_details(booking_details,postgres)
        elif choise=="3":
            pass
        elif choise==4:
            break
        else:
            print("Please choise correct vaeriant:")







