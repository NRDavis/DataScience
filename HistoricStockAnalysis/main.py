import numpy as np  # used for array manipulation
import matplotlib.pyplot as plt   # used for making visuals
import os           # used for accessing files and data
import csv          # used to read data from .txt/.csv files


# user defined python modules
import obtain as ob             # we import all of the functions we use to search for data and read it
import plotting as pt           # functions used to display data and save it

import FrenchFama as FF         # import fama and french analysis functionality
import PriceEarnings as PE



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
    print("Enter a stock symbol:")      # prompt user for stock option
    inp = input()                       # get input from user
    fileName = ob.searchStocks(inp)     # obtain path to requested data
    b = ob.readData(fileName)           # read data into a numpy array


    # when given a symbol by the user, we want to keep the processed data around
    #pt.plotVar(b, "Open")
    #pt.plotSave(b, "Volume", inp)

    print(PE.forwardPE(50, 5, 0))
    print(PE.forwardPE(50, 5, 10))


