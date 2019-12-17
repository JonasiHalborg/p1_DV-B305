# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:55:52 2019

@author: jonas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Indlæser filen og sætter adskillelsen til ","
f15=pd.read_csv('players_15.csv', sep=',')
f20=pd.read_csv('players_20.csv', sep=',')
"""
# 2 funktioner som først laver en gruppe med de spillere som har samme alder
# Bruger .groupby til at lave "age" om til index og tilføjer "potential" og "overall" som kollonne
f20_pot = f20[f20.age <= 35].groupby(['age'])['potential'].mean()
f20_over = f20[f20.age <= 35].groupby(['age'])['overall'].mean()

#pd.concat Kombinerer 2 serier til en dataframe og ændrer ikke stregenes indekser
f20_bed_alder = pd.concat([f20_pot, f20_over], axis=1)
#Dette er meget praktisk når man skal have flere grafer
"""
f20_bed_alder = f20[f20.age <= 35].groupby(['age'])['potential',"overall"].mean()

"""
#Gør det samme med FIFA 15
f15_pot = f15[f15.age <= 35].groupby(['age'])['potential'].mean()
f15_over = f15[f15.age <= 35].groupby(['age'])['overall'].mean()
f15_bed_alder = pd.concat([f15_pot, f15_over], axis=1)
"""

f15_bed_alder = f15[f15.age <= 35].groupby(['age'])['potential',"overall"].mean()

#Dette stykke kode gør at jeg kan ændre størrelsen på figuren
#fig, axe returnerer en tuple 
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,4.5))

#Alt muligt MAtpslopplipplop
plt.plot(f20_bed_alder)
plt.plot(f15_bed_alder)
plt.legend(["FIFA 20 - potentiale","FIFA 20 - overall", "FIFA 15 - potentiale","FIFA 15 - overall"], loc=8)
plt.axis([16,35,52,78])
plt.xticks(np.arange(16,36,step=2))
plt.ylabel('Bedømmelse', fontsize=12)
plt.xlabel('Alder', fontsize=13)
plt.grid(True)
plt.annotate(r"$Sammenfletning$", 
             xy=[28,67.259887], 
             xycoords="data",
             xytext=[10,-40],
             fontsize=12,
             textcoords="offset points",
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.3")
)
plt.annotate(r"$Sammenfletning$", 
             xy=[31,69.938042], 
             xycoords="data",
             xytext=[-60,30],
             fontsize=12,
             textcoords="offset points",
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2")
)
plt.savefig('gen_bed.pdf')

