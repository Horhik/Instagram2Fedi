import os
import sys
import requests
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

def get_image(url):
    try:
        print(Fore.YELLOW + "🚀 > Downloading Image...", url)
        print(Style.RESET_ALL)

        response = requests.get(url)
        response.raw.decode_content = True
        
        print(Fore.GREEN + "✨ > Downloaded!")
        print(Style.RESET_ALL)

        return response.content
    except:

        print(Fore.RED + "💥 > Failed to download image.")
        print(Style.RESET_ALL)


def already_posted(id):
    with open(id_filename) as file:
        content = file.read().split("\n")
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        if sha1 in content:
            return True
        return False

def mark_as_posted(id):
    with open(id_filename, 'a') as file:
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        file.write(sha1+'\n')

def upload_image_to_mastodon(url):
    try:
        print(Fore.YELLOW + "🐘 > Uploading Image...")
        print(Style.RESET_ALL)
        media = mastodon.media_post(media_file = get_image(url), mime_type = "image/jpeg") # sending image to mastodon
        print(Fore.GREEN + "✨ > Uploaded!")
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + "💥 > failed to upload image to mastodon")
        print(Style.RESET_ALL)
    return media["id"]

def toot(urls, title ):
    try:
        print(Fore.YELLOW + "🐘 > Creating Toot...", title)
        print(Style.RESET_ALL)
        ids = []
        for url in urls:
            ids.append(upload_image_to_mastodon(url))
        post_text = str(title) + "\n" + "crosposted from https://instagram.com/"+fetched_user # creating post text
        print(ids)
        mastodon.status_post(post_text, media_ids = ids)

    except:
        print(Fore.RED + "😿 > Failed to create toot")
        print(Style.RESET_ALL)

def none_convert(title):
    if title == None:
        return ""
    else:
        return str(title)

def try_to_get_carousel(arr, post):
    try:
        urls = list(map(lambda arr: arr['node']['display_url'], vars(post)['_node']['edge_sidecar_to_children']['edges']))
        return urls
        print("Found carousel")
    except:
        print("No carousel")
        return arr

def split_array(arr, size):
    count = len(arr) // size + 1
    new_arr = []
    for i in range(count):
        new_arr.append(arr[i*size:(i+1)*mastodon_carousel_size])
    return new_arr

posts = profile.get_posts()
def get_new_posts():
    stupidcounter = 0
    for post in posts:
        stupidcounter += 1
        url_arr = try_to_get_carousel([post.url], post), mastodon_carousel_size

        if stupidcounter <= post_limit:
            if already_posted(str(post.mediaid)):
                print(Fore.YELLOW + "🐘 > Already Posted ", post.url)
                print(Style.RESET_ALL)
                continue
            print("Posting... ", post.url)
            if using_mastodon:
                urls_arr = split_array(url_arr)
                for urls in urls_arr:
                    toot(urls, post.caption)
            else:
                toot(url_arr, post.caption)
                    
            mark_as_posted(str(post.mediaid))
            time.sleep(post_interval)
        else:
            return


while True:
    get_new_posts()
    time.sleep(time_interval_sec)
