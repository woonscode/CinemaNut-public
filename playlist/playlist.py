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
    
    user_name = input["user_name"]
    title = input["title"]
    caption = input["caption"]

    # Convert to string as DynamoDB does not accept int format
    playlist_id = str(get_record_id())

    db_response = db.put_item(
    TableName='playlist',
    Item={
        'playlist_id': {
            'N': playlist_id
        },
        'user_name': {
            'S': user_name
        },
        'title': {
            'S': title
        },
        'caption': {
            'S': caption
        }
    },
    ReturnValues='NONE',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        return {"code": 500, "message": "Failed to write to database."}
    else:
        return {"code": 201, "message": "Database write success, new record added."}

def get_record_id():
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)

    # Get all playlists
    db_response = db.scan(
    TableName='playlist',
    ProjectionExpression='playlist_id',
    )
    latest_record_id = 0
    items = db_response["Items"]
    # Extend response as DynamoDB limitation of 1MB per scan
    while 'LastEvaluatedKey' in db_response:
        db_response = db.scan(ExclusiveStartKey=db_response['LastEvaluatedKey'])
        items.extend(db_response['Items'])
    # Loop through all records to get latest playlist_id
    for item in items:
        item_record_id = int(item["playlist_id"]["N"])
        if item_record_id > latest_record_id:
            latest_record_id = item_record_id
    return latest_record_id + 1

def update_db(input):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    playlist_id = input["playlist_id"]
    movie_IDs = input["movie_IDs"]

    db_response = db.update_item(
    TableName='playlist',
    Key={
        'playlist_id': {
            'N': playlist_id
        },
    },
    ExpressionAttributeValues={
            ':mID': {'NS': movie_IDs},
        },
    UpdateExpression=f'ADD movie_IDs :mID',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    # return JSON
    if status_code not in range(200, 300):
        return {"code": 500, "message": "Failed to write to database."}
    else:
        return {"code": 200, "message": "Database write success, record updated."}

def read_db_by_id(playlist_id):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    db_response = db.get_item(
    TableName='playlist',
    Key={
        'playlist_id': {
            'N': playlist_id,
            }
        }
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when getting playlist records."}
    elif "Item" in db_response:
        item = db_response["Item"]
        return {"code": 200, "data": item}
    else:
        return {"code": 404, "message": "Record not found."}

def playlists_by_user(user_name):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)

    # Get all playlists
    db_response = db.scan(
    TableName='playlist',
    )
    items = db_response["Items"]
    # Extend response as DynamoDB limitation of 1MB per scan
    while 'LastEvaluatedKey' in db_response:
        db_response = db.scan(ExclusiveStartKey=db_response['LastEvaluatedKey'])
        items.extend(db_response['Items'])

    # If playlist user_name matches query user_name, append to playlist
    playlists = []
    for item in items:
        creator = item["user_name"]["S"]
        if creator == user_name:
            playlists.append(item)
    
    if not playlists:
        return {"code": 404, "message": "No playlists found."}

    return {"code": 200, "data": playlists}

def delete_from_db(playlist_id):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    
    db_response = db.delete_item(
        TableName='playlist',
        Key={'playlist_id': {'N': playlist_id}},
        ReturnValues='ALL_OLD',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when deleting playlist."}
    elif "Attributes" in db_response:
        return {"code": 200, "message": "Playlist successfully deleted."}
    else:
        return {"code": 404, "message": "Playlist not found."}

def send_msg(message):
    # Initialize Message Sender client which creates a connection and channel for sending messages
    message_sender = MessageSender(broker_id, mq_user, mq_password, region)

    # Gets current datetime
    dtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message["datetime"] = dtime
    formatted_message = json.dumps(message)

    # Send a message to the queue
    message_sender.send_message(exchange="cinemanut", routing_key="activity_log", body=formatted_message)

# Gets all playlists created by user_name
@app.route("/playlist/user/<string:user_name>")
def get_playlists_by_user(user_name):
    response = playlists_by_user(user_name)
    return jsonify(response), response["code"]

# Gets details for a specific playlist_id
# DynamoDB does not accept int format, use string for playlist_id
@app.route("/playlist/id/<string:playlist_id>")
def find_playlist_by_id(playlist_id):
    response = read_db_by_id(playlist_id)
    return jsonify(response), response["code"]

# Create new playlist
@app.route("/playlist", methods=['POST'])
def create_playlist():
    if request.is_json:
        data = request.get_json()
        response = write_to_db(data)

        if response["code"] == 201:
            # Send message to activity_log
            playlist_id = str(get_record_id() - 1)
            message = {"log_type": "playlist", "description": "Playlist " + playlist_id + " created."}
            send_msg(message)
    else:
        response = {"code": 400, "message": "Invalid data input."}

    return jsonify(response), response["code"]

# Add/Delete movie to existing playlist
# No duplicate values for movie_IDs
# DynamoDB does not accept int format, use string for playlist_id
@app.route("/playlist/<string:playlist_id>", methods=['PUT'])
def add_movie_to_playlist(playlist_id):
    if request.is_json:
        data = request.get_json()
        data["playlist_id"] = playlist_id

        # input playlist has to be a list of strings
        response = update_db(data)

        if response["code"] == 200:
            # Send message to activity_log
            message = {"log_type": "playlist", "description": "Playlist " + playlist_id + " updated."}
            send_msg(message)
    else:
        response = {"code": 400, "message": "Invalid data input."}

    return jsonify(response), response["code"]

# Delete playlist with playlist_id
# DynamoDB does not accept int format, use string for movie_id
@app.route("/playlist/<string:playlist_id>", methods=['DELETE'])
def delete_playlist(playlist_id):
    response = delete_from_db(playlist_id)
    
    if response["code"] == 200:
        # Send message to activity_log
        message = {"log_type": "playlist", "description": "Playlist " + playlist_id + " deleted."}
        send_msg(message)

    return jsonify(response), response["code"]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4002, debug=True)
