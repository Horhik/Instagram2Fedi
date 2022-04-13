# -*- coding: utf-8 -*-
import os
import datetime
from colorama import Fore, Back, Style


instagram_user = os.environ.get("I2M_INSTAGRAM_USER")
instance = os.environ.get("I2M_INSTANCE")
token = os.environ.get("I2M_TOKEN")
check_interval = os.environ.get("I2M_CHECK_INTERVAL") #1 hour 
post_interval = os.environ.get("I2M_POST_INTERVAL") #1 hour 
use_mastodon = os.environ.get("I2M_USE_MASTODON") #max carouse is 4, if there's no limit set to -1
fetch_count = os.environ.get("I2M_FETCH_COUNT") # how many instagram posts to fetch per check_interval
print('instagram', instagram_user)
print('instagram', instance)
print(token)
print(check_interval)
print(post_interval)
print(use_mastodon)
print(fetch_count)




def process_arguments(args, defaults):
    if(instance):
        defaults["instance"] = instance
    elif (instagram_user):
        defaults["instagram-user"] = instagram_user
    elif (token):
        defaults["token"] = token

    elif (check_interval):
        defaults["check-interval"] = check_interval

    elif (post_interval):
        defaults["post-interval"] = post_interval

    elif (fetch_count):
        defaults["fetch-count"] = fetch_count

    elif (use_mastodon):
        defaults["carousel-limit"] = use_mastodon
    else:
        print(Fore.RED + '❗ -> Missing Argument ')
        print(Style.RESET_ALL)
        print(datetime.datetime.now())
    return defaults

