#API key for finnhub.io: bu5icf748v6qku33udt0
#API doc: https://finnhub.io/docs/api

#get previous close price, open price, and current price
import finnhub
import time
from datetime import date

# Setup client
finnhub_client = finnhub.Client(api_key="bu5icf748v6qku33udt0")

quoteData = open("topfif.txt", "r")
today = date.today()
date = today.strftime("%m-%d-%y")
f = open("stockdata " + date + ".txt", "a+")
print(date, file=f)
for stock in quoteData:
    time.sleep(.3)
    quote = finnhub_client.quote(stock.split("\n"))
    print(stock.split("\n")[0], "previous closing:", quote["pc"], "opening:", quote["o"], "current:", quote["c"], file=f)