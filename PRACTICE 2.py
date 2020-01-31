#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:02:40 2019

@author: ibidapo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#numbera=float(input("Number:"))

def num():
    global numbera
    if numbera % 2 == 0:
        
        print("even")
        
    else:
        print("odd")
#num()

file="BD_Master.xlsx"
body_df=pd.read_excel(file)

print(body_df.info())

print(body_df.iloc[:,16].value_counts())

print(body_df["HEIGHT"].describe())

print(body_df["HEIGHT"].median())

female_white=body_df["WHITE"].where(body_df["GENDER"]=='female').mean()

print(female_white)


male_white=body_df["WHITE"].where(body_df["GENDER"]=='male').mean()

print(male_white)

print(male_white-female_white)

no_missing_values_df=pd.DataFrame.copy(body_df)

no_missing_values_df=no_missing_values_df.dropna().round(3)

print(no_missing_values_df.head())


for i in no_missing_values_df.columns[2:15]:
    plt.boxplot(no_missing_values_df[i])
    plt.title(i)
    plt.show()