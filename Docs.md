# Instagram2Fedi Docs 📜

## How to use
You can use Instagram2Fedi via docker or just like a python scrip

### Via Docker

Specify your variables in `./env.sh` and then run `./run.sh`

You can modify `docker run` arguments in `./run.sh`

### Just a python script

Run `pip3 install -r requirements.txt` and then run `./insta2fedi`.

Specify your arguments. You should use `--use-docker 0`.

## Command line arguments 

`--use-mastodon` - set not positive number (`0`, `-1`...)  if your instance don't have max image count limit. 

For example, default maximum photo count in mastodon is `4`

`--instance` - Your instance url 

`--instagram-user` - Your instagram user name. 

`--token` - Your OAuth token

`--check-interval` - Interval in seconds how often to check for new posts

`--post-interval`  - Interval in seconds between new fetched posts.

If theres more than one new post, sets with which time interval should it post them

`--fetch-count` - How many new posts to select

`--use-docker` - If you're running it via docker container, set to `1` or `True`
