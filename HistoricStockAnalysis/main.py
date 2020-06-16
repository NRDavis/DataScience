import numpy as np  # used for array manipulation
import matplotlib.pyplot as plt   # used for making visuals
import os           # used for accessing files and data
import csv          # used to read data from .txt/.csv files

import obtain as ob             # we import all of the functions we use to search for data and read it
import plotting as pt           # functions used to display data and save it

'''
Within this project, we're going to perform historical analysis on the stock data accumulated between about 2005
and 2017. Data obtained from Kaggle data set.

The user will type in the symbolic name of a stock, the application will find the pertinent data and then return a 
visualization of the dataset.

each of the stock documents within our folder is given by it's symbolic name as follows
       "<symbol-name>.us.txt"
'''




inp = "going"

while inp != "q":
    print("Enter a stock symbol:")
    inp = input()
    fileName = ob.searchStocks(inp)
    b = ob.readData(fileName)
    # when given a symbol by the user, we want to keep the processed data around
    pt.plotVar(b, "Open")
    #plotSave(b, "Volume", inp)
