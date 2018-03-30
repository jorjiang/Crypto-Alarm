import urllib.request as ur
import numpy as np
import pandas as pd
from datetime import datetime




topic_list = ['transactions', 'Size', 'sentbyaddress', 'difficulty',
              'hashrate', 'price', 'mining_profitability', 'sentinusd', 
              'transactionfees', 'median_transaction_fee', 'confirmationtime', 
              'marketcap', 'transactionvalue', 'mediantransactionvalue', 
              'tweets', 'activeaddresses', 'top100cap']
coin_list = 'btc eth ltc xrp bch neo etc usdt bnb trx eos iot xlm xmr ada dash icx zec omg ven qtum dgd cnd lsk xem nbt gvt waves btg nebl mtl snt srn xvg strat bcpt noah enj vibe bqx storm ldc doge sub adx wtc bcd mco eng zrx powr sc gup fct hsr trig'.split(' ')

def get_url(topic, coin):
    topic
    coin_str = coin.replace(', ', '-').replace(' ', '-')
    url = 'https://bitinfocharts.com/comparison/'+topic + '-' + coin_str+'.html'
    return url


#url = 'https://bitinfocharts.com/comparison/bitcoin-transactions.html'
def get_trait_data(topic, coin):    
    url = get_url(topic, coin)

    columns = []
    for coin_abbr in url.split('-'):
        columns.append(coin_abbr)
    columns[0] = 'Date'
    columns[-1] = columns[-1].replace('.html', '')
    
    
    
    
    def cov_date(string):
        return datetime.strptime(string, "%Y-%m-%d")
    
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    request = ur.urlopen(ur.Request(url, data=None, headers={'User-Agent': user_agent}))
    #response = urllib.request.urlopen(url)
    webContent = request.read()
    source = webContent.decode('utf-8')
    
    data_str = source.split('Dygraph(document.getElementById("container"),')[1].split(', {labels: ["Date"')[0]
    data_str = data_str.replace('new Date(', '').replace(')', '').replace('null','np.nan').replace('/', '-')
    
    data = eval(data_str)
    df = pd.DataFrame(data, columns = columns)
    df.set_index('Date')
    df.index = map(cov_date, df['Date'].values.tolist())
    df.drop(['Date'], 1, inplace = True)
    return df

def get_coin_data(topic, coin):    
    columns = []
    na_columns = []
    for i, t in enumerate(topic):
        url = 'https://bitinfocharts.com/comparison/'+ t + '-' + coin.lower()+'.html'     
        columns.append(t)
        
        
        
        
        def cov_date(string):
            return datetime.strptime(string, "%Y-%m-%d")
        
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
        request = ur.urlopen(ur.Request(url, data=None, headers={'User-Agent': user_agent}))
        #response = urllib.request.urlopen(url)
        webContent = request.read()
        source = webContent.decode('utf-8')
        
        data_str = source.split('Dygraph(document.getElementById("container"),')[1].split(', {labels: ["Date"')[0]
        data_str = data_str.replace('new Date(', '').replace(')', '').replace('null','np.nan').replace('/', '-')
        
        data = eval(data_str)
        df = data
        if data != []:
            df = pd.DataFrame(df)
            df.columns = ['Date', columns[i]]
            df = df.set_index('Date')
            if i == 0:
                df_f = df
            else:
                try:
                    df_f = df_f.join(df)
                except:
                    df_f = df
            
            df_f.index = pd.to_datetime(df_f.index)
        else:
            na_columns.append(t)
    for t in na_columns:
        df_f[t] = np.nan
    return df_f
