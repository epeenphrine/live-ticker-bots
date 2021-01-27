#%% test api
import requests
res = requests.get('https://ql.stocktwits.com/batch?symbols=gme').json()
print(res)