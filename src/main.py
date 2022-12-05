# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime
import json
from mastodon import Mastodon
from colorama import Fore, Back, Style
from instaloader import Profile, Instaloader, LatestStamps
from arguments import process_arguments


from network import get_new_posts


default_settings = {
    "instance": None,
    "instagram-user": None,
    "user-name": "",
    "user-password": None,
    "token": None,
    "check-interval": 3600,
    "post-interval": 60,
    "fetch-count" : 10,
    "carousel-limit": 4,
    "scheduled": False,
    "verbose": False
}

settings = process_arguments(sys.argv, default_settings)

verbose = settings["verbose"]

if verbose:
    print("ARGUMENTS")
    print(sys.argv)
    print('SETTINGS' , settings)

agree = [1, True, "true", "True", "yes", "Yes"]
if (os.environ.get("USE_DOCKER")):
    id_filename = "/app/already_posted.txt"
elif (os.environ.get("USE_KUBERNETES")):
    id_filename = "/data/already_posted.txt"
else:
    id_filename = "./already_posted.txt"


with open(id_filename, "a") as f:
    f.write("\n")

fetched_user = settings["instagram-user"]
mastodon_instance = settings["instance"]
mastodon_token = settings["token"]

post_limit = settings["fetch-count"]
time_interval_sec = settings["check-interval"] #1d
post_interval =  settings["post-interval"]#1m

using_mastodon = settings["carousel-limit"] > 0;
mastodon_carousel_size = settings["carousel-limit"]
scheduled = settings["scheduled"]


user = {
    "name": settings["user-name"],
    "password": settings["user-password"]
}

print(Fore.GREEN + '🚀 > Connecting to Mastodon/Pixelfed...')
print(Style.RESET_ALL)
print(datetime.datetime.now())
mastodon = Mastodon(
    access_token = mastodon_token,
    api_base_url = mastodon_instance
    # api_base_url = 'https://pixelfed.tokyo/'
)
while True:
    get_new_posts(mastodon, mastodon_carousel_size, post_limit, id_filename, using_mastodon, mastodon_carousel_size, post_interval, fetched_user, user)
    if scheduled:
        break
    time.sleep(time_interval_sec)
