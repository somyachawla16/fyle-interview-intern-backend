FROM python:3.8.18

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=core/server.py

CMD ["bash","run.sh"]