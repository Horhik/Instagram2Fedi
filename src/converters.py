from colorama import Fore, Back, Style

def split_array(arr, size):
    count = len(arr) // size + 1
    new_arr = []
    for i in range(count):
        new_arr.append(arr[i*size:(i+1)*size])
    return new_arr


def try_to_get_carousel(array, post):
    try:
        urls = list(map(lambda arr: arr['node']['display_url'], vars(post)['_node']['edge_sidecar_to_children']['edges']))
        return urls
        print(Fore.GREEN + "🎠 > Found carousel!")
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "🎠💥 > No carousel :( \n", e)
        print(Style.RESET_ALL)
        return array

    
