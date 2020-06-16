#print("This is the current working directory:"+cwd)
print("Enter a stock symbol: ")
sym = input()
print(searchStocks(sym))

print("\n\nEnter an ETF symbol:")
etf = input()
print(searchETFs(etf))