# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
import datetime

def split_array(arr, size):
    count = len(arr) // size + 1
    new_arr = []
    for i in range(count):
        new_arr.append(arr[i*size:(i+1)*size])
    return new_arr


def try_to_get_carousel(array, post):
    try:
        print("Looking for carousel in " + str(post))
        node = vars(post)['_node']
        if 'edge_sidecar_to_children' in node:
            try:
                urls = list(map(lambda arr: arr['node']['display_url'], node['edge_sidecar_to_children']['edges']))
                print(Fore.GREEN + "🎠 > Found carousel!")
                print(Style.RESET_ALL)
                print(datetime.datetime.now())
                return urls
            except Exception as e:
                print(Fore.RED + "🎠💥 > No carousel :( \n", e)
                print(Style.RESET_ALL)
                print(datetime.datetime.now())
                return array
        else:
                print(Fore.YELLOW + "🎠💥 > No carousel\n")

        # We can also have video in a separate key
        if 'is_video' in node and node ['is_video']:
            try:
                urls = [node['video_url']]
                print(Fore.GREEN + "🎞 > Found video!")
                print(Style.RESET_ALL)
                print(datetime.datetime.now())
                return urls
            except Exception as e:
                print(Fore.RED + "🎞💥 > No video :( \n", e)
                print(Style.RESET_ALL)
                print(datetime.datetime.now())
                return array
        else:
            print(Fore.YELLOW + "🎠💥 > No video\n")

    except Exception as e:
        print(Fore.RED + "😱💥 > No node :( \n", e)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())
        return array
    return array
