#!/bin/sh
source ./env.sh
docker build -t $YOUR_CONTAINER_NAME .;  docker container run -it -v $(pwd):/app $YOUR_CONTAINER_NAME --use-docker 1 --instagram-user $I2M_INSTAGRAM_USER --instance $I2M_INSTANCE --token $I2M_TOKEN --check-interval $I2M_CHECK_INTERVAL --post-interval $I2M_POST_INTERVAL --fetch-count $I2M_FETCH_COUNT --use-mastodon  $I2M_USE_MASTODON
