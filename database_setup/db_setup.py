import boto3
import os
import time

access_key = os.environ.get("ACCESS_KEY")
secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
region = "ap-southeast-1"

# To be run once to set up DynamoDB database only and then the container will be exited

# Initialise DynamoDB Client
client = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)

# Create Activity Log Table
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'record_id',
            'AttributeType': 'N',
        },
    ],
    TableName='activity_log',
    KeySchema=[
        {
            'AttributeName': 'record_id',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)

# Create User Table
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'user_name',
            'AttributeType': 'S',
        },
    ],
    TableName='user',
    KeySchema=[
        {
            'AttributeName': 'user_name',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)

# Create Movie table
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'movie_id',
            'AttributeType': 'N',
        },
    ],
    TableName='movie',
    KeySchema=[
        {
            'AttributeName': 'movie_id',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)

# Create Playlist Table
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'playlist_id',
            'AttributeType': 'N',
        },
    ],
    TableName='playlist',
    KeySchema=[
        {
            'AttributeName': 'playlist_id',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)

# Wait 10 seconds for table to be created as DynamoDB create table is an asynchronous function
time.sleep(10)

# Set up admin user credentials
admin_credentials = {
    "user_name": "woons", 
    "password": "esdadmin", 
    "full_name": "Yong Woon Hao", 
    "email": "whyong.2020@scis.smu.edu.sg"
}

# Create admin user
response_create_user = client.put_item(
    TableName='user',
    Item={
        'user_name': {
            'S': admin_credentials['user_name']
        },
        'password': {
            'S': admin_credentials['password']
        },
        'full_name': {
            'S': admin_credentials['full_name']
        },
        'email': {
            'S': admin_credentials['email']
        },
    },
    ReturnValues='NONE',
)