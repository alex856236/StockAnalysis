import requests
from collections import namedtuple
from io import StringIO
import pandas as pd


AllQuote = namedtuple('DateQuote', ['sid', 'name', 'volume', 'transactions', 'value',
                                    'open', 'high', 'low', 'close', 'plusmn', 'change',
                                    'lBuy', 'lBuyAmount', 'lSale', 'lSaleAmount', 'pe_ratio'])
StockQuote = namedtuple('Quote', ['date', 'volume', 'value', 'open', 'high', 'low', 'close',
                                  ])

def getAllQuote(date: str):
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


def getStockQuote(sid: str, date: str):
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=20190101&stockNo=2330'
    params = {'stockNo': sid,
              'date': date,
              'response': 'json'}

    req = requests.get(url, params=params)

data = getAllQuote('20180131')
df = pd.DataFrame(data)
print(df)
