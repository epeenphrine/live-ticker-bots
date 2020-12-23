#%%
import requests
import pandas as pd
import bs4 as bs
import json
import time
def scrape_live_ticker():
    #maybe rotate user agent through a list ... 
    user_agent_list = [

    ]
    #for now single agent is ok ...
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    }
    change_columns = ['name', 'last', 'change%'] 
    res = requests.get('https://investing.com', headers=headers).content
    df= pd.read_html(res)
    ### need to uncomment and run this to check index of the list of dataframes
    # count=0
    # for item in df:
    #     count +=1
    #     print("***************************")
    #     print(item)
    index = df[7]
    index.drop(columns=[0,3,5,6], axis=1, inplace=True)
    index.columns = change_columns 
    index_dict = index.to_dict("records")

    shitcoin= df[1]
    # print(shitcoin.columns)
    shitcoin.drop(columns=['Unnamed: 0', "Name", "Market Cap", "Vol (24H)"], axis=1, inplace=True)
    shitcoin.columns = change_columns 
    shitcoin_dict = shitcoin.to_dict("records")

    commodity= df[4] 
    commodity.drop(columns=['Name', 'Month'], axis=1, inplace=True)
    commodity.columns = change_columns
    commodity_dict = commodity.to_dict("records")

    dollar = df[8]
    dollar.drop(columns=[0, 3, 5, 6], axis=1, inplace=True)
    dollar.columns = change_columns
    dollar_dict= dollar.to_dict("records")

    # data = {
    #     "index":index_dict ,
    #     "shitcoin": shitcoin_dict,
    #     "commodity": commodity_dict, 
    #     "dollar" : dollar_dict
    # }

    ## cleaned data
    data = {
        'dow': index_dict[0], 
        'es': index_dict[1] ,
        'nas': index_dict[2],
        'dollar': index_dict[-1],
        'vix': index_dict[-2],
        'gold': commodity_dict[0],
        'btc': shitcoin_dict[0],
        'eth': shitcoin_dict[1]
    }
    print(data)
    ## commented out incase want to save
    # with open('tickerScrape.json','w') as f:
    #     json.dump(data,f)
    return data 
scrape_live_ticker()
