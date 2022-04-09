from flask import Flask, jsonify
from flask_cors import CORS
from mq_publisher import MessageSender
from invokes import invoke_http
from datetime import datetime
import os
import json

broker_id = os.environ.get("BROKER_ID")
mq_user = os.environ.get("MQ_USER")
mq_password = os.environ.get("MQ_PASSWORD")
region = "ap-southeast-1"

app = Flask(__name__)
CORS(app)

movie_local_url = os.environ.get("movie_local_url")
movie_external_url = os.environ.get("movie_external_url")

#Movie ID received from GET
@app.route("/manage_movie/<string:movie_id>")
def manage_movie(movie_id):   
    # Use movie_id as input to the 2 microservices
    response = process_manage_movie(movie_id)
    message = {"log_type": "movie", "description": "movie_id " + movie_id + " managed."}
    send_msg(message)
    
    return jsonify(response), response["code"]


# Retrieve info of <movie_id> from both local database and external API
def process_manage_movie(movie_id):
    # Invoke movie_local microservice to get result from internal database
    movie_local_result = invoke_http(f"{movie_local_url}/{movie_id}")

    # Invoke movie_external microservice to get result from external API
    movie_external_result = invoke_http(f"{movie_external_url}/title/{movie_id}/details")

    response = {"code": 200, "external_data": movie_external_result}

    # Add internal data if it exists
    if movie_local_result["code"] == 200:
        response["internal_data"] = movie_local_result["data"]["user_data"]["M"]
        
    # Return movie_local, movie_external data
    return response

def send_msg(message):
    # Initialize Message Sender client which creates a connection and channel for sending messages
    message_sender = MessageSender(broker_id, mq_user, mq_password, region)

    # Gets current datetime
    dtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message["datetime"] = dtime
    formatted_message = json.dumps(message)

    # Send a message to the queue
    message_sender.send_message(exchange="cinemanut", routing_key="activity_log", body=formatted_message)

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4005, debug=True)

