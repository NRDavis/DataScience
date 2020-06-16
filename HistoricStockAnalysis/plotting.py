import numpy as np  # used for array manipulation
import matplotlib.pyplot as plt   # used for making visuals



def plotVar(numArr, string):
    # we define a dictionary in a manner similar to cpp enumerations
    varDict = {"date": 0, "open": 1, "high": 2, "low": 3, "close": 4, "volume": 5, "openint": 6}
    revDict = {0: "Date", 1: "Open", 2: "High", 3: "Low", 4: "Close", 5: "Volume", 6: "OpenInt"}

    if not string.lower() in varDict:
        print("Variable not defined - cannot search data")
        return          # if we don't receive an acceptable input string, we print a statement are return
    elif string.lower() == "date":
        print("There is not point in displaying the date variable graphically")
        return

    itemList = []   # list
    rangeList = []

    for i in range(0, len(numArr)):
        itemList.append(float(numArr[i][varDict.get(string.lower())]))
        rangeList.append(i)

    plt.plot(rangeList, itemList)
    plt.ylabel(revDict.get(varDict.get(string)))
    plt.xticks([min(rangeList), max(rangeList)])
    plt.yticks([min(itemList), max(itemList)])
    plt.show()                                      # we display the item
    return


def plotSave(numArr, string, symbol):
    varDict = {"date": 0, "open": 1, "high": 2, "low": 3, "close": 4, "volume": 5, "openint": 6}
    revDict = {0: "Date", 1: "Open", 2: "High", 3: "Low", 4: "Close", 5: "Volume", 6: "OpenInt"}

    if not string.lower() in varDict:
        print("Variable not defined - cannot search data")
        return          # if we don't receive an acceptable input string, we print a statement are return
    elif string.lower() == "date":
        print("There is not point in displaying the date variable graphically")
        return

    itemList = []   # list
    rangeList = []

    for i in range(0, len(numArr)):
        itemList.append(float(numArr[i][varDict.get(string.lower())]))
        rangeList.append(i)

    plt.plot(rangeList, itemList)
    plt.ylabel(revDict.get(varDict.get(string)))
    plt.xticks([min(rangeList), max(rangeList)])
    plt.yticks([min(itemList), max(itemList)])
    save = str(symbol.upper()) +"-"+str(string)+ ".png"
    plt.savefig(save)
    return

