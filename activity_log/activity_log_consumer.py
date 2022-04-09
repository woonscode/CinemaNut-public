from mq_setup import BasicPikaClient
import os
import boto3
import json

access_key = os.environ.get("ACCESS_KEY")
secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
broker_id = os.environ.get("BROKER_ID")
mq_user = os.environ.get("MQ_USER")
mq_password = os.environ.get("MQ_PASSWORD")
region = "ap-southeast-1"

# Initialise AmazonMQ client
class MessageReceiver(BasicPikaClient):
    def start_loop(self, queue_name):
        self.check_setup()
        channel = self.connection.channel()
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

# Callback function for message
def callback(channel, method, properties, body):
    write_to_db(json.loads(body))

def get_record_id(client):
    db_response = client.scan(
    TableName='activity_log',
    ProjectionExpression='record_id',
    )
    latest_record_id = 0
    items = db_response["Items"]
    # Extend response as DynamoDB limitation of 1MB per scan
    while 'LastEvaluatedKey' in db_response:
        db_response = client.scan(ExclusiveStartKey=db_response['LastEvaluatedKey'])
        items.extend(db_response['Items'])
    # Loop through all records to get latest record_id
    for item in items:
        item_record_id = int(item["record_id"]["N"])
        if item_record_id > latest_record_id:
            latest_record_id = item_record_id
    return latest_record_id + 1

# Writing to DynamoDB table upon consuming message
def write_to_db(message):
    # Initialise DynamoDB client
    db = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
    # Get last record_id in table + 1, need to convert to string as DynamoDB does not accept int format
    record_id = str(get_record_id(db))
    log_type = message["log_type"]
    datetime = message["datetime"]
    description = message["description"]

    db_response = db.put_item(
    TableName='activity_log',
    Item={
        'record_id': {
            'N': record_id,
        },
        'log_type': {
            'S': log_type,
        },
        'datetime': {
            'S': datetime,
        },
        'description': {
            'S': description,
        }
    },
    ReturnValues='NONE',
    )

    status_code = db_response["ResponseMetadata"]["HTTPStatusCode"]

    if status_code not in range(200, 300):
        print("Error when writing to database")
    else:
        print(f"Message received from Amazon MQ with body: {message}")

if __name__ == "__main__":
    # Create MessageReceiver to consume messages
    message_receiver = MessageReceiver(broker_id, mq_user, mq_password, region)
    # Start loop to continuously check queue for messages
    message_receiver.start_loop("activity_log")