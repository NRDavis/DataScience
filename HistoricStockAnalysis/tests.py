#print("This is the current working directory:"+cwd)
print("Enter a stock symbol: ")
sym = input()
print(searchStocks(sym))

print("\n\nEnter an ETF symbol:")
etf = input()
print(searchETFs(etf))





print("Enter a stock symbol:")
sym = input()
fileName = searchStocks(sym)
b = readData(fileName)

print("we've obtained our numpy array.")
for i in range(0, 20):
    print(b[i])