from selenium import webdriver
from time import time
from time import sleep
from datetime import datetime
import subprocess
import shlex
import pyautogui
import pyperclip

values = []
items= {}

# music = input("Enter ur favourite music : ")
# values.append(music)
food = input("Enter ur favourite food : ")
values.append(food)
movie = input("Enter ur favourite movie  : ")
values.append(movie)
habbit = input("Enter ur favourite habbit : ")
values.append(habbit)
country = input("Enter ur favourite countrie : ")
values.append(country)
animal = input("Enter ur favourite animal : ")
values.append(animal)
singer = input("Enter ur favourite singer : ")
values.append(singer)
thing1 = input("Enter ur favourite thing 1 : ")
values.append(thing1)
thing2 = input("Enter ur favourite thing 2 : ")
values.append(thing2)


now = datetime.now()

begin_time = now.strftime("%H:%M:%S")
print(begin_time)


def getUrl(name):
    webdriver.Chrome().get("https://images.google.com/")
    sleep(2)
    login_field = webdriver.Chrome().find_element_by_xpath(
        '//*[@id="sbtc"]/div/div[2]/input').send_keys(name+" image size : 886x1920")
    next_butt = webdriver.Chrome().find_element_by_xpath(
        '//*[@id="sbtc"]/button').click()

    pyautogui.moveTo(200, 510, duration = 1)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(800, 510, duration = 1)
    sleep(3)
    pyautogui.click(button='right')
    pyautogui.press('up', presses=3)
    pyautogui.press('enter')
    url =  pyperclip.paste()
    return url


#get all necessary links
for item in values:
    items[item] = getUrl(item)


# class BirthdayGift:
#     def __init__(self, music, food , movie , habbit , country , animal , singer , thing1 , thing2):
#         self.driver = webdriver.Chrome()



#my_gift = BirthdayGift(music, food , movie , habbit , country , animal , singer , thing1 , thing2)

#finally i will get last time
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(end_time)
