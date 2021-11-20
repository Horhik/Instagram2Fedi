FROM python:3.9

RUN pip install instaloader
RUN pip install Mastodon.py
RUN pip install colorama

COPY . /app
WORKDIR /app


ENTRYPOINT ["python", "/app/src/main.py"]

