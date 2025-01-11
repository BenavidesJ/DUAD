from db_client import DBClient
from flask import Flask, request, jsonify
from src.queries import queries
from src.utils import build_filter_query

app = Flask(__name__)
db_client = DBClient('lyfter_car_rental','postgres', 1234, 'localhost')

# Crear un usuario nuevo
@app.route('/users', methods=['POST'])
def create_user():
    try:
        body_data = request.json
        name = body_data["name"]
        email = body_data["email"]
        username = body_data["username"]
        password = body_data["password"]
        date_of_birth = body_data["date_of_birth"]
        account_status = body_data["account_status"]

        db_client.execute_query(queries.create_user, name, email, username, password, date_of_birth, account_status)
        
        return jsonify({"message": "User created"}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
    
# Crear un automóvil nuevo
@app.route("/cars", methods=["POST"])
def create_car():
    try:
        body_data = request.json
        brand = body_data["brand"]
        model = body_data["model"]
        year_of_manufacture = body_data["year_of_manufacture"]
        car_status = body_data["car_status"]

        db_client.execute_query(queries.create_car, brand, model, year_of_manufacture, car_status)
        return jsonify({"message": "Car created"}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
    
# Crear un alquiler nuevo
@app.route("/rentals", methods=["POST"])
def create_rental():
    try:
        body_data = request.json
        user_id = body_data["user_id"]
        car_id = body_data["car_id"]
        rental_date = body_data["rental_date"]
        return_date = body_data["return_date"]
        status = body_data["status"]

        db_client.execute_query(queries.create_rental, user_id, car_id, rental_date, return_date, status)
        return jsonify({"message": "Rental created"}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
    
# Cambiar el estado de un automóvil
@app.route("/cars/<int:car_id>/status", methods=["PATCH"])
def update_car_status(car_id):
    try:
        body_data = request.json
        new_status = body_data["car_status"]
        
        rows_updated = db_client.execute_query(queries.update_car_status, new_status, car_id)

        if rows_updated > 0:
            return jsonify({"message": "Car status updated successfully"}), 200
        else:
            return jsonify({"error": f"Car with id {car_id} not found"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    

# Cambiar el estado de un usuario
@app.route("/users/<int:user_id>/status", methods=["PATCH"])
def update_user_status(user_id):
    try:
        body_data = request.json
        new_status = body_data["account_status"]
   
        rows_updated = db_client.execute_query(queries.update_user_account_status, new_status, user_id)

        if rows_updated > 0:
            return jsonify({"message": "User status updated successfully"}), 200
        else:
            return jsonify({"error": f"User with id {user_id} not found"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# Completar un alquiler
@app.route("/rentals/<int:rental_id>/complete", methods=["PATCH"])
def complete_rental(rental_id):
    try:   
        rows_updated = db_client.execute_query(queries.complete_rental, rental_id)

        if rows_updated > 0:
            return jsonify({"message": "Rental completed successfully"}), 200
        else:
            return jsonify({"error": f"Rental with id {rental_id} not found or already completed"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# Cambiar el estado de un alquiler
@app.route("/rentals/<int:rental_id>/status", methods=["PATCH"])
def update_rental_status(rental_id):
    try:
        body_data = request.json
        new_status = body_data["status"]

        rows_updated = db_client.execute_query(queries.update_rental_status, new_status, rental_id)

        if rows_updated > 0:
            return jsonify({"message": "Rental status updated successfully"}), 200
        else:
            return jsonify({"error": f"Rental with id {rental_id} not found"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# Flagear un usuario como moroso
@app.route("/users/<int:user_id>/late_payment", methods=["PATCH"])
def flag_user_moroso(user_id):
    try:
        rows_updated = db_client.execute_query(queries.flag_user_late_payment, user_id)

        if rows_updated > 0:
            return jsonify({"message": "User flagged as late payment successfully"}), 200
        else:
            return jsonify({"error": f"User with id {user_id} not found"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
# Listar usuarios
@app.route("/users", methods=["GET"])
def list_users():
    try:
        query_params = request.args.to_dict()
        where_clause, values = build_filter_query(query_params)

        query = f"{queries.select_user} {where_clause};"
        users_data = db_client.execute_query(query, *values)

        return jsonify({"data": users_data}), 200

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# Listar todos los carros
@app.route("/cars", methods=["GET"])
def list_cars():
    try:
        query_params = request.args.to_dict()
        where_clause, values = build_filter_query(query_params)

        query = f"{queries.select_car} {where_clause};"
        cars_data = db_client.execute_query(query, *values)

        return jsonify({"data": cars_data}), 200

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# Listar todos los alquileres
@app.route("/rentals", methods=["GET"])
def list_rentals():
    try:
        query_params = request.args.to_dict()
        where_clause, values = build_filter_query(query_params)

        query = f"{queries.select_rental} {where_clause};"
        rentals_data = db_client.execute_query(query, *values)

        return jsonify({"data": rentals_data}), 200

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    
     
if __name__ == "__main__":
    app.run(host="localhost", debug=True)