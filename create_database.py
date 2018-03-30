# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 08:47:28 2018

@author: beautifultroll
"""
import sqlite3
from get_git_data import get_git as gg
from readbitinfochart import get_coin_data as gc
import time
from tqdm import tqdm

def create_database():
    topic_list = ['transactions', 'Size', 'sentbyaddress', 'difficulty',
                  'hashrate', 'price', 'mining_profitability', 'sentinusd', 
                  'transactionfees', 'median_transaction_fee', 'confirmationtime', 
                  'marketcap', 'transactionvalue', 'mediantransactionvalue', 
                  'tweets', 'activeaddresses', 'top100cap']
    
    
    coin_list = 'btc eth ltc xrp bch neo etc usdt bnb trx eos iot xlm xmr ada dash icx zec omg ven qtum dgd cnd lsk xem nbt gvt waves btg nebl mtl snt srn xvg strat bcpt noah enj vibe bqx storm ldc doge sub adx wtc bcd mco eng zrx powr sc gup fct hsr trig'.split(' ')
    
    git_data = gg()
    connection = sqlite3.connect('crypto.db')
    
    for coin in tqdm(coin_list):
        coin_data = gc(topic_list, coin)
        try:
            coin_data = coin_data.join(git_data[coin.upper()])
        except:
            pass
        
        coin_data.to_sql(name = coin, con = connection, if_exists = 'replace')
        time.sleep(0.5)
    
    git_data.to_sql(name = 'github_activity', con = connection, if_exists = 'replace')
    


# =============================================================================
# def create_table(coin_name):
#     c.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(coin_name, ('Date TEXT, REAL, '.join(topic_list) + ' REAL')))
#     c = get_coin_data(topic_list, coin_name)
#     for col in topic_list:
#         sql = """INSERT INTO {} (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(coin_name, parentid, commentid, parent, comment, subreddit, int(time), score)
#         transaction_bldr(sql)
#     except Exception as e:
#         print('s0 insertion',str(e))
# =============================================================================
            


# =============================================================================
# def fetch_data():
#     git_data = gg().fillna(method = 'bfill')
#     
#     bitcoin = gc(['transactions', 'price'],'btc')
#     bitcoin = bitcoin.join(git_data['BTC'].rename('git').interpolate(), how = 'left')
# =============================================================================
