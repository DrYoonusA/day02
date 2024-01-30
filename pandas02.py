# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:24:39 2024

@author: yabrahams
"""

import pandas
file = pandas.read_csv("iris.csv")
print(file)

print(file.info())
print(file.describe())
