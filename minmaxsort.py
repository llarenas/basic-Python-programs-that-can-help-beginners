'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''


stocks = {

    'goog': 555.54,
    'yahoo': 598.34,
    'fb': 25.54,
    'aapl': 105.54



}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))
