import numpy as np
import matplotlib

import os           # used for accessing files and data


'''
Within this project, we're going to perform historical analysis on the stock data accumulated between about 2005
and 2017.

The user will type in the symbolic name of a stock, the application will find the pertinent data and then return a 
visualization of the dataset.
'''

Stocks = "Stocks"
ETFs = "ETFs"
Data = "Data"
cwd = os.getcwd()       # we save the current working directory (cwd) to a string
                        # from the cwd, we can obtain open the Stocks or ETFs folders

print(os.path.join(cwd + os.sep, Stocks))
                        # This demonstrates how we can make filepaths using os.path methods

# each of the stock documents within our folder is given by it's symbolic name as follows
#       "<symbol-name>.us.txt"


def searchStock(symbol):
    symPath = os.path.join(cwd + os.sep, Stocks, symbol)        #os.sep determines the best
    return symPath


#print("This is the current working directory:"+cwd)
print("Enter a stock symbol: ")
sym = input()
print(searchStock(sym))

