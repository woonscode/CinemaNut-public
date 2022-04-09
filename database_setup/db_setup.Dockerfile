FROM python:3-slim
WORKDIR /usr/src/app
COPY db_setup_reqs.txt ./
RUN python -m pip install --no-cache-dir -r db_setup_reqs.txt
COPY db_setup.py ./
CMD [ "python", "db_setup.py" ]
