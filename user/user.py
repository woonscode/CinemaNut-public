from flask import Flask, request, jsonify
from flask_cors import CORS
from mq_publisher import MessageSender
from datetime import datetime
import boto3
import os
import json

access_key = os.environ.get("ACCESS_KEY")
secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
region = "ap-southeast-1"
broker_id = os.environ.get("BROKER_ID")
mq_user = os.environ.get("MQ_USER")
mq_password = os.environ.get("MQ_PASSWORD")

# Initialise Flask app
app = Flask(__name__)
cors = CORS(app)

# Write to DynamoDB table
def write_to_db(input):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    user_name = input["user_name"]
    password = input["password"]
    full_name = input["full_name"]
    email = input["email"]

    db_response = db.put_item(
    TableName='user',
    Item={
        'user_name': {
            'S': user_name
        },
        'password': {
            'S': password
        },
        'full_name': {
            'S': full_name
        },
        'email': {
            'S': email
        },
    },
    ReturnValues='NONE',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        return {"code": 500, "message": "Failed to write to database."}
    else:
        return {"code": 201, "message": "Database write success, new record added."}

def update_db(input):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    # Convert to string as DynamoDB does not accept int format
    user_name = input["user_name"]
    password = input["password"]
    full_name = input["full_name"]
    email = input["email"]

    db_response = db.update_item(
        TableName='user',
        Key={
            'user_name': {
                'S': user_name,
            },
        },
        ExpressionAttributeValues={
            ':p': {'S': password},
            ':fn': {'S': full_name},
            ':e': {'S': email},
        },
        UpdateExpression='SET password = :p, full_name = :fn, email = :e',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        return {"code": 500, "message": "Failed to write to database."}
    else:
        return {"code": 200, "message": "Database write success, record updated."}

def read_db(user_name):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    db_response = db.get_item(
    TableName='user',
    Key={
        'user_name': {
            'S': user_name,
            }
        }
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when getting user records."}
    elif "Item" in db_response:
        item = db_response["Item"]
        return {"code": 200, "data": item}
    else:
        return {"code": 404, "message": "Record not found."}

def delete_from_db(user_name):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    db_response = db.delete_item(
        TableName='user',
        Key={'user_name': {'S': user_name,}},
        ReturnValues='ALL_OLD',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when deleting user."}
    elif "Attributes" in db_response:
        return {"code": 200, "message": "User successfully deleted."}
    else:
        return {"code": 404, "message": "User not found."}

def send_msg(message):
    # Initialize Message Sender client which creates a connection and channel for sending messages
    message_sender = MessageSender(broker_id, mq_user, mq_password, region)

    # Gets current datetime
    dtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message["datetime"] = dtime
    formatted_message = json.dumps(message)

    # Send a message to the queue
    message_sender.send_message(exchange="cinemanut", routing_key="activity_log", body=formatted_message)

# User registration
@app.route("/user/register", methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()

        user_name = data['user_name']
        # Check if exists in database
        read_response = read_db(user_name)
        if read_response["code"] == 200:
            response = {"code": 500, "message": "user_name has already been taken."}
        elif read_response["code"] == 404:
            response = write_to_db(data)
            if response["code"] == 201:
                # Send message to activity_log
                message = {"log_type": "user", "description": "User " + user_name + " created."}
                send_msg(message)
    else:
        response = {"code": 400, "message": "Invalid data input."}

    return jsonify(response), response["code"]

# User authentication and login
@app.route("/user/login", methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()

        user_name = data["user_name"]
        password = data["password"]

        # Check if exists in database
        read_response = read_db(user_name)

        # Authentication
        # If user_name exists,
        if read_response["code"] == 200:
            read_data = read_response["data"]

            # If password matches
            if read_data["password"]["S"] == password:
                response = {"code": 200, "message": "Successfully authenticated."}
            else:
                response = {"code": 401, "message": "Invalid password."}

        # User not found or error
        else:
            response = read_response

    else:
        response = {"code": 400, "message": "Invalid data input."}

    return jsonify(response), response["code"]    

# Get user profile details
@app.route("/user/<string:user_name>")
def get_details(user_name):
    # Read from database
    if isinstance(user_name, str):
        response = read_db(user_name)
    else:
        response = {"code": 400, "message": "user_name should be a string."}

    return jsonify(response), response["code"]

# Update profile details
# PRE-POPULATE FRONTEND FORM DATA AND RESEND ON UPDATE OR ELSE THE DETAILS WILL BE OVERWRITTEN
@app.route("/user/<string:user_name>", methods=['PUT'])
def update_profile(user_name):
    if request.is_json:
        data = request.get_json()

        data["user_name"] = user_name

        # Check if exists in database
        read_response = read_db(user_name)

        # Authentication
        # If user_name exists, proceed to update
        if read_response["code"] == 200:
            response = update_db(data)

            if response["code"] == 200:
                # Send message to activity_log
                message = {"log_type": "user", "description": "User " + user_name + " profile updated."}
                send_msg(message)

        # User not found or error
        else:
            response = read_response

    else:
        response = {"code": 400, "message": "Invalid data input."}

    return jsonify(response), response["code"]

# Add movie_id to user details
@app.route("/user/add_movie_id/<string:user_name>/<string:movie_id>")
def add_movie_id(user_name, movie_id):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    # Add movie_id to user's existing record
    movie_id_list = [movie_id]
    db_response = db.update_item(
        TableName='user',
        Key={
            'user_name': {
                'S': user_name,
            },
        },
        ExpressionAttributeValues={
            ':mID': {'NS': movie_id_list},
        },
        UpdateExpression=f'ADD movie_IDs :mID',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        response = {"code": 500, "message": "Failed to write to database."}
    else:
        response = {"code": 200, "message": "Database write success, record updated."}

        # Send message to activity_log
        message = {"log_type": "user", "description": "User " + user_name + " movie list updated."}
        send_msg(message)

    return jsonify(response), response["code"]

@app.route("/user/<string:user_name>", methods=['DELETE'])
def delete_account(user_name):
    response = delete_from_db(user_name)
    
    if response["code"] == 200:
        # Send message to activity_log
        message = {"log_type": "user", "description": "User " + user_name + " deleted."}
        send_msg(message)

    return jsonify(response), response["code"]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
