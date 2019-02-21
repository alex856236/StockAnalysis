import requests
import pandas as pd
import time
from collections import namedtuple


AllQuote = namedtuple('DateQuote', ['sid', 'name', 'volume', 'transactions', 'value',
                                    'open', 'high', 'low', 'close', 'plusmn', 'change',
                                    'lBuy', 'lBuyAmount', 'lSale', 'lSaleAmount', 'pe_ratio'])
StockQuote = namedtuple('Quote', ['date', 'volume', 'value', 'open', 'high', 'low', 'close', 'change', 'amount'])


def getAllQuote(date):
    print('get ' + str(date) + ' quote')
    url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALL'
    params = {'date': date,
              'response': 'csv',
              'type': 'ALL'}

    req = requests.get(url, params=params)
    all_data = req.text.split('\n')

    stock_data = [row for row in all_data
                    if len(row.split('",')) == 17 and row[0] != '='][1:]

    date_quote = [AllQuote(*d.split('",')[:-1]) for d in stock_data]

    return date_quote


def getStockQuote(sid, year, month):
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY'
    params = {'stockNo': sid,
              'date': '%d%02d01' % (year, month),
              'response': 'json'}

    req = requests.get(url, params=params)
    data = req.json()
    if data['stat'] == 'OK':
        return [StockQuote(*row) for row in data['data']]
    else:
        return 0

# data = getAllQuote('20180131')
data = getStockQuote(2330, 2018, 12)
df = pd.DataFrame(data)
print(df)
