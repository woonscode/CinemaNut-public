FROM python:3-slim
WORKDIR /usr/src/app
COPY mq_publisher_reqs.txt template_publisher_reqs.txt ./
RUN python -m pip install --no-cache-dir -r mq_publisher_reqs.txt -r template_publisher_reqs.txt
COPY template_publisher.py mq_publisher.py mq_setup.py ./
CMD [ "python", "template_publisher.py" ]
