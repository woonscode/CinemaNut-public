# SMU Module IS213 Enterprise Solution Development School Project
G07T08: CinemaNut
Members: James Tee, Jaye Brianna Yap, Kevan Oktavio, Timothy Phua Chia Hoe, Yong Woon Hao

## Description
This school project is to consolidate what we have learnt throughout the module, specifically containerization and messaging architecture.

**Technologies involved:**
- Python Flask
- Node.js Express
- AWS DynamoDB
- Amazon MQ (RabbitMQ)
- Docker (with docker-compose)
- Kong API Gateway

**Notes:**
**- All sensitive information (AWS credentials and External API Keys) have been removed for security reasons**
- Solution should be run on WAMPServer on http://localhost for Cookies.js (our session handling feature) to work

**Configuration:**
1. On executing the command docker-compose up -d, db_setup container will be executed that sets up all DynamoDB Tables and the admin user with username "woons", Amazon MQ will also be fully set-up with exchanges and queues
2. Go to http://localhost:1337, the Konga GUI to set-up your personal Konga admin user credentials
3. Set up connection with Type default, Name: default & Kong Admin URL: http://kong:8001
4. Go to Snapshots on the left panel and click Import From File -> choose import kong_config_to_import.json, the Kong configuration file, in the root folder of CinemaNut
5. Click on Details on the newly imported kong config file with name production_v2
6. Click on Restore and select all objects (NOTE: DUE TO A KONGA BUG, THIS STEP HAS TO BE DONE MULTIPLE TIMES TO FULLY IMPORT ALL CONFIGURATION)
7. Due to another Konga bug where although the API Key Auth can be saved when taking a Snapshot, there is an error when importing, the API Key has to be manually keyed in for the consumer with username admin -> go to Credentials -> API Key and manually set the key as "woons"

**Credentials:**
Website Admin User
Username: woons
Password: esdadmin