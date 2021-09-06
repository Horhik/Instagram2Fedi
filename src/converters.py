def split_array(arr, size):
    count = len(arr) // size + 1
    new_arr = []
    for i in range(count):
        new_arr.append(arr[i*size:(i+1)*size])
    return new_arr


def try_to_get_carousel(arr, post):
    try:
        urls = list(map(lambda arr: arr['node']['display_url'], vars(post)['_node']['edge_sidecar_to_children']['edges']))
        return urls
        print("Found carousel")
    except:
        print("No carousel")
        return arr

