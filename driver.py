import os


userInput = ""
while("quit" not in userInput.lower()): #Read user Input
    userInput = input("Please enter what you want in the format \"StockSymbol month/day/year\" Example: \"AAPL 10-17-2020\" \n")

    splitInput = userInput.split(" ")
    Stock = splitInput[0]
    Date = splitInput[1]

    stockTemp = "StockData " + Date 
    reccomendationTemp = "Reccomendations " + Date 

    #Find Associated Data Files
    stockData = os.path.join(r'/DataBase', stockTemp)
    reccomendationData = os.path.join(r'/DataBase', reccomendationTemp)

    #Validate Stock Data
    if(os.path.exists(stockData)):
        with open(stockData) as f:
            stockFile = f.read()
    else:
        print("Could not find Data for that stock")
    #Validate Reccomendation Data
    if(os.path.exists(reccomendationData)):
        with open(stockData) as f:
            stockFile = f.read()
    else:
        print("Could not find Data for that stock")
    
    