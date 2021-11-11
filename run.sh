#!/bin/sh
source ./env.sh
docker build -t $YOUR_CONTAINER_NAME .;  docker container run -it -v $(pwd):/app $YOUR_CONTAINER_NAME --instagram-user $I2M_INSTAGRAM_USER --instance $I2M_INSTANCE --token $I2M_TOKEN
