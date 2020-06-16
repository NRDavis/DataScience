import numpy as np  # used for array manipulation
import matplotlib.pyplot as plt   # used for making visuals
import os           # used for accessing files and data
import csv          # used to read data from .txt/.csv files


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


def readData(pathName):
    # we process our data using the with block because that'll terminate the open() with a close() when done
    '''
    Data follows the format of:
        Date,Open,High,Low,Close,Volume,OpenInt

        We'll use the searchStocks() or searchETFs() functions to provide our path names
    '''
    with open(pathName, 'r') as reader:
        day = list(csv.reader(reader))      # we create an array of list objects
        return np.array(day[1:])        # returns numpy array, skips first row including column names

'''
Within this project, we're going to perform historical analysis on the stock data accumulated between about 2005
and 2017. Data obtained from Kaggle data set.

The user will type in the symbolic name of a stock, the application will find the pertinent data and then return a 
visualization of the dataset.

each of the stock documents within our folder is given by it's symbolic name as follows
       "<symbol-name>.us.txt"
'''
