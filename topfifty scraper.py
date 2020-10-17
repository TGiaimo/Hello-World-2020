from selenium import webdriver
import string

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
chrome_driver_binary = "chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options = options)
alphabet_array = list(string.ascii_uppercase)
URL = "http://www.iweblists.com/us/commerce/MarketCapitalization.html"
driver.get(URL)
f = open("topfif.txt", "a+")
for i in range(1, 51):
    name = driver.find_elements_by_xpath(f"/html/body/div[3]/div[2]/table/tbody/tr[{i}]/td[3]")[0]
    #/html/body/div[3]/div[2]/table/tbody/tr[1]/td[3]
    #/html/body/div[3]/div[2]/table/tbody/tr[2]/td[3]
    print(name.text, file=f)