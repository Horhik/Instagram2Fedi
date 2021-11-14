# -*- coding: utf-8 -*-
import datetime
from colorama import Fore, Back, Style
def process_arguments(args, defaults):
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

        else:
            print(Fore.RED + '❗ -> Wrong Argument Name!...')
            print(Style.RESET_ALL)
            print(datetime.datetime.now())

        count +=2
    return defaults

