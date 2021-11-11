from colorama import Fore, Back, Style
def process_arguments(args, defaults):
    count = 1
    while (len(args) > count):
        if(args[count] == "--instance"):
            defaults["instance"] = args[count + 1]
        elif (args[count] == "--instagram-user"):
            defaults["instagram-user"] = args[count + 1]

        elif (args[count] == "--token"):
            defaults["token"] = args[count + 1]

        elif (args[count] == "--check-interval"):
            defaults["check-interval"] = args[count + 1]

        elif (args[count] == "--post-interval"):
            defaults["post-interval"] = args[count + 1]

        elif (args[count] == "--fetch-count"):
            defaults["fetch-count"] = args[count + 1]

        elif (args[count] == "--using-mastodon"):
            defaults["carousel-limit"] = int(args[count + 1])

        else:
            print(Fore.RED + '❗ -> Wrong Argument Name!...')
            print(Style.RESET_ALL)

        count +=2
    return defaults

#fuck this shit im out''
#teenagers scare the living shit out of me
#deeeespaaaacito quero esperanto de despacito
#хорошо всё будет хорошо
#и камнем вниииз
#u kinda smell *smif* like a BAKA
#Yeren Yegaaaaaaa!!!!!!!!!
