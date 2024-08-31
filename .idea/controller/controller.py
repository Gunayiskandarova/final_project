from flask import Flask, request, jsonify
from config.connect_postgres import connect_to_database
from flight import flight_postgres

app = Flask(__name__)
@app.route('/flight',methods=['POST'])
def get_save_flight():
    flight_details = request.json
    try:
       conn= connect_to_database()
       flight_postgres.save_flight_details(flight_details, conn)
       return jsonify({"message": "Flight added successfully"}), 201
    except Exception as e:
        print ( f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400
if __name__ == "__main__":
    app.run(debug = True, port = 5010 )