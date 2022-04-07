# from ast import Break
import pandas as pd
import ccxt
import json
import os

from data_engine import DataEngine

# -- Data variable --
start_date = '2021-01-01T00:00:00'

# f = open('./data/source/pair_list.json',)
f = open('./data/source/pair_list_all.json',)
pair_list = json.load(f)
f.close()

# f = open('./data/source/timeframe_list.json',)
f = open('./data/source/timeframe_list_all.json',)
timeframe_list = json.load(f)
f.close()

# -- Instance class --
dataEngine = DataEngine(session=ccxt.binance())

# -- Download data from data variable --
dataEngine.download_data(pair_list, timeframe_list, start_date)