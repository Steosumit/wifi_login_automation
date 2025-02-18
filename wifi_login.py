"""
A script to automate the lousy wifi login process at my university.
Contributed By: Sumit (steosumit@gmail.com, reach for errors :) 

"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

class WifiAutomate:
    # Private variables 
    username_ = ""
    password_ = ""
    network_name_ = ""

    # Constructor 1
    def __init__(self):
        if not os.path.isfile("user_info.json"):
            print("User info not found, please input it :)")
            username = input("Enter the username:")
            password = input("Enter the password:")
            self.search_network()
            network_name = input("Enter network name:")
            self.user_info_save(username, password, network_name)
        self.read_user_info()
        
    def search_network(self):
        os.system('cmd /c "netsh wlan show networks')

    def attemp_connect(self, network_name):
        os.system(f'cmd /c "netsh wlan connect name={network_name}')
        if os.error:
            print("Something went wrong in the ps command to connect(ignore if working LOL)!")
    
    def user_info_save(self, username, password, network_name):
        temp_dict = {'username': username, 'password': password, 'network_name': network_name}
        with open("user_info.json", "w+") as file:
            json.dump(temp_dict, file)
        print("user_info.txt file written! Change it manually for future changes tech guys... or delete it and recreate if messed up")
    
    def read_user_info(self):
        with open('user_info.json', 'r+') as file:
            temp_dict = json.load(file)
            self.username_ = temp_dict['username']
            self.password_ = temp_dict['password']
            self.network_name = temp_dict['network_name']
            print("Read user info 200...")
        

    def main(self):
        # Create the driver access object
        driver = webdriver.Edge()
        # Attemp connect to reach the browser environment
        self.attemp_connect(self.network_name)
        # Get the website by url(uniquely generated everytime)
        driver.get("http://172.16.48.4:1000/login?0335caf461d00cbd")
        print("IGNORE ERRORS AFTER THIS IF ANY :)")
        # The required web elements
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.NAME, "password")
        button_element = driver.find_element(By.XPATH, "//input[@type='submit']")
        print("IGNORE ERRORS AFTER THIS IF ANY :)")
        # Set the username and password variables TODO: change it
        my_username = self.username_
        my_password = self.password_
        # Use the web element to write the username and password
        username_element.send_keys(my_username)
        password_element.send_keys(my_password)
        button_element.click()
        driver.close()


WifiAutomateObj =  WifiAutomate()  
WifiAutomateObj.main()


# Back up original script for future use if things are messed up
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create the driver access object
driver = webdriver.Edge()
# Get the website by url(uniquely generated everytime)
driver.get("http://172.16.48.4:1000/login?0335caf461d00cbd")
# The required web elements
username_element = driver.find_element(By.NAME, "username")
password_element = driver.find_element(By.NAME, "password")
button_element = driver.find_element(By.XPATH, "//input[@type='submit']")
# Set the username and password variables TODO: change it
my_username = "heheheheh"
my_password = "shitshitshit"
# Use the web element to write the username and password
username_element.send_keys(my_username)
password_element.send_keys(my_password)
button_element.click()
driver.close()
"""
