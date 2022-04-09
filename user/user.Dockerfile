FROM python:3-slim
WORKDIR /usr/src/app
COPY mq_publisher_reqs.txt user_reqs.txt ./
RUN python -m pip install --no-cache-dir -r mq_publisher_reqs.txt -r user_reqs.txt
COPY mq_setup.py mq_publisher.py user.py ./
CMD [ "python", "user.py" ]