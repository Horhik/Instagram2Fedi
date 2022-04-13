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

def exists(a):
    return a != '' and a != False


def process_arguments(args, defaults):
    defaults["instance"] = instance if instance !='' and instance else None
    defaults["instagram-user"] = instagram_user if instagram_user != '' and instagram_user else None
    defaults["token"] = token if token != '' and token else None
    defaults["check-interval"] = int(check_interval) if check_interval != '' and check_interval else None
    defaults["post-interval"] = int(post_interval) if post_interval != '' and post_interval else None
    defaults["fetch-count"] = int(fetch_count) if fetch_count != '' and fetch_count else None
    defaults["carousel-limit"] = int(use_mastodon) if use_mastodon != '' and use_mastodon else None
    #print(Fore.RED + '❗ -> Missing Argument ')
    #print(Style.RESET_ALL)
    #print(datetime.datetime.now())
    print(defaults)
    return defaults

