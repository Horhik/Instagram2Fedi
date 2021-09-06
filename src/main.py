import os
import sys
import time
import hashlib
import json
from mastodon import Mastodon
from colorama import Fore, Back, Style
from instaloader import Profile, Instaloader, LatestStamps

id_filename = "/app/already_posted.txt"
with open(id_filename, "a") as f:
    f.write("\n")

fetched_user = sys.argv[1]
mastodon_instance = sys.argv[2]
mastodon_token = sys.argv[3]

post_limit = 1
time_interval_sec = 86400
post_interval = 10

using_mastodon = True;
mastodon_carousel_size = 4

print(Fore.GREEN + '🚀 > Connecting to Instagram...')
print(Style.RESET_ALL)

L = Instaloader()
profile = Profile.from_username(L.context, fetched_user)

print(Fore.GREEN + '🚀 > Connecting to Mastodon/Pixelfed...')
print(Style.RESET_ALL)
mastodon = Mastodon(
    access_token = mastodon_token,
    api_base_url = mastodon_instance
    # api_base_url = 'https://pixelfed.tokyo/'
)
while True:
    get_new_posts(mastodon, profile)
    time.sleep(time_interval_sec)
