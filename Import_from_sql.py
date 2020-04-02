# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:07:40 2020

@author: alyss
"""
import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:\Users\alyss\Desktop\MS BAIS\Spring 2020\ISM6419_Data_Visualization\Week_7_Python\datasets\datasets\gradedata.db'
engine = create_engine('sqlite:///C:/Users/alyss/Desktop/MS BAIS/Spring 2020/ISM6419_Data_Visualization/Week_7_Python/datasets/datasets/gradedata.db')
sql = 'SELECT * from test where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df