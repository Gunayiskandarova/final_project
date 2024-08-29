from final_project.booking.booking_operation import create_booking_details
from final_project.booking.booking_postgress import save_booking_details
from final_project.flight.flight_operation import create_flight_details
from final_project.flight.flight_postgres import save_flight_details
from final_project.config.connect_postgress import connect_to_database

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
        choise = input("Please choice your option: ")
        if choise==1:
            pass
        elif choise==2:
            pass
        elif choise==3:
            pass
        elif choise==4:
            break
        else:
            print("Please choise correct vaeriant:")







