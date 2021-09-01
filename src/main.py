import os
import sys
import requests
import time
from mastodon import Mastodon
from colorama import Fore, Back, Style
from instaloader import Profile, Instaloader

id_filename = "/app/already_posted.txt"
f = open(id_filename, "a")
f.write("\n")
f.close()

fetched_user = sys.argv[1]
mastodon_instance = sys.argv[2]
mastodon_token = sys.argv[3]

post_limit = 7
time_interval_sec = 1000

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
    file = open(id_filename);
    content = file.read()
    if id in content:
        file.close()
        return True
    else:
        file.close()
        return False

def mark_as_posted(id):
    file = open(id_filename, 'a');
    file.write(id + "\n")
    file.close()

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

def toot(url, title ):
    try:
        print(Fore.YELLOW + "🐘 > Creating Toot...", title)
        print(Style.RESET_ALL)

        id = upload_image_to_mastodon(url)
        post_text = str(title) + "\n" + "crosposted from https://instagram.com/"+fetched_user # creating post text
        print(id)
        mastodon.status_post(post_text, media_ids = [id])

    except:
        print(Fore.RED + "😿 > Failed to create toot")
        print(Style.RESET_ALL)

def none_convert(title):
    if title == None:
        return ""
    else:
        return str(title)

def generate_title(post):
    text = ""
    try:
        print(post.title)
        text += none_convert(post.title) + "\n"
    except:
        print("no title")
    try:
        print(post.accessibility_caption)
        text += none_convert(post.accessibility_caption) + "\n"
    except:
        print("no accessibilitycaption")
    try:
        print(post.edge_media_to_caption['edges'][0]['node']['text'])
        text += none_convert(post.edge_media_to_caption['edges'][0]['node']['text'])
    except:
        print("no edge_media_to_caption")
    return text
#  'edge_media_to_caption': {'edges': [{'node': {'text': 'Good morning!\n#komikaki #всемкартинки'}}]}

posts = profile.get_posts()
def get_new_posts():
    stupidcounter = 0
    for post in posts:
        stupidcounter += 1
        if stupidcounter < post_limit:
            if already_posted(str(post.url)):
                print(Fore.YELLOW + "🐘 > Already Posted", stupidcounter, " of ", posts.count)
                print(Style.RESET_ALL)
                continue
            toot(post.url, post.caption)
            mark_as_posted(str(post.url))
        else:
            return


while True:
    get_new_posts()
    time.sleep(time_interval_sec)
