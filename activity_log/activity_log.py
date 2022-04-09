from flask import Flask, jsonify
from flask_cors import CORS
import boto3
import os
access_key = os.environ.get("ACCESS_KEY")
secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
region = "ap-southeast-1"

# Initialise Flask app
app = Flask(__name__)
CORS(app)

def delete_from_db(record_id):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    db_response = db.delete_item(
    TableName='activity_log',
    Key={'record_id': {'N': record_id,}},
    ReturnValues='ALL_OLD',
    )
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        return {"code": 500, "message": "Error when deleting activity log record."}
    else:
        return {"code": 200, "message": "Activity log record successfully deleted."}

# Get all activity_logs from database table
@app.route("/log")
def get_all_logs():
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)

    db_response = db.scan(TableName='activity_log')
    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        response = {"code": 500, "message": "Error when getting activity log records."}

    else:
        all_items = db_response["Items"]
        # Extend response as DynamoDB limitation of 1MB per scan
        while 'LastEvaluatedKey' in db_response:
            db_response = db.scan(ExclusiveStartKey=db_response['LastEvaluatedKey'])
            all_items.extend(db_response['Items'])

        response = {"code": 200, "data": all_items}
    return jsonify(response), response["code"]

# Delete specific record from activity log based on record_id
# DynamoDB does not accept int format, use string for record_id
@app.route("/log/<string:record_id>", methods=["DELETE"])
def delete_log(record_id):
    response = delete_from_db(record_id)
    return jsonify(response), response["code"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4001)