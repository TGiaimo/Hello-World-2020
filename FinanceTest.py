from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

#Zacks
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
chrome_driver_binary = "chromedriver"

def ZacksRec(StockTicker):
    
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options = options)
    Zacks = "https://zacks.com/stock/quote/" + StockTicker;
    driver.get(Zacks);

    Rec = driver.find_element_by_id("quote_ribbon_v2");
    Rec.screenshot("Zacks.png");
    
    im = Image.open("Zacks.png");
    im.show();
    
    
    driver.close();

#CNN Money

def CNNRec(StockTicker):
    
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options = options)
    CNN = "https://money.cnn.com/quote/forecast/forecast.html?symb=" + StockTicker;
    driver.get(CNN);

    Rec = driver.find_element_by_id("wsod_forecasts");
    Rec.screenshot("CNN.png");

    im = Image.open(r"CNN.png");
    width, height = im.size;

    im = im.crop((0, 0, width, 430));
    im.show();
    
    driver.close();
    

  
    

