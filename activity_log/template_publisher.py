from mq_publisher import MessageSender
from datetime import datetime
import os
import json
broker_id = os.environ.get("BROKER_ID")
mq_user = os.environ.get("MQ_USER")
mq_password = os.environ.get("MQ_PASSWORD")
region = "ap-southeast-1"

# Initialize Message Sender which creates a connection and channel for sending messages
message_sender = MessageSender(broker_id, mq_user, mq_password, region)
# Gets current datetime
dtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
tester = {"log_type": "playlist", "datetime": dtime, "description": "Playlist 'James is a clown' has been created."}
message = json.dumps(tester)
# Send a message to the queue
message_sender.send_message(exchange="cinemanut", routing_key="activity_log", body=message)

## Publisher Dockerfile to include mq_setup.py and mq_publisher.py