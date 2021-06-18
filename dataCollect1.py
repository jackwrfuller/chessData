from main import getPlayerData
import requests
import numpy as np
import pandas as pd
import json
import matplotlib as mpl





df1 = getPlayerData('IT', 10000)
df1.to_csv('IT_stats.csv', index = False)