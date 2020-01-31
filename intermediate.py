#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:58:22 2019

@author: ibidapo
"""

import matplotlib.pyplot as plt

year =[1950,1970, 1990, 2010]

pop =[2.519,3.692,5.263,6.972]

plt.plot(year,pop)

plt.show()

plt.scatter(year,pop)

plt.show()

year =[1950,1970, 1990, 2010, 2030]

pop =[2.538, 2.57, 2.62, 2.70, 3.2]

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Populations Projections')
plt.yticks([0,2,4,6,8,10],
           ['0','2B', '4B', '6B', '8B', '10B'])
plt.show()

import pandas as pd
import matplotlib as plt

df = pd.from_excel("google_trends.xlsx")

df.plot("col1", "col2", type="hist")