# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
import requests
import time
import datetime
from already_posted import already_posted, mark_as_posted
from converters import split_array, try_to_get_carousel
import hashlib
import os
from instaloader import Profile, Instaloader, LatestStamps

def get_instagram_user(user, fetched_user, id_session):
    L = Instaloader()

    print(Fore.GREEN + 'TEST 🚀 > Connecting to Instagram...')
    print(Style.RESET_ALL)
    print(datetime.datetime.now())
    if os.path.exists(id_session):
        L.load_session_from_file(user["name"], id_session)
    try:
        username = L.test_login()
    except:
        username = None
    print("USER USER USER!!!!!!!!!!!!!", user["name"])
    if not username and user["name"] != None:
        print("USER USER USER!!!!!!!!!!!!!", user["name"])
        L.login(user["name"], user["password"])
        L.save_session_to_file(id_session)
    return Profile.from_username(L.context, fetched_user)

def get_image(url):
    try:
        print(Fore.YELLOW + "🚀 > Downloading Image...", url)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())

        response = requests.get(url)
        response.raw.decode_content = True

        print(Fore.GREEN + "✨ > Downloaded!")
        print(Style.RESET_ALL)
        print(datetime.datetime.now())

        return response.content
    except Exception as e:

        print(Fore.RED + "💥 > Failed to download image. \n", e)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())


def upload_image_to_mastodon(url, mastodon):
    try:
        print(Fore.YELLOW + "🐘 > Uploading Image...")
        print(Style.RESET_ALL)
        print(datetime.datetime.now())
        media = mastodon.media_post(media_file = get_image(url), mime_type = "image/jpeg") # sending image to mastodon
        print(Fore.GREEN + "✨ > Uploaded!")
        print(Style.RESET_ALL)
        print(datetime.datetime.now())
        return media["id"]
    except Exception as e:
        print(Fore.RED + "💥 > failed to upload image to mastodon. \n", e)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())

def toot(urls, title, mastodon, fetched_user ):
    try:
        print(Fore.YELLOW + "🐘 > Creating Toot...", title)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())
        ids = []
        for url in urls:
            ids.append(upload_image_to_mastodon(url, mastodon))
        post_text = str(title) + "\n"  # creating post text
        post_text = post_text[0:1000]
        if(ids):
            print(ids)
            mastodon.status_post(post_text, media_ids = ids)

    except Exception as e:
        print(Fore.RED + "😿 > Failed to create toot \n", e)
        print(Style.RESET_ALL)
        print(datetime.datetime.now())

def get_new_posts(mastodon,  mastodon_carousel_size, post_limit, already_posted_path, using_mastodon, carousel_size, post_interval, fetched_user, user, id_session):
    # fetching user profile to get new posts
    profile = get_instagram_user(user, fetched_user, id_session)
    # get list of all posts
    posts = profile.get_posts()
    stupidcounter = 0
    for post in posts:
        url_arr = try_to_get_carousel([post.url], post)
        # checking only `post_limit` last posts
        if stupidcounter < post_limit:
            stupidcounter += 1
            if already_posted(str(post.mediaid), already_posted_path):
                print(Fore.YELLOW + "🐘 > Already Posted ", post.url)
                print(Style.RESET_ALL)
                print(datetime.datetime.now())
                continue
            print("Posting... ", post.url)
            print(datetime.datetime.now())
            if using_mastodon:
                urls_arr = split_array(url_arr, carousel_size)
                for urls in urls_arr:
                    toot(urls, post.caption, mastodon, fetched_user)
            else:
                toot(url_arr, post.caption, mastodon, fetched_user)
            mark_as_posted(str(post.mediaid), already_posted_path)
            time.sleep(post_interval)
        else:
            break
    print(Fore.GREEN + "✨ > Fetched All")
    print(Style.RESET_ALL)
    print(datetime.datetime.now())


