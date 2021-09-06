
def already_posted(id, id_filename):
    with open(id_filename) as file:
        content = file.read().split("\n")
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        if sha1 in content:
            return True
        return False

def mark_as_posted(id, id_filename):
    with open(id_filename, 'a') as file:
        sha1 = hashlib.sha1(bytes(id, "utf-8")).hexdigest()
        file.write(sha1+'\n')

