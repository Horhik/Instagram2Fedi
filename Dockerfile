FROM python

RUN pip install instabot
RUN pip3 install Mastodon.py

WORKDIR /app
COPY . /app

ENTRYPOINT [ "python", "/app/__init__.py", "innubis"]
