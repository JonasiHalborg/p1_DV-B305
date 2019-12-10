# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:25:10 2019

@author: magnu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f20 = pd.read_csv('players_20.csv', sep=',')

age = sorted(f20['age'])
age_count = dict()
for i in age:
    age_count[i] = age_count.get(i, 0) +1 

x_value = list(age_count.keys())
y_value = list(age_count.values())
plt.minorticks_on()
plt.bar(x_value, y_value)
plt.xlabel('Alder')
plt.ylabel('Antal spillere')
#plt.savefig('Alder_rep.pdf')
plt.show()

