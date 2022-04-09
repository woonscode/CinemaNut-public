FROM python:3-slim
WORKDIR /usr/src/app
COPY manage_movie_reqs.txt mq_publisher_reqs.txt ./
RUN python -m pip install --no-cache-dir -r manage_movie_reqs.txt -r mq_publisher_reqs.txt
COPY mq_setup.py mq_publisher.py invokes.py manage_movie.py ./
CMD [ "python", "manage_movie.py" ]
