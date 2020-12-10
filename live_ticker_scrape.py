#%%
import requests
import pandas as pd
import bs4 as bs
import json
def scrape_live_ticker():
    user_agent_list = [

    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    }

    res = requests.get('https://investing.com', headers=headers).content
    df= pd.read_html(res)
    # print(res)
    index = df[3]
    index.drop(columns=['Name'], axis=1, inplace=True)
    index.columns = ['index', 'month', 'last', 'change%']
    index_dict = index.to_dict("records")

    shitcoin= df[1]
    # print(shitcoin.columns)
    shitcoin.drop(columns=['Unnamed: 0', "Name", "Market Cap", "Vol (24H)"], axis=1, inplace=True)
    shitcoin.columns = ['shitcoin', 'price', 'change%']
    shitcoin_dict = shitcoin.to_dict("records")

    commodity= df[4] 
    commodity.drop(columns=['Name'], axis=1, inplace=True)
    commodity.columns = ['index', 'month', 'last', 'change%']
    commodity_dict = commodity.to_dict("records")

    dollar = df[8]
    dollar.drop(columns=[0, 5, 6], axis=1, inplace=True)
    dollar.columns = ['index', 'price', 'change', 'change%']
    dollar_dict= dollar.to_dict("records")

    data = {
        "index":index_dict ,
        "shitcoin": shitcoin_dict,
        "commodity": commodity_dict, 
        "dollar" : dollar_dict
    }
    # with open('tickerScrape.json','w') as f:
    #     json.dump(data,f)
    return data 
scrape_live_ticker()