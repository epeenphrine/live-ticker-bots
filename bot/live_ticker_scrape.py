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

    main_url        = 'https://investing.com' 
    futures_url     = 'https://www.investing.com/indices/indices-futures'
    currency_url    = 'https://www.investing.com/currencies/fx-futures'

    main_res        =   requests.get(main_url, headers=headers).content
    futures_res     =   requests.get(futures_url, headers= headers).content
    currency_res    =   requests.get(currency_url, headers = headers).content
    

    df= pd.read_html(main_res)
    futures_df      =   pd.read_html(futures_res)
    currency_df     =   pd.read_html(currency_res)

    futures_df = futures_df[0]
    futures_df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
    futures_df.columns = change_columns
    futures_df_dict =  futures_df.to_dict('records')


    currency_df = currency_df[0]
    currency_df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
    currency_df.columns = change_columns
    currency_df_dict =  currency_df.to_dict('records')

    ### need to uncomment and run this to check index of the list of dataframes
    # count=0
    # for item in df:
    #     count +=1
    #     print("***************************")
    #     print(item)

    shitcoin= df[1]
    # print(shitcoin.columns)
    shitcoin.drop(columns=['Unnamed: 0', "Name", "Market Cap", "Vol (24H)"], axis=1, inplace=True)
    shitcoin.columns = change_columns 
    shitcoin_dict = shitcoin.to_dict("records")

    commodity= df[4] 
    commodity.drop(columns=['Name', 'Month'], axis=1, inplace=True)
    commodity.columns = change_columns
    commodity_dict = commodity.to_dict("records")

    # data = {
    #     "index":index_dict ,
    #     "shitcoin": shitcoin_dict,
    #     "commodity": commodity_dict, 
    #     "dollar" : dollar_dict
    # }

    ## cleaned data
    data = {
        'dow':      futures_df_dict[0], 
        'es':       futures_df_dict[1] ,
        'nas':      futures_df_dict[2],
        'vix':      futures_df_dict[4],
        'dollar':   currency_df_dict[0],
        'gold':     commodity_dict[0],
        'btc':      shitcoin_dict[0],
        'eth':      shitcoin_dict[1]
    }
    ## commented out incase want to save
    # with open('tickerScrape.json','w') as f:
    #     json.dump(data,f)
    return data 
scrape_live_ticker()
