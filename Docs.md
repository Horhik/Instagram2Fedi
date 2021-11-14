# Instagram2Fedi Docs

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
