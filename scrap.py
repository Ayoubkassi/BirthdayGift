from selenium import webdriver
from time import time
from time import sleep
from datetime import datetime
import subprocess
import shlex

music = input("Enter ur favourite music : ")
food = input("Enter ur favourite food : ")
movie = input("Enter ur favourite movie  : ")
habbit = input("Enter ur favourite habbit : ")
country = input("Enter ur favourite countrie : ")
animal = input("Enter ur favourite animal : ")
singer = input("Enter ur favourite singer : ")
thing1 = input("Enter ur favourite thing 1 : ")
thing2 = input("Enter ur favourite thing 2 : ")


now = datetime.now()

begin_time = now.strftime("%H:%M:%S")
print(begin_time)



class BirthdayGift:
    def __init__(self, music, food , movie , habbit , country , animal , singer , thing1 , thing2):
        self.driver = webdriver.Chrome()

        #get food
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(food)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()
        sleep(3)


        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()

        #get movie
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(movie)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)


        #get habbit
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(habbit)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)


        #get country
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(country)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)


        #get animal
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(animal)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)


        #get singer
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(singer)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()

        sleep(3)

        #get thing1
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(thing1)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)


        #get thing2
        self.driver.get("https://picjumbo.com/")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[1]').send_keys(thing2)
        next_butt = self.driver.find_element_by_xpath(
            '/html/body/div[2]/form/input[2]').click()
        image = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/a/picture/img').click()

        sleep(2)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[4]/article/div/div[4]/a[1]').click()
        sleep(3)





my_gift = BirthdayGift(music, food , movie , habbit , country , animal , singer , thing1 , thing2)

#finally i will get last time
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(end_time)
