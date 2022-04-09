FROM python:3-slim
WORKDIR /usr/src/app
COPY activity_log_consumer_reqs.txt ./
RUN python -m pip install --no-cache-dir -r activity_log_consumer_reqs.txt
COPY activity_log_consumer.py mq_setup.py ./
CMD [ "python", "activity_log_consumer.py" ]
