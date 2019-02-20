# coding: utf-8

import requests
import urllib.parse
import calendar
from collections import namedtuple
from bs4 import BeautifulSoup

CNYES_BASE_URL = 'http://www.cnyes.com/twstock/'
HISTORY_URL = urllib.parse.urljoin(CNYES_BASE_URL, 'ps_historyprice/')

QUOTETUPLE = namedtuple('Quotes', ['date', 'open', 'high', 'low', 'close', 'change',
                                    'increase', 'transaction', 'amount', 'pe_ratio'])


class CNYESCrawler():
    def __init__(self, sid):
        self.sid = str(sid)

    def fetch_history_quotes(self, s_year, s_month, e_year, e_month, retry=5):

        e_day = calendar.monthrange(e_year, e_month)[1]  # [0]第一天星期幾 [1]一個月有幾天
        params = {'ctl00$ContentPlaceHolder1$startText': '%d/%02d/01' % (s_year, s_month),
                  'ctl00$ContentPlaceHolder1$endText': '%d/%02d/%02d' % (e_year, e_month, e_day)}

        # 嘗試做retry次 如果不行表示成空集合
        for _ in range(retry):
            req = requests.post(HISTORY_URL+self.sid+'.htm', data=params)
            if req.status_code == 200:  # 連線成功
                stat = 1
                break
        else:  # for-else語法
            stat = 0

        if stat:
            soup = BeautifulSoup(req.content, 'html.parser')
            quotes = self.purify([row.get_text('|').split('|') for row in soup.select('.tab tr')[1:]])
            return Quotes(quotes)

    def _make_datatuple(self, data):
        data[1] = float(data[1].replace(',', ''))  # open
        data[2] = float(data[2].replace(',', ''))  # high
        data[3] = float(data[3].replace(',', ''))  # low
        data[4] = float(data[4].replace(',', ''))  # close
        data[5] = float(data[5])                   # change
        data[6] = float(data[6].replace('%', ''))  # increase
        data[7] = int(data[7].replace(',', ''))    # transaction
        data[8] = int(data[8].replace(',', ''))    # amount
        data[9] = float(data[9])                   # pe_ratio
        return QUOTETUPLE(*data)

    def purify(self, raw_data):
        return [self._make_datatuple(row) for row in raw_data]


class Quotes():

    def __init__(self, quotes):
        self.quotes = quotes
        self.fetcher

    def __iter__(self):
        return iter(self.quotes)

    @property
    def open(self):
        return [q.open for q in self.quotes]

    @property
    def high(self):
        return [q.high for q in self.quotes]

    @property
    def low(self):
        return [q.low for q in self.quotes]

    @property
    def close(self):
        return [q.close for q in self.quotes]

    @property
    def change(self):
        return [q.change for q in self.quotes]

    @property
    def increase(self):
        return [q.increase for q in self.quotes]

    @property
    def transaction(self):
        return [q.transaction for q in self.quotes]

    @property
    def amount(self):
        return [q.amount for q in self.quotes]

    @property
    def pe_ratio(self):
        return [q.pe_ratio for q in self.quotes]

