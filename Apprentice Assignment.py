#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:30:00 2020

@author: ibidapo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("Apprentice_Chef_Dataset.xlsx")
print(df.shape)
print(df.head())
print(df.describe())

