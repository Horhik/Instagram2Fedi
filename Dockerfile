FROM python:3.9

RUN pip install instaloader
RUN pip install Mastodon.py
RUN pip install colorama

COPY . /app
WORKDIR /app

ENV USE_DOCKER=1
ENV YOUR_CONTAINER_NAME="$YOUR_CONTAINER_NAME"
ENV I2M_INSTAGRAM_USER="$I2M_INSTAGRAM_USER"
ENV I2M_INSTANCE="$I2M_INSTANCE"
ENV I2M_TOKEN="$I2M_TOKEN"


ENV I2M_CHECK_INTERVAL "$I2M_CHECK_INTERVAL"
ENV I2M_POST_INTERVAL "$I2M_POST_INTERVAL"
ENV I2M_USE_MASTODON "$I2M_USE_MASTODON"
ENV I2M_FETCH_COUNT "$I2M_FETCH_COUNT"



#ENTRYPOINT ["python", "/app/src/main.py", "--instagram-user", I2M_INSTAGRAM_USER, "--instance",  I2M_INSTANCE, "--token", I2M_TOKEN, "--check-interval", I2M_CHECK_INTERVAL, "--post-interval", I2M_POST_INTERVAL, "--fetch-count", I2M_FETCH_COUNT,  "--use-mastodon", I2M_USE_MASTODON]
#ENTRYPOINT ["echo", "--instagram-user", I2M_INSTAGRAM_USER, "--instance",  I2M_INSTANCE, "--token", I2M_TOKEN, "--check-interval", I2M_CHECK_INTERVAL, "--post-interval", I2M_POST_INTERVAL, "--fetch-count", I2M_FETCH_COUNT,  "--use-mastodon", I2M_USE_MASTODON]
ENTRYPOINT ["python", "/app/src/main.py"]
