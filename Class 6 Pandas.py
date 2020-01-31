#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:55:49 2019

@author: ibidapo
"""

#Importing packages

import pandas as pd

#specifying a file ()
file = "diamonds_missing_values.xlsx"

#reading the file into Python through pandas
diamonds = pd.read_excel(file)


print(diamonds)

print(diamonds['carat'])

type(diamonds['carat'])
 
type(diamonds[['carat']])

#slicing
print(diamonds[['carat']])

print(diamonds['carat'][diamonds['carat']>2])

print(diamonds['price'][diamonds['color']==1]\
                          [diamonds['cut']==1])

print((diamonds.loc[:, 'color']))

#rows 50 to 101
print(diamonds.iloc[50:101,2])

print(diamonds.loc[:,'store'][diamonds['clarity']==10])

#print column names

print(diamonds.columns)