# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:18:34 2020

@author: alyss
"""

import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])
df

df.loc[(df['Grades'] < 0,'Grades')] = 0
df
