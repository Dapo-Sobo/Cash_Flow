#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:55:14 2019

@author: ibidapo
"""

x = [4, 4, 2, 1, 1, 6]



print(x[5] + x[4])


import numpy as np
z = np.array([[4, 0, 5], 
              [2, 8, 4]])

print(z[0][2])


x = ["a", "b", "c"]

print(x[1])

np_x = np.array(x)
print(np_x[1])



np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)


print(np_mat + np.array([10, 10]))


print(np_mat + np_mat)

print(np_mat + 10)

x = [1, 4, 8, 10, 12]

print(np.mean(x))

print(np.median(x))

# Import numpy
import numpy as np

positions = ['GK', 'M', 'A', 'D']

heights = [191, 184, 185, 180]
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)

np_heights=np.array(heights)


# Heights of the goalkeepers: gk_heights
gk_heights=np_heights[np_positions=='GK']

print ("gk heights:", gk_heights)

# Heights of the other players: other_heights
other_heights =np_heights[np_positions!= 'GK']

print ("other heights:", other_heights)

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))

z = [11, 12, 13, 14]
y = z
y[2:4] = [15, 16]
print(z)


r = np.array([14, 21, 24, 24])
s = np.array([12, 6, 23, 29])
t = np.array([r, s])


z = np.array([[5, 9, 8], 
              [9, 0, 6],[7,6,5]])
print(z[1:,1:])

d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}
print(d['two'])


d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}
