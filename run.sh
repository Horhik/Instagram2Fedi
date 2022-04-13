#!/bin/sh
source ./env.sh
docker build -t $YOUR_CONTAINER_NAME .;  docker container run -it -v $(pwd):/app 
