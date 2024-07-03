import requests, random, time
from colorama import Fore

while True: 
    user = ""

    for character in random.choices("abcdefghijqlmnopqrstuvwxyz1234567890", k=4):
        user = user + character

    response = requests.get("https://www.tiktok.com/@{user}/")

    if (response.status_code == 200):
         print(Fore.RED + f"NOT FOUND: {user}" + Fore.RESET)
    elif (response.status_code == 404):
         print(Fore.GREEN + f"USER FOUND: {user}" + Fore.RESET)
    else:
        print("BLOCKED FROM Tiktok")
        time.sleep(120) 