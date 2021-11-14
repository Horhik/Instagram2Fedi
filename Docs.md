# Instagram2Fedi Docs 📜

## How to use
You can use Instagram2Fedi via docker or just like a python script

### Via Docker 🐋

Specify your variables in `./env.sh` and then run `./run.sh`

You can modify `docker run` arguments in `./run.sh`

### Just a python script 🐍

Run `pip3 install -r requirements.txt` and then run `./insta2fedi`.

Specify your arguments. You should use `--use-docker 0`.

For example: 
``` bash
 ./insta2fedi --use-docker false --instagram-user <instagram username> --instance <instance domain> --token <OAuth token> --check-interval 10 --post-interval 10 --use-mastodon 4
 # will check for new post each 10 seconds
```

## Command line arguments 🖥

`--use-mastodon` - set not positive number (`0`, `-1`...)  if your instance don't have max image count limit. 

For example, default maximum photo count in mastodon is `4`

`--instance` - Your instance url 

`--instagram-user` - Your instagram user name. 

`--token` - Your OAuth token

`--check-interval` - Interval in seconds how often to check for new posts

`--post-interval`  - Interval in seconds between posting new fetched posts.

If theres more than one new post, sets with which time interval should it post them

`--fetch-count` - How many new posts to select

`--use-docker` - If you're running it via docker container, set to `1` or `True`

## Default values ⚙
Default values are:
``` bash
    --instance None
    --instagram-user None
    --token None
    --check-interval 3600
    --post-interval 3600
    --fetch-count  10
    --use-mastodon 4
    --use-docker True
```
