FROM python

RUN pip install instabot
RUN pip3 install Mastodon.py

COPY . /app
WORKDIR /app

ENTRYPOINT [ "python", "/app/__init__.py", "innubis"]
