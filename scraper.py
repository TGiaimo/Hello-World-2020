#Test

from selenium import webdriver
#import pandas as pd
import string

driver_path = "C:/Users/Thomas/Desktop/school/hello world 2020/chromedriver/chromedriver.exe"
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
alphabet_array = list(string.ascii_uppercase)
URL = "https://www.advfn.com/nasdaq/nasdaq.asp?companies="
for letter in alphabet_array:
    temp = URL
    temp += letter
    driver.get(temp)
    #companyName = driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[18]/td[1]/a")[0]
    #driver.get(temp)
    tbody = driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr")
    companies = []
    for i in range(5, len(tbody)):
        try:
            companyName = driver.find_elements_by_xpath(f"/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[{i}]/td[2]/a")[0]
            companies.append(companyName)
            #change f = open to something else, depreciated code
            f = open("output.txt", "a+")
            print(companyName.text + ":NASDAQ", file=f)
        except:
            pass