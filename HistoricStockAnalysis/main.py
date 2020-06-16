import numpy as np  # used for array manipulation
import matplotlib.pyplot as plt   # used for making visuals
import os           # used for accessing files and data
import csv          # used to read data from .txt/.csv files


'''
Within this project, we're going to perform historical analysis on the stock data accumulated between about 2005
and 2017. Data obtained from Kaggle data set.

The user will type in the symbolic name of a stock, the application will find the pertinent data and then return a 
visualization of the dataset.
'''


# each of the stock documents within our folder is given by it's symbolic name as follows
#       "<symbol-name>.us.txt"

    # we search for a symbol name within our Stocks Folder, if it exists, we return path, else return none
def searchStocks(symbol):
    symPath = os.path.join(os.getcwd() + os.sep, "Stocks", symbol.lower()+".us.txt")        #os.sep determines the best
    if not os.path.isfile(symPath):
        print("File "+symPath+" does not exist")
        return None
    else:
        return symPath      # returns proper path to respective stock

    # if data for the symbol exists - return path. Else, print statement and return None
def searchETFs(symbol):
    symPath = os.path.join(os.getcwd() + os.sep, "ETFs", symbol.lower() +".us.txt")
    if not os.path.isfile(symPath):
        print("File "+symPath+" does not exist")
        return None
    else:
        return symPath

'''
Data follows the format of:
    Date,Open,High,Low,Close,Volume,OpenInt
    
    We'll use the searchStocks() or searchETFs() functions to provide our path names
'''
def readData(pathName):
    # we process our data using the with block because that'll terminate the open() with a close() when done
    with open(pathName, 'r') as reader:
        day = list(csv.reader(reader))      # we create an array of list objects
        return np.array(day[1:])        # returns numpy array, skips first row including column names


# we define a dictionary in a manner similar to cpp enumerations


def plotVar(numArr, string):
    #print(b[0:20])
    varDict = {"date": 0, "open": 1, "high": 2, "low": 3, "close": 4, "volume": 5, "openint": 6}
    itemList = []   # list
    for i in range(0,20):
        print(numArr[i][varDict.get(string.lower())])
        itemList.append(numArr[i][varDict.get(string.lower())])

    plt.plot(itemList)
    plt.ylabel("some number's")
    plt.show()
    return



print("Enter a stock symbol:")
sym = input()
fileName = searchStocks(sym)
b = readData(fileName)


# when given a symbol by the user, we want to keep the processed data around
plotVar(b, "open")
