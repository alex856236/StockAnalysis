import twstock
import pandas as pd

class saveData():

    def __init__(self, stock_id, s_year, s_month, e_year, e_month):
        stock = twstock.CNYESCrawler(stock_id)

        data = stock.fetch_history_quotes(s_year, s_month, e_year, e_month)
        data_df = pd.DataFrame(data)
        print(data_df)

        # save_path = './data/%s_%d%02d_%d%02d.csv' % (stock_id, s_year, s_month, e_year, e_month)
        # data_df.to_csv(save_path, encoding='utf-8-sig')

if __name__ == '__main__':
    file = saveData(2330, 2000, 1, 2001, 1)
