# Main Python file

from selenium import webdriver
#import pandas as pd
import string

driver = webdriver.Chrome('C:\\Users\\Thomas\\Desktop\\school\\hello world 2020\\chromedriver')
alphabet_array = list(string.ascii_lowercase)
print(alphabet_array)
url = "https://www.advfn.com/nasdaq/nasdaq.asp?companies="
for letter in alphabet_array:
    url += letter
    driver.get(url)
    companyName = driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[18]/td[1]/a")
    print(companyName)