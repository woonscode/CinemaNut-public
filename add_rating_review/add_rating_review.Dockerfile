FROM python:3-slim
WORKDIR /usr/src/app
COPY add_rating_review_reqs.txt ./
RUN python -m pip install --no-cache-dir -r add_rating_review_reqs.txt
COPY invokes.py add_rating_review.py ./
CMD [ "python", "add_rating_review.py" ]
