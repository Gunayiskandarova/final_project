# (
# id integer primary key,
# flight_number integer, 
# date_flight varchar, 
# time_flight varchar, 
# origin varchar, 
# destination varchar, 
# seats integer
# );


# drop table flight;



# create table booking
# (
# id integer,
# passenger_name varchar,
# flight_id integer,
# FOREIGN KEY (flight_id) REFERENCES flight(id),
# seat_count integer
# );

# select * from flight;
# select * from booking;
# select *  from  flight
# full join booking on flight.id = booking.flight_id;