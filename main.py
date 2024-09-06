from console.console import main

if __name__=="__main__":
    from config.connect_postgres import connect_to_database
from flask import Flask, request, jsonify
from flight.flight_postgres import find_flight_by_id, save_flight_details, find_all_flights, delete_flight
from booking.booking_postgress import save_booking_details, find_booking_by_id, find_all_booking, delete_booking
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

conn = connect_to_database()

@app.route('/flight', methods=['POST'])
def save_flight():
    flight_details = request.json
    try:
        save_flight_details(flight_details, conn)
        return jsonify({"message": "Flight added successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400


@app.route('/booking', methods=['POST'])
def save_booking():
    booking_details = request.json
    try:
        print(booking_details)
        save_booking_details(booking_details, conn)
        return jsonify({"message": "Booking added successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400


@app.route('/flight/<int:flight_id>', methods=["GET"])
def get_flight_by_id(flight_id):
    try:
        result = find_flight_by_id(flight_id, conn)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": "Flight not found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400


@app.route('/booking/<int:booking_id>', methods=["GET"])
def get_booking_by_id(booking_id):
    try:
        result = find_booking_by_id(booking_id, conn)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": "booking not found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400

@app.route('/flight', methods=["GET"])
def find_flight():
    try:
        flights = find_all_flights(conn)
        return jsonify(flights), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400


@app.route('/flight/<int:flight_id>', methods=['DELETE'])
def delete_flight_net(flight_id):  
    try:
        delete_flight(flight_id, conn)
        return jsonify({'message': f'Flight ID {flight_id} successfully deleted.'}), 200
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return jsonify({'message': f'Error: {e}'}), 500
app = Flask(__name__)

@app.route('/booking', methods=["GET"])
def find_all_booking(conn):
  try:
    conn = connect_to_database()
    bookings = find_all_booking(conn) 
    conn.close() 
    return jsonify(bookings), 200 
  except Exception as e:
    print(f"Error: {e}")
    return jsonify({"ERROR": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)