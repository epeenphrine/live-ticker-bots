#%%
import requests

def make_req(tickers):
    """
    make request to stocktwits api and check for extended
    """
    res = requests.get(f'https://ql.stocktwits.com/batch?symbols={tickers}').json()
    tickers = [ticker for ticker in res]
    return res

make_req('gme,aapl')