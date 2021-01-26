#%%
import requests
import pandas as pd
import bs4 as bs
import json
import time
def scrape_live_ticker():
    change_columns = ['name', 'last', 'change%'] 
    #maybe rotate user agent through a list ... 
    user_agent_list = [

    ]
    #for now single agent is ok ...
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
    }

    futures_url     = 'https://www.investing.com/indices/indices-futures'
    # currency_url    = 'https://www.investing.com/currencies/fx-futures'
    # commodity_url   = 'https://www.investing.com/commodities/real-time-futures'
    shitcoin_url    = 'https://www.investing.com/crypto/currencies'

    futures_res     =   requests.get(futures_url, headers= headers).content
    # currency_res    =   requests.get(currency_url, headers = headers).content
    # commodity_res   =   requests.get(commodity_url, headers = headers).content
    shitcoin_res    =   requests.get(shitcoin_url, headers = headers).content

    futures_df      =   pd.read_html(futures_res)
    # currency_df     =   pd.read_html(currency_res)
    # commodity_df    =   pd.read_html(commodity_res)
    shitcoin_df     =   pd.read_html(shitcoin_res)

    futures_df = futures_df[0]
    futures_df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
    futures_df.columns = change_columns
    futures_df_dict =  futures_df.to_dict('records')

    dow = [future for future in futures_df_dict if future['name'] == 'US 30'][0]
    es  = [future for future in futures_df_dict if future['name'] == 'US 500'][0]
    nas = [future for future in futures_df_dict if future['name'] == 'US Tech 100'][0]
    vix = [future for future in futures_df_dict if future['name'] == 'S&P 500 VIX'][0]

    # currency_df = currency_df[0]
    # currency_df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
    # currency_df.columns = change_columns
    # currency_df_dict =  currency_df.to_dict('records')

    # dxy = [currency for currency in currency_df_dict if currency['name'] == 'Dollar Index'][0]

    # commodity_df = commodity_df[0]
    # commodity_df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
    # commodity_df.columns = change_columns
    # commodity_df_dict =  commodity_df.to_dict('records')

    # gold = [commodity for commodity in commodity_df_dict if commodity['name'] == 'Gold'][0]

    shitcoin_df = shitcoin_df[0]
    shitcoin_df.drop(columns=["#", "Unnamed: 1", 'Name', 'Market Cap', 'Vol (24H)', 'Total Vol', 'Chg (7D)'],axis=1, inplace=True)
    shitcoin_df.columns = change_columns
    shitcoin_df_dict =  shitcoin_df.to_dict('records')

    ## too much rows ... filter this way. Might be better 
    btc = [shitcoin for shitcoin in shitcoin_df_dict if shitcoin['name']== "BTC"][0]
    eth = [shitcoin for shitcoin in shitcoin_df_dict if shitcoin['name']== "ETH"][0]


    ### need to uncomment and run this to check index of the list of dataframes
    # count=0
    # for item in df:
    #     count +=1
    #     print("***************************")
    #     print(item)

    ## cleaned data
    data = {
        'dow':      dow, 
        'es':       es,
        'nas':      nas,
        'vix':      vix,
        # 'dollar':   dxy,
        # 'gold':     gold, 
        'btc':      btc, 
        'eth':      eth 
    }
    ## commented out incase want to save
    # with open('tickerScrape.json','w') as f:
    #     json.dump(data,f)
    return data 
scrape_live_ticker()