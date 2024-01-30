# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:29:37 2024

@author: yabrahams
"""

import pandas

file = pandas.read_csv("diab_data.csv")

print(file)

print(file.info())

print(file.describe())