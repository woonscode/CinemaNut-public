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
CORS(app)

# Write to DynamoDB table
def write_to_db(input):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    # Convert to string as DynamoDB does not accept int format
    user_name = input["user_name"]
    movie_id = str(input["movie_id"])
    watched = input["watched"]
    rating = str(input["rating"])
    review = input["review"]

    db_response = db.put_item(
    TableName='movie',
    Item={
        'movie_id': {
            'N': movie_id,
        },
        'user_data': {
            'M': {
                user_name: 
                    { 'M':
                        {
                            'watched': {'BOOL': watched},
                            'rating': {'N': rating},
                            'review': {'S': review}
                        }
                    }
                }
        }
    },
    ReturnValues='ALL_OLD',
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
    movie_id = str(input["movie_id"])
    watched = input["watched"]
    rating = str(input["rating"])
    review = input["review"]

    db_response = db.update_item(
        TableName='movie',
        Key={
            'movie_id': {
                'N': movie_id,
            },
        },
        ExpressionAttributeValues={
            ':ud': 
                    { 'M':
                        {
                            'watched': {'BOOL': watched},
                            'rating': {'N': rating},
                            'review': {'S': review}
                        }
                    }
            
        },
        UpdateExpression=f'SET user_data.{user_name} = :ud',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        return {"code": 500, "message": "Failed to write to database."}
    else:
        return {"code": 200, "message": "Database write success, record updated."}

def read_db(movie_id):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    db_response = db.get_item(
    TableName='movie',
    Key={
        'movie_id': {
            'N': movie_id,
            }
        }
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when getting movie records."}
    elif "Item" in db_response:
        items = db_response["Item"]
        return {"code": 200, "data": items}
    else:
        return {"code": 404, "message": "Record not found."}

def delete_from_db(movie_id, user_name):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    # Since table has a dictionary of dictionaries as an attribute, need to update instead of deleting entire record
    db_response = db.update_item(
        TableName='movie',
        Key={
            'movie_id': {
                'N': movie_id,
            },
        },
        ReturnValues='UPDATED_OLD',
        UpdateExpression=f'REMOVE user_data.{user_name}',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # Check if user_data is empty, if yes, delete entire record in table
    read_response = read_db(movie_id)["data"]["user_data"]["M"]
    if not read_response:
        table_response = db.delete_item(
            TableName='movie',
            Key={'movie_id': {'N': movie_id,}},
        )

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when deleting user movie record."}
    elif "Attributes" in db_response:
        return {"code": 200, "message": "User movie record successfully deleted."}
    else:
        return {"code": 404, "message": "User movie record not found."}

def send_msg(message):
    # Initialize Message Sender client which creates a connection and channel for sending messages
    message_sender = MessageSender(broker_id, mq_user, mq_password, region)

    # Gets current datetime
    dtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message["datetime"] = dtime
    formatted_message = json.dumps(message)

    # Send a message to the queue
    message_sender.send_message(exchange="cinemanut", routing_key="activity_log", body=formatted_message)

# Get user movie details for movie based on movie_id
# DynamoDB does not accept int format, use string for movie_id
@app.route("/movie_local/<string:movie_id>")
def get_movie_details(movie_id):
    response = read_db(movie_id)
    return jsonify(response), response["code"]

# Adds or updates status, rating and review
# DynamoDB does not accept int format, use string for movie_id
# PRE-POPULATE FRONTEND FORM DATA AND RESEND ON UPDATE OR ELSE THE RATING/REVIEW WILL BE OVERWRITTEN
@app.route("/movie_local/<string:movie_id>", methods=['POST', 'PUT'])
def add_or_update_movie_details(movie_id):
    if request.is_json:
        data = request.get_json()

        data["movie_id"] = movie_id

        read_response = read_db(movie_id)
        read_response_code = read_response["code"]

        # If read_response status code == 200, movie_id already exists, should update to add record
        if read_response_code == 200:
            response = update_db(data)

            if response["code"] == 200:
                # Send message to activity_log
                message = {"log_type": "movie", "description": "movie_id " + movie_id + " user record updated."}
                send_msg(message)
        else:
            response = write_to_db(data)

            if response["code"] == 201:
                # Send message to activity_log
                message = {"log_type": "movie", "description": "movie_id " + movie_id + " user record added."}
                send_msg(message)
            
    else:
        response = {"code": 400, "message": "Invalid movie ID."}

    # If response returns code 200, it means it is an update. If response returns code 201, it means it is a new record.
    return jsonify(response), response["code"]

# Delete record based on movie_id
# DynamoDB does not accept int format, use string for movie_id
@app.route("/movie_local/<string:movie_id>/<string:user_name>", methods=['DELETE'])
def delete_user_movie_record(movie_id, user_name):
    response = delete_from_db(movie_id, user_name)

    # Send message to activity_log
    if response["code"] == 200:
        message = {"log_type": "movie", "description": "movie_id " + movie_id + " user record deleted."}
        send_msg(message)

    return jsonify(response), response["code"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4003, debug=True)



 