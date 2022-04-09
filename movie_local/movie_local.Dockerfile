FROM python:3-slim
WORKDIR /usr/src/app
COPY movie_local_reqs.txt mq_publisher_reqs.txt ./
RUN python -m pip install --no-cache-dir -r movie_local_reqs.txt -r mq_publisher_reqs.txt
COPY mq_setup.py mq_publisher.py movie_local.py ./
CMD [ "python", "movie_local.py" ]
