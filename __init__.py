import os
import sys
import requests
from instabot import Bot
from mastodon import Mastodon

id_filename = "/app/already_posted.txt"
f = open(id_filename, "a")
f.close()

fetched_user = sys.argv[1]
username = sys.argv[2]
passwd = sys.argv[3]
mastodon_token = sys.argv[4]

bot = Bot()
bot.login(username = username,  password = passwd)

mastodon = Mastodon(
    access_token = mastodon_token,
    api_base_url = 'https://mastodon.ml'
)

def get_post(media_id, filename):
    media = bot.get_media_info(media_id)[0]
    id = media["id"]
    post_text = media["caption"]["text"]
    link = bot.get_media_id_from_link(id)
    images = []
    if ("image_versions2" in media.keys()):
        url = media["image_versions2"]["candidates"][0]["url"]
        response = requests.get(url)
        response.raw.decode_content = True
        images.append(response.content)
    elif("carousel_media" in media.keys()):
        for e, element in enumerate(media["carousel_media"]):
            url = element['image_versions2']["candidates"][0]["url"]
            response = requests.get(url)
            response.raw.decode_content = True
            images.append(response.content)
    return {
        "id"  : id,
        "text": post_text,
        "link": link,
        "images" : images
    }

def already_posted(id):
    file = open(id_filename, 'r');
    if id in file:
        file.close()
        return True
    else:
        file.close()
        return False

def add_id(id):
    file = open(id_filename, 'a');
    file.write(id + "\n")
    file.close()

def upload_images_to_mastodon(images_array):
    ids = []
    for i in images_array:
        media = mastodon.media_post(media_file = i, mime_type = "image/jpeg") # sending image to mastodon
        ids.append(media["id"])
    return ids

twony_last_medias = bot.get_user_medias(fetched_user, filtration = None)

for e,media_id in enumerate(twony_last_medias):
    post = get_post(media_id, "img_"+str(e)) # getting post info
    if(not already_posted(post["id"])):
        image_ids = upload_images_to_mastodon(post["images"])
        post_text = str(post["text"]) + "\n" + "crosposted from " + str(post["link"]) # creating post text
        mastodon.status_post(post_text, media_ids = image_ids) # attaching image to post and creating a toot
        add_id(post["id"]) # pushing id to "already_posted" file

