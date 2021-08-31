# Instagram2Mastodon 🐘

Simple python 🐍 script for crossposting from instagram to mastodon/pixelfed
## Installing
Just clone repo, build a docker container and run it
``` bash
git clone https://github.com/horhik/instagram2mastodon
cd instagram2mastodon
docker build -t YOUR_CONTAINER_NAME .
docker container run -it -v $(pwd):/app YOUR_CONTAINER_NAME I2M_INSTAGRAM_USER I2M_INSTANCE I2M_TOKEN
```


