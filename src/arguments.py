# -*- coding: utf-8 -*-
import os
import datetime
from colorama import Fore, Back, Style


instagram_user = os.environ.get("I2M_INSTAGRAM_USER")
user_name = os.environ.get("I2M_USER_NAME")
user_password = os.environ.get("I2M_USER_PASSWORD")
instance = os.environ.get("I2M_INSTANCE")
token = os.environ.get("I2M_TOKEN")
check_interval = os.environ.get("I2M_CHECK_INTERVAL") #1 hour 
post_interval = os.environ.get("I2M_POST_INTERVAL") #1 hour 
use_mastodon = os.environ.get("I2M_USE_MASTODON") #max carousel is 4, if there's no limit set to -1
fetch_count = os.environ.get("I2M_FETCH_COUNT") # how many instagram posts to fetch per check_interval
if os.environ.get("I2M_SCHEDULED") == "True":
    scheduled_run = True # run continuously (if False) or a single time (if True)
else:
    scheduled_run = False
if os.environ.get("I2M_VERBOSE") == "True": # verbose output
    verbose_output = True
else:
    verbose_output = False

if verbose_output:
    print('instagram', instagram_user)
    print('instagram', instance)
    print(token)
    print(check_interval)
    print(post_interval)
    print(use_mastodon)
    print(fetch_count)
    print(user_name)
    print(user_password)
    print(scheduled_run)
    print(verbose_output)



def flags(args, defaults):
    count = 1
    while (len(args) > count):
        if(args[count] == "--instance"):
            defaults["instance"] = args[count + 1]
        elif (args[count] == "--instagram-user"):
            defaults["instagram-user"] = args[count + 1]

        elif (args[count] == "--token"):
            defaults["token"] = args[count + 1]

        elif (args[count] == "--check-interval"):
            defaults["check-interval"] = int(args[count + 1])

        elif (args[count] == "--post-interval"):
            defaults["post-interval"] = int(args[count + 1])

        elif (args[count] == "--fetch-count"):
            defaults["fetch-count"] = int(args[count + 1])

        elif (args[count] == "--use-mastodon"):
            defaults["carousel-limit"] = int(args[count + 1])
        elif (args[count] == "--use-docker"):
            defaults["use-docker"] = args[count + 1]
        elif (args[count] == "--user-name"):
            defaults["user-name"] = args[count + 1]
        elif (args[count] == "--user-password"):
            defaults["user-password"] = args[count + 1]
        elif (args[count] == "--scheduled"):
            defaults["scheduled"] = True
            count -= 1
        elif (args[count] == "--verbose"):
            defaults["verbose"] = True
            count -= 1

        else:
            print(Fore.RED + '❗ -> Wrong Argument Name!...')
            print(Style.RESET_ALL)
            print(datetime.datetime.now())

        count +=2
    return defaults

def check_defaults(arg):
    return arg if arg != '' and arg else None

def process_arguments(args, defaults):
    defaults["instance"] = instance if instance !='' and instance else None
    defaults["instagram-user"] = instagram_user if instagram_user != '' and instagram_user else None
    # Users login and password
    defaults["user-name"] = check_defaults(user_name)
    defaults["user-password"] = check_defaults(user_password)
    defaults["token"] = token if token != '' and token else None
    defaults["check-interval"] = int(check_interval) if check_interval != '' and check_interval else None
    defaults["post-interval"] = int(post_interval) if post_interval != '' and post_interval else None
    defaults["fetch-count"] = int(fetch_count) if fetch_count != '' and fetch_count else None
    defaults["carousel-limit"] = int(use_mastodon) if use_mastodon != '' and use_mastodon else None
    defaults["scheduled"] = bool(scheduled_run) if scheduled_run else False
    defaults["verbose"] = bool(verbose_output) if verbose_output else False
    #print(Fore.RED + '❗ -> Missing Argument ')
    #print(Style.RESET_ALL)
    #print(datetime.datetime.now())


    # Command line arguments more prioritized, if smth has been written in .env and in cmd args, then Instagram2Fedi will take values from `cmd args`
    new_defaults = flags(args, defaults)
    return new_defaults

