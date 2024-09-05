# from console.console import main

# if __name__=="__main__":
#     main()

from flask import Flask, request, jsonify
from config.connect_postgres import connect_to_database
from flight import flight_postgres
from booking import booking_postgress

app = Flask(__name__)
@app.route('/flight', methods=['POST'])
def get_save_flight():
    flight_details = request.json
    try:
       conn = connect_to_database()
       flight_postgres.save_flight_details(flight_details, conn)
       return jsonify({"message": "Flight added successfully"}), 201
    except Exception as e:
        print( f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug = True, port = 5010 )
    app.run(debug = True, port = 5010 )



app = Flask(__name__)
@app.route('/flight', methods=['POST'])
def get_save_booking():
    booking_details = request.json
    try:
       conn = connect_to_database()
       get_save_booking(booking_details, conn)
       return jsonify({"message": "Booking added successfully"}), 201
    except Exception as e:
        print( f"Error: {e}")
        return jsonify({"ERROR": str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug = True, port = 5010 )
    app.run(debug = True, port = 5010 )



# app = Flask(__name__)
    
# @app.route('/flight/<int:flight_id>', methods =["GET"])
# def get_find_flight_by_id():
#     flight_id = request.args.get('flight_id')
#     try:
#         conn = connect_to_database()
#         result = get_find_flight_by_id(flight_id,conn)
#         if result:
#             return jsonify({"flight": result, "message": "Find flight by id successfully"}), 200
#         else:
#             return jsonify({"message": "Flight not found"}), 404
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({"ERROR": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5010)


    # @app.route('/find-flight', methods=['GET'])
# def find_flight():
#     flight_id = request.args.get('flight_id')  # URL'den flight_id parametresini alıyoruz
    
#     if not flight_id:
#         return jsonify({"error": "Flight ID is required"}), 400
    
#     flight, error = find_flight(flight_id)
    
#     if error:
#         return jsonify({"error": f"Database error: {error}"}), 500
    
#     if flight:
#         return jsonify({"flight": flight}), 200  # Uçuş bulunduysa JSON döndür
#     else:
#         return jsonify({"error": "Flight not found"}), 404  # Uçuş bulunamadıysa hata döndür

# app = Flask(__name__)
# @app.route('/delete_flight', methods= ['DELETE'])
# def delete_flight(flight_id)
#     conn = get_database_connection ()
#     cursor = conn.cursor ()
#     try :
#         cursor.execute("""
#         SELECT COUNT (*) FROM flights
#         WHERE id = %s;
#         """,(flight_id,))
#         result = cursor.fetchone()
#         if result and result[0] > 0:
#             cursor.execute(""""
#             DELETE FROM flights
#             WHERE id = %s;
#             """, (flight_id,))
#             conn.commit()
#             return jsonify = {'message': f'Flight ID {flight_id} succesfully deleted.'}200
#         else:
#             return jsonify = {'message': 'Flight ID not found.'}404

#     except Exception as e:
#         conn.rollback()
#         return jsonify = {'message':f'Error:{e}'}500


#     finally:
#         cursor.close()
#         conn.close()


# from flight import get_find_flight_by_id as get_flight_from_db

# app = Flask(__name__)

# @app.route("/flight/<int:flight_id>", methods=["GET"])  # flight_id URL'den alınır
# def get_find_flight_by_id(flight_id):
#     try:
#         conn = connect_to_database()
#         result = get_flight_from_db(flight_id, conn)  # Doğru funksiya çağırışı
#         if result:
#             return jsonify({"flight": result, "message": "Find flight by ID successfully"}), 200
#         else:
#             return jsonify({"message": "Flight not found"}), 404
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({"ERROR": str(e)}), 400
#     finally:
#         if conn:
#             conn.close()

# if __name__ == '__main__':
#     app.run(debug=True, port=5010)




# app = Flask(__name__)
# from flight import find_flight_by_id as get_flight_from_db

# @app.route("/flight/<int:flight_id>", methods=["GET"])
# def get_find_flight_by_id(flight_id):
#     try:
#         conn = connect_to_database()
#         if conn is None:
#             return jsonify({"message": "Database connection failed"}), 500

#         result = get_flight_from_db(flight_id, conn)
#         if result:
#             return jsonify({"flight": result, "message": "Flight found successfully"}), 200
#         else:
#             return jsonify({"message": "Flight not found"}), 404
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({"ERROR": str(e)}), 400
#     finally:
#         if conn:
#             conn.close()

# if __name__ == '__main__':
#     app.run(debug=True, port=5010)

# from flight import flights_postgres_delete_flight

# app = Flask(__name__)

# @app.route('/flight/<int:flight_id>', methods=['DELETE'])
# def delete_flight(flight_id):
#     conn = connect_to_database()
#     flight_details = request.json  
#     try:
#         flights_postgres_delete_flight(flight_id, conn)

#         return jsonify({'message': f'Flight ID {flight_id} successfully deleted.'}), 200
#     except Exception as e:
#         conn.rollback()
#         return jsonify({'message': f'Error: {e}'}), 500
#     finally:
#         conn.close()  

# if __name__ == '_main_':
#     app.run(debug=True)