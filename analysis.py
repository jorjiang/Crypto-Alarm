# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 04:11:48 2018

@author: beautifultroll
"""
import sqlite3

from os.path import getmtime
from datetime import timedelta, datetime
from create_database import create_database
import pandas as pd
from sklearn.preprocessing import scale 
from numpy.linalg import norm
import numpy as np

if __name__ == '__main__':
    topic_list = ['transactions', 'Size', 'sentbyaddress', 'difficulty',
                  'hashrate', 'price', 'mining_profitability', 'sentinusd', 
                  'transactionfees', 'median_transaction_fee', 'confirmationtime', 
                  'marketcap', 'transactionvalue', 'mediantransactionvalue', 
                  'tweets', 'activeaddresses', 'top100cap']
    
    
    coin_list = 'btc eth ltc xrp bch neo etc usdt bnb trx eos iot xlm xmr ada dash icx zec omg ven qtum dgd cnd lsk xem nbt gvt waves btg nebl mtl snt srn xvg strat bcpt noah enj vibe bqx storm ldc doge sub adx wtc bcd mco eng zrx powr sc gup fct hsr trig'.split(' ')
#update database if the data is 1 day old
    if datetime.now() - timedelta(days = 7) >= datetime.fromtimestamp(getmtime('crypto.db')):
        create_database()
    
    
    funda_col = ['transactions', 'sentbyaddress', 'hashrate', 'sentinusd', 'confirmationtime', 'transactionvalue',  'activeaddresses', 'git_activity']

    sent_col = ['price', 'tweets']

#fundamental evaluation for each coin
def fund_value_change(coin, days, starting_date):
    if type(starting_date) == str:
        starting_date = pd.to_datetime(starting_date)
    starting_date_index = ((starting_date  - pd.Timestamp.today()) / np.timedelta64(1, 'D')).astype(int) - 1
    
    fund_change_list = []
    for col in funda_col:
        try:
            coin_fund_scaled = scale(coin[col])
            change = coin_fund_scaled[starting_date_index] - coin_fund_scaled[starting_date_index-days]
        except Exception as e:
            print('date out of range, no historical data!')
            change = 0
        if (col == 'confirmationtime') | (col == 'median_transaction_fee'):
        #big confirmationtime and median_transaction_fee decrease utility of a coin
            fund_change_list.append(-change)
        else:
            fund_change_list.append(change)
        
    return np.sum(fund_change_list)


def sent_value_change(coin, days, starting_date):
    if type(starting_date) == str:
        starting_date = pd.to_datetime(starting_date)
    
    starting_date_index = ((starting_date  - pd.Timestamp.today()) / np.timedelta64(1, 'D')).astype(int) - 1
    fund_change_list = []


    for col in sent_col:
        try:
            coin_fund_scaled = scale(coin[col])
            change = coin_fund_scaled[starting_date_index] - coin_fund_scaled[starting_date_index-days]
        except Exception as e:
            print('date out of range, no historical data!')
            change = 0
        if (col == 'confirmationtime') | (col == 'median_transaction_fee'):
        #big confirmationtime and median_transaction_fee decrease utility of a coin
            fund_change_list.append(-change)
        else:
            fund_change_list.append(change)
        
    return np.sum(fund_change_list)          
    
#    def eula_distance(list):
#        return norm(list)
    


def get_value_all_coins(days = 30, starting_date = pd.Timestamp.today()):
    value = pd.DataFrame(columns = ['coin', 'fundamental', 'hype'])
    for coin in coin_list:
        conn = sqlite3.connect('crypto.db')
        coin_df = pd.read_sql_query("select * from {};".format(coin), conn, index_col = 'Date', parse_dates = ['Date'])
        fund_value = fund_value_change(coin_df, days, starting_date)
        sent_value = sent_value_change(coin_df, days, starting_date)
        row = pd.DataFrame([[coin, fund_value, sent_value]], columns= value.columns)
        value = pd.concat([value, row])
    return value.set_index('coin')


#xxx.hype.plot(kind = 'barh', title = 'hype', color=list(map(lambda x: 'r' if x > 0 else 'g', xxx.hype)))    
    
def get_top_value_gainer(n = 5, days = 30, starting_date = pd.Timestamp.today()):
    df = get_value_all_coins(days = days, starting_date = starting_date)
    return df.nlargest(n, 'fundamental')['fundamental']

def get_top_hyper(n = 5, days = 30, starting_date = pd.Timestamp.today()):
    df = get_value_all_coins(days = days, starting_date = starting_date)
    return df.nlargest(n, 'hype')['hype']

