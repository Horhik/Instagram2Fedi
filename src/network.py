from colorama import Fore, Back, Style
import requests
import time
from already_posted import already_posted, mark_as_posted
from converters import split_array, try_to_get_carousel
import hashlib

def get_image(url):
    try:
        print(Fore.YELLOW + "🚀 > Downloading Image...", url)
        print(Style.RESET_ALL)

        response = requests.get(url)
        response.raw.decode_content = True
        
        print(Fore.GREEN + "✨ > Downloaded!")
        print(Style.RESET_ALL)

        return response.content
    except Exception as e:

        print(Fore.RED + "💥 > Failed to download image. \n", e)
        print(Style.RESET_ALL)


def upload_image_to_mastodon(url, mastodon):
    try:
        print(Fore.YELLOW + "🐘 > Uploading Image...")
        print(Style.RESET_ALL)
        media = mastodon.media_post(media_file = get_image(url), mime_type = "image/jpeg") # sending image to mastodon
        print(Fore.GREEN + "✨ > Uploaded!")
        print(Style.RESET_ALL)
        return media["id"]
    except Exception as e:
        print(Fore.RED + "💥 > failed to upload image to mastodon. \n", e)
        print(Style.RESET_ALL)

def toot(urls, title, mastodon, fetched_user ):
    try:
        print(Fore.YELLOW + "🐘 > Creating Toot...", title)
        print(Style.RESET_ALL)
        ids = []
        for url in urls:
            ids.append(upload_image_to_mastodon(url, mastodon))
        post_text = str(title) + "\n" + "crosposted from https://instagram.com/"+fetched_user # creating post text
        post_text = post_text[0:1000]
        print(ids)
        mastodon.status_post(post_text, media_ids = ids)

    except Exception as e:
        print(Fore.RED + "😿 > Failed to create toot \n", e)
        print(Style.RESET_ALL)

def get_new_posts(mastodon, profile, mastodon_carousel_size, post_limit, already_posted_path, using_mastodon, carousel_size, post_interval, fetched_user):
    posts = profile.get_posts()
    stupidcounter = 0
    for post in posts:
        stupidcounter += 1
        url_arr = try_to_get_carousel([post.url], post)
        if stupidcounter <= post_limit:
            if already_posted(str(post.mediaid), already_posted_path):
                print(Fore.YELLOW + "🐘 > Already Posted ", post.url)
                print(Style.RESET_ALL)
                continue
            print("Posting... ", post.url)
            if using_mastodon:
                urls_arr = split_array(url_arr, carousel_size)
                for urls in urls_arr:
                    toot(urls, post.caption, mastodon, fetched_user)
            else:
                toot(url_arr, post.caption, mastodon, fetched_user)
                    
            mark_as_posted(str(post.mediaid), already_posted_path) 
            time.sleep(post_interval)
        else:
            return


