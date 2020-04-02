# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:05:31 2020

@author: alyss
"""

import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob(r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\weekly_call_data\weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    all_data.describe()