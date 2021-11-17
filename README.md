# Instagram2Fedi <span><img width="50px" src="https://upload.wikimedia.org/wikipedia/commons/9/93/Fediverse_logo_proposal.svg"></span>

Simple python 🐍 script for crossposting from instagram to Mastodon/Pixelfed

## Installing

Just clone repo, build a docker container and run it

``` bash
git clone https://github.com/horhik/instagram2fedi
cd instagram2fedi
docker build -t $YOUR_CONTAINER_NAME .
docker container run -it -d -v $(pwd):/app $YOUR_CONTAINER_NAME $I2M_INSTAGRAM_USER $I2M_INSTANCE $I2M_TOKEN
```

You can write all needed variables in `./env.sh` and then do `source ./run.sh`


![image](https://user-images.githubusercontent.com/46262811/131577640-a3103ff2-af37-422d-96f1-60f1acdef939.png)



