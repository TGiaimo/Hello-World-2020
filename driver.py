import os
from getdata import *
from FinanceTest import *

run()
userInput = ""
while("quit" not in userInput.lower()): #Read user Input
    userInput = input("Please enter what you want in the format \"StockSymbol month/day/year\" Example: \"AAPL 10-17-2020\" \n")

    splitInput = userInput.split(" ")
    Stock = splitInput[0]
    Date = splitInput[1]
    
    stockTemp = "stockdata " + Date + ".txt" 

    #Find Associated Data Files
    #stockData = os.path.join(r'/DataBase', stockTemp)

    #Validate Stock Data
    ZacksRec(Stock)
    CNNRec(Stock)
    if(os.path.exists(stockTemp)):
        with open(stockTemp) as f:
            stockFile = f.read()
            stockFile = stockFile.split("\n")
            for line in stockFile:
                if Stock in line:
                    print(line)
    else:
        print("Could not find Data for that stock")
