#%%
import requests
import pandas as pd
import bs4 as bs
import json
import time
CHANGE_COLUMNS= ['name', 'last', 'change%'] 
def make_req_and_make_df_dict(url):
    """
    make requests and then pass to pandas dataframe and then convert to dictionary
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
        }
        res = requests.get(url,headers=headers).content
        df = pd.read_html(res)[0]
        df.drop(columns=["Unnamed: 0", 'Month', 'High', 'Low', 'Chg.','Time', 'Unnamed: 9'], axis=1, inplace=True)
        df.columns = CHANGE_COLUMNS 
        df_dict =  df.to_dict('records')
        return df_dict 
    except:
        print(f'ran into errors in make_req for URL: {url}')
        return None 
def make_req_and_make_df_dict_crypto(url):
    """
    same thing for, but for crypto
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
        }
        res = requests.get(url,headers=headers).content
        df = pd.read_html(res)[0]
        df.drop(columns=["#", "Unnamed: 1", 'Name', 'Market Cap', 'Vol (24H)', 'Total Vol', 'Chg (7D)'],axis=1, inplace=True)
        df.columns = CHANGE_COLUMNS 
        df_dict =  df.to_dict('records')
        return df_dict 
    except:
        print(f'ran into errors in make_req for URL: {url}')
        return None 

def make_req_and_make_df_dict_bonds(url):
    """
    same thing for, but for crypto
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
        }
        res = requests.get(url,headers=headers).content
        df = pd.read_html(res)[0]
        df.drop(columns=["Unnamed: 0", 'Prev.', 'High', 'Low', 'Time','Chg.', 'Unnamed: 9'],axis=1, inplace=True)
        df.columns = CHANGE_COLUMNS 
        df_dict =  df.to_dict('records')
        return df_dict 
    except:
        print(f'ran into errors in make_req for URL: {url}')
        return None 

def wrangle_data():
    ## regular market stuff
    URLS = [ 
        'https://www.investing.com/indices/indices-futures', #futures
        'https://www.investing.com/currencies/fx-futures', #currency 
        'https://www.investing.com/commodities/real-time-futures', #commodity
    ]

    ## crypto
    CRYPTO_URL ='https://www.investing.com/crypto/currencies' 
    ##bonds 
    RATES_BONDS_URL = 'https://www.investing.com/rates-bonds/'
    df_dict_list = []
    for url in URLS:
        try:
            df_dict = make_req_and_make_df_dict(url)
            df_dict_list.append(df_dict)
        except: 
            print(f'ran into errors trying to get {url}')
            df_dict_list.append(None)
    try: 
        df_dict = make_req_and_make_df_dict_crypto(CRYPTO_URL) 
        df_dict_list.append(df_dict)
    except:
        print(f'ran into errors trying to get {CRYPTO_URL}')
        df_dict_list.append(None)
    try: 
        df_dict = make_req_and_make_df_dict_bonds(RATES_BONDS_URL) 
        df_dict_list.append(df_dict)
    except:
        print(f'ran into errors trying to get {RATES_BONDS_URL}')
        df_dict_list.append(None)
    data = {
      'dow': None,
      'es': None,
      'nas': None,
      'dxy': None,
      'us10y': None,
      'silver': None,
      'vix': None,
      'btc': None,
      'eth': None,
      'link': None,
    }
    for df_dicts in df_dict_list:
        if df_dicts:
            if not data['dow']:
                data['dow'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US 30'][0]
            if not data['es']:
                data['es'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US 500'][0]
            if not data['nas']:
                data['nas'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'US Tech 100'][0]
            if not data['vix']:
                data['vix'] = [df_dict for df_dict in df_dicts if df_dict['name'] == 'S&P 500 VIX'][0]
            if not data['dxy']:
                check_for_dxy = [df_dict for df_dict in df_dicts if df_dict['name'] == 'Dollar Index']
                if check_for_dxy:
                    data['dxy'] = check_for_dxy[0]
            if not data['us10y']:
                check_for_us10y= [df_dict for df_dict in df_dicts if df_dict['name'] == 'U.S. 10Y']
                if check_for_us10y:
                    data['us10y'] = check_for_us10y[0]
            if not data['silver']:
                check_for_silver = [df_dict for df_dict in df_dicts if df_dict['name'] == 'Silver']
                if check_for_silver:
                    data['silver'] = check_for_silver[0]
            if not data['btc']:
                check_for_btc = [df_dict for df_dict in df_dicts if df_dict['name'] == 'BTC']
                if check_for_btc:
                    data['btc'] = check_for_btc[0]
            if not data['eth']:
                check_for_eth = [df_dict for df_dict in df_dicts if df_dict['name'] == 'ETH']
                if check_for_eth:
                    data['eth'] = check_for_eth[0]
            if not data['link']:
                check_for_link = [df_dict for df_dict in df_dicts if df_dict['name'] == 'LINK']
                if check_for_link:
                    data['link'] = check_for_link[0]

    return data
testing = wrangle_data()
print(testing)