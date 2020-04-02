# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:32:44 2020

@author: alyss
"""

import pandas as pd
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()

import numpy as np
df['isFailing'] = np.where(df['grade']<70,'yes', 'no')
df.tail(10)

df['isFailingMale'] = np.where((df['grade']<70)
    & (df['gender'] == 'male'),'yes', 'no')
df.tail(10)

df['timemgmt'] = np.where((df['exercise']>3)
    & (df['hours'] > 17),'busy', 'not_busy')
df.tail(10)