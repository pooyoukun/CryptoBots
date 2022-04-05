from ast import Break
import pandas as pd
import ccxt
import json
import os

from data_engine import DataEngine

print(os.getcwd())
#Break

# -- Data variable --
f = open('./data/source/pair_list.json',)
pair_list = json.load(f)
f.close()

f = open('./data/source/timeframe_list.json',)
timeframe_list = json.load(f)
f.close()

# -- Instance class --
dataEngine = DataEngine(session=ccxt.binance())

# -- Download data from data variable --
dataEngine.update_data(pair_list, timeframe_list)