FROM python:3-slim
WORKDIR /usr/src/app
COPY activity_log_reqs.txt ./
RUN python -m pip install --no-cache-dir -r activity_log_reqs.txt
COPY activity_log.py ./
CMD [ "python", "activity_log.py" ]
