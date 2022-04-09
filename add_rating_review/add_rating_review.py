from flask import Flask, request, jsonify
from flask_cors import CORS
from invokes import invoke_http
import os
import json

app = Flask(__name__)
CORS(app)

movie_local_url = os.environ.get("movie_local_url")
user_url = os.environ.get("user_url")

# Add new movie details
@app.route("/add_rating_review/<string:movie_id>", methods=['POST'])
def add_rating_review(movie_id):
    if request.is_json:
        data = request.get_json()
        user_name = data["user_name"]

        # Invoke movie_local microservice to update movie_local table
        movie_local_result = invoke_http(f"{movie_local_url}/{movie_id}", method="POST", json=data)
        # Invoke user microservice to update user table
        user_result = invoke_http(f"{user_url}/add_movie_id/{user_name}/{movie_id}")

        if ((movie_local_result["code"] != 200) and (movie_local_result["code"] != 201)) or (user_result["code"] != 200):
            response = {"code": 500, "message": "Error adding new record."}
        else:
            response = {"code": 201, "message": "Record successfully added."}

    else:
        response = {"code": 400, "message": "Invalid input."}
    
    return jsonify(response), response["code"]

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4006, debug=True)

