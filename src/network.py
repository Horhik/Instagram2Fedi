from colorama import Fore, Back, Style
import requests

from converters import split_array, try_to_get_carousel

def upload_image_to_mastodon(url, mastodon):
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

def get_new_posts(mastodon, profile, mastodon_carousel_size, ):
    posts = profile.get_posts()
    stupidcounter = 0
    for post in posts:
        stupidcounter += 1
        url_arr = try_to_get_carousel([post.url], post), mastodon_carousel_size

        if stupidcounter <= post_limit:
            if already_posted(str(post.mediaid), id_filename):
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
                    
            mark_as_posted(str(post.mediaid), id_filename) 
            time.sleep(post_interval)
        else:
            return



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

