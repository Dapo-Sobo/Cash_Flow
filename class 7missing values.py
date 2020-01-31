#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:44:43 2019

@author: ibidapo
"""
#data science essentials
import pandas as pd 

#data visualization
import matplotlib.pyplot as plt

#reading a file
file = 'diamonds_missing_values.xlsx'

#reading the file into python through pandas
diamonds=pd.read_excel(file)

print("""
      \n 
      """)

#printing the first 5 rows of the data
print(diamonds.head(n=5))

print("""
      \n 
      """)
#to display null statement or missing value
print(diamonds.isnull().sum())

print("""
      \n 
      """)

print(diamonds.isnull().sum().sum())

print("""
      \n 
      """)

print(diamonds.sum() )

print("""
      \n 
      """)

print(diamonds.isnull().sum().sum())

print("""
      \n 
      """)

print(len(diamonds))

print("""
      \n 
      """)
#Percentage of missing values aggreagate
print(diamonds.isnull().sum().sum()/len(diamonds))

print("""
      \n 
      """)

print(diamonds.isnull().sum().sum())

print("""
      \n 
      """)
# Otoal data set
print(len(diamonds))

print("""
      \n 
      """)
#Percentage of missing values
print(diamonds.isnull().sum()/len(diamonds))

#creating missing value flags
diamonds['m_carat'] = diamonds['carat'].isnull().astype(int)
diamonds['m_color'] = diamonds['color'].isnull().astype(int)
diamonds['m_clarity'] = diamonds['clarity'].isnull().astype(int)
diamonds['m_cut'] = diamonds['cut'].isnull().astype(int)

print("""
      \n 
      """)

print(diamonds['m_carat'])
print(diamonds['m_color'])
print(diamonds['m_clarity'])
print(diamonds['m_cut'])



favorite_color = 'blue'
if 'b' in favorite_color:
    if favorite_color == 'blue':
        print ("o sa mo")