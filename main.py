import urllib3

urllib3.disable_warnings()
http = urllib3.PoolManager()
from PIL import Image
from colorama import init, Fore, Back, Style

init()
from time import sleep
import os, sys
import math
import io
from os import listdir
import glob
from requests import get

print(Fore.LIGHTMAGENTA_EX + "\n"
      f'Started New Cosmetics Generator | Made by Kraypex')


def gen():
    res = get('https://benbot.app/api/v1/newCosmetics').json()['items']
    for i in res:
        name = i['name']
        desc = i['description']
        rarity = i['rarity']
        img = i['icons']['icon']
        id = i['id']
        print(Fore.CYAN + '[NCG] ', end="")
        print(Fore.GREEN + f'Name: {name} Desc: {desc} Rarity: {rarity}')
        try:
            img = Image.open(io.BytesIO(http.urlopen("GET", img).data))
            img.save(f"Output/{id}.png")
        except:
            img = 'your backup image url'
            img = Image.open(io.BytesIO(http.urlopen("GET", img).data))
            img.save(f"Output/{id}.png")


def merge():
    try:
        print(Fore.CYAN)
        images_to_len = [file for file in listdir('Output')]
        x = len(images_to_len)
        folder = os.path.join(os.getcwd(), "Output")
        img_list = os.listdir(folder)
        img_list1 = []
        for i in img_list:
            img_list1.append(os.path.join(folder, i))

        for i in range(len(img_list1)):
            img_list1[i] = Image.open(img_list1[i])
            img_list1[i] = img_list1[i].resize((512, 512))
        if x <= 25:
            height = math.ceil(len(img_list1) / 5)
            width_accroding_to_len = 2560
            number_of_if = 5
        elif 35 > x > 25:
            height = math.ceil(len(img_list1) / 6)
            width_accroding_to_len = 3072
            number_of_if = 6
        elif 50 >= x > 35:
            height = math.ceil(len(img_list1) / 8)
            width_accroding_to_len = 4096
            number_of_if = 8
        elif x < 15:
            height = math.ceil(len(img_list1) / 4)
            width_accroding_to_len = 2048
            number_of_if = 4
        elif x > 50:
            height = math.ceil(len(img_list1) / 9)
            number_of_if = 9
            width_accroding_to_len = 4608

        new = Image.new("RGBA", (width_accroding_to_len, 512 * height))

        w = 0
        h = 0
        for i in img_list1:
            new.paste(i, (512 * w, 512 * h))
            w = w + 1
            if w == number_of_if:
                w = 0
                h = h + 1
        new = new.save('Output\merged.png')
        print(f"{Fore.LIGHTCYAN_EX}-> All done the image is merged.")
    except:
        print(
            f"{Fore.RED}-> Merge Failed (Please check if the folder is empty or not)"
        )


print(Fore.CYAN + '\nDo you want to:')
print(Fore.LIGHTGREEN_EX)
print(" (1) Grab all new cosmetics from the API ")
print(" (2) Delete all the content of Output Folder ")
print(" (3) Merge all images in Output File ")
ask = (input("- >>> "))

if ask == "3":
    merge()
    print(f"{Fore.CYAN} All image merged...Closing...")
    sleep(3)
    sys.exit()
if ask == "2":
    del_files = glob.glob('output/*')
    for file in del_files:
        os.remove(file)

    print(f"{Fore.LIGHTRED_EX}-> Deleting old content... ")
    print(f"{Fore.RED}-> Content deleted... \n"
          )  #this part for delete the content of the [output]
    print(Fore.LIGHTGREEN_EX)
    ask_to_gen = (input(
        "\n-> Do you want to start Generate the items or Close [Gen] or [Close] >> "
    ))
    if ask_to_gen == "Gen":
        print(f"{Fore.YELLOW}-> GENERATION STARTED\n\n")
        gen()
        print(
            "\n-> Do you want to merge the generated images ? y (yes) / n (no) : "
        )
        ask_to_merge = (input(">>>> "))
        if ask_to_merge == "y":
            merge()
        elif ask_to_merge == "n":
            print("Not merging the generated images... Closing...")
            sys.exit()
        else:
            print(
                f"{Fore.LIGHTRED_EX}-> undefind answer please try again...closing"
            )
            sleep(5)
            sys.exit()

    elif ask_to_gen == "Close":
        print(Fore.YELLOW)
        print("Closing the generator, thanks for using!")
        sleep(2)
        sys.exit()

    else:
        print(
            f"{Fore.LIGHTRED_EX}-> Undefind answer please try again...closing")
        sleep(5)
        sys.exit()
if ask == "1":
    print(f"{Fore.YELLOW}-> Generation Started:\n\n")
    gen()
    print(
        "\n-> Do you want to merge the generated images ? y (yes) / n (no) : ")
    ask_to_merge = (input(">>>> "))
    if ask_to_merge == "y":
        merge()
    elif ask_to_merge == "n":
        print("Not Merging the generated images... Closing...")
        sys.exit()
    else:
        print(
            f"{Fore.LIGHTRED_EX}-> Undefind answer please try again...closing")
        sleep(5)
        sys.exit()
