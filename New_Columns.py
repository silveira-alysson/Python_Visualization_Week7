# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:22:43 2020

@author: alyss
"""

import pandas as pd
Location = r"C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']
df['lettergrade'] = pd.cut(df['grade'], bins,labels=group_names)

bins = [0, 80, 100]
group_pass_fail = ['Fail','Pass']
df['passfail'] = pd.cut(df['grade'], bins,labels=group_pass_fail)
df