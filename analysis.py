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

#update database if the data is 1 day old
if datetime.now() - timedelta(days = 0) >= datetime.fromtimestamp(getmtime('crypto.db')):
    create_database()
    
conn = sqlite3.connect('crypto.db')
btc = pd.read_sql_query("select Date, price, transactions from xlm;", conn, index_col = 'Date', parse_dates = ['Date'])
