#!/bin/sh
source ./env.sh
docker build -t $YOUR_CONTAINER_NAME .;  docker container run -it  -v $(pwd):/app $YOUR_CONTAINER_NAME $I2M_INSTAGRAM_USER $I2M_INSTANCE $I2M_TOKEN
