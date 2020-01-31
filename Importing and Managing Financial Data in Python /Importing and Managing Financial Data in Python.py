#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 02:05:12 2020

@author: ibidapo
"""

# Import pandas library
import pandas as pd
#from pandas_datareader.data import DataReader
from datetime import date

# Import the data
nasdaq = pd.read_csv('nasdaq-listings.csv', 
                      na_values ='NAN', 
                      parse_dates=['Last Update'])
# Display first 10 rows

print(nasdaq.head(10))

# Inspect nasdaq
nasdaq.info()


# Create pd.ExcelFile() object
xls = pd.ExcelFile('listings.xlsx')

# Extract sheet names and store in exchanges
exchanges = xls.sheet_names

# Create listings dictionary with all sheet data
listings = pd.read_excel(xls, sheet_name=exchanges, na_values='n/a')

# Inspect NASDAQ listings
listings['nasdaq'].info()

# Import the NYSE and NASDAQ listings
nyse = pd.read_excel('listings.xlsx', sheet_name='nyse', na_values='n/a')
nasdaq = pd.read_excel('listings.xlsx', sheet_name='nasdaq', na_values='n/a')

# Inspect nyse and nasdaq
nyse.info()
nasdaq.info()

# Add Exchange reference columns
nyse['Exchange'] = 'NYSE'
nasdaq['nasdaq'] = 'NASDAQ'

# Concatenate DataFrames  
combined_listings = pd.concat([nyse, nasdaq]) 

# Set start and end dates
start = date(2016, 1, 1)
end = date(2016, 12, 31)

# Set the ticker
ticker = 'AAPL'

# Set the data source
data_source = 'iex'

# Import the stock prices
#stock_prices = DataReader(ticker, data_source, start, end)

# Display and inspect the result
#print(stock_prices.head())
#stock_prices.info()

"""
Here, you will use this new data source to visualize the gold price trend over the 
last 50 years, specifically,
the Gold Fixing Price 10:30 AM (London time) in London Bullion Market, in US Dollars. 
DataReader, date, pandas as pd, and matplotlib.pyplot as plt have been imported.
"""

#Getting ticker for the largest company
nyse = pd.read_excel('listings.xlsx',sheet_name='nyse',na_values='n/a')
nyse = nyse.sort_values('Market Capitalization', ascending = False)
nyse[['Stock Symbol','Company Name']].head(3)

print(listings.head(10))

# Select companies in Consumer Services
consumer_services = listings[listings.Sector == 'Consumer Services']

# Sort consumer_services by market cap
consumer_services2 = consumer_services.sort_values('Market Capitalization', ascending=False)

# Display first 5 rows of designated columns
print(consumer_services2[['Company Name', 'Exchange', 'Market Capitalization']].head())


## Sumarising Data ##

#Import the data
income=pd.read_csv('per_capita_income.csv')

#Inspect the result
income.info()

income.head()

#Sort the data by income
income = income.sort_values('Income per Capita',ascending = False)

# Calculate the mean
print(income['Income per Capita'].mean())

# Calculate the median
print(income['Income per Capita'].median())

# Create the new column
income['Income per Capita (,000)'] = income['Income per Capita']//1000

# Calculate the mode of the new column
income['Income per Capita (,000)'].mode()

help(nyse.sub())
