FROM python:3-slim
WORKDIR /usr/src/app
COPY mq_publisher_reqs.txt playlist_reqs.txt ./
RUN python -m pip install --no-cache-dir -r mq_publisher_reqs.txt -r playlist_reqs.txt
COPY mq_setup.py mq_publisher.py playlist.py ./
CMD [ "python", "playlist.py" ]