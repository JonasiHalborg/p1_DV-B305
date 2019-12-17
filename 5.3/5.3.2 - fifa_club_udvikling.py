# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:55:52 2019

@author: jonas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Indlæser filen og sætter adskillelsen til ","
f15=pd.read_csv('players_15.csv', sep=',')
f20=pd.read_csv('players_20.csv', sep=',')

x = f15[["sofifa_id","age","club","overall"]]
y = f20[["sofifa_id","age","club","overall"]]

# Bruger .groupby til at lave "sofifa_id" om til index og tilføjer klubben som kollonne
# Bruger .concat funktionen til at samle de 2 klubber og give dem hver især deres egen column navn.
# Bruger .dropna funktionen, som fjerner alle rækker med et NaN Element. 
# Dvs. Vi fjerner de spillere som ikke har været med i Fifa 15 og Fifa 20
def club15_20(x, y, alder):
    b = x[x.age <= alder].groupby("sofifa_id")["club"].agg(lambda col: ''.join(col))
    c = y.groupby("sofifa_id")["club"].agg(lambda col: ''.join(col))
    f20_bed_alder = pd.concat([b,c], axis=1)
    f20_bed_alder.columns = ["club15","club20"]
    a = f20_bed_alder.dropna(subset=["club15","club20"])
    
    return a
#Returnerer spillere under 19 års klubber i FIFA 15 og FIFA 20, uden spillerdata
#x og y er de sorterede versioner af f20 og f15.
a = club15_20(x, y, 18)

# Bruger .groupby  til at lave "sofifa_id" om til  index og tilføjer "age og "overall" som  kollonner
def sofifa_id_fifa15_20(fil1, fil2, alder):
    b = fil1[fil1.age <= alder].groupby(["sofifa_id"])["age","overall"].sum()
    c = fil2.groupby(["sofifa_id"])["age","overall"].sum()
    
    #Samler  de nye  dataframes  med .concat  og  bruger så .dropna  til at  
    #udelukke de  spillere,  som  ikke  var med i FIFA 15  eller  FIFA 20
    f20_bed_alder = pd.concat([b,c], axis=1)
    f20_bed_alder.columns = ["age15","overall15","age20","overall20"]
    a = f20_bed_alder.dropna(subset=['age15',"overall15",'age20',"overall20"])
    #Returnerer et dataframe med et almindeligt indeks
    return a

#x og y er de sorterede versioner af f20 og f15.
b = sofifa_id_fifa15_20(x, y, 18)


#Sammenligner og laver et dataframe med klub, overall i f15 og f20 af de spillere som har samme klub i FIFA 15 og FIFA 20
def sammenlign(x, y):
    x.index = np.arange(0, len(x.index))
    y.index = np.arange(0, len(y.index))
    a = list()
    b = list()
    c = list()
    for i in range(len(x.club15)):
        if x.club15[i] == x.club20[i]:
            a.append(x.club15[i])
            b.append(y.overall15[i])
            c.append(y.overall20[i])
    d = {"club" : a,
         "overall15" : b,
         "overall20" : c}
    return pd.DataFrame(d)

c = sammenlign(a, b)

#Gennemgår det sammenlignede datasæt og laver en ny kollonner med 
#forskellen på fifa 15 overall og fifa 20 overall
#Bruger .groupby til at samle klubbernes udviklingsgennemsnit 
def analyse(x):
    a = []
    for i in x.index:
        a.append(x.overall20[i] - x.overall15[i])
    x["forskel"] = a
    b = x.groupby(["club"])["forskel"].mean()
    return pd.DataFrame(b)

d = analyse(c)
#Sorterer de klubber fra med et udviklingsgennemsnit under 15
e = d[d.forskel >= 15].sort_values(by=["forskel"], ascending=True)

#Matplotlib
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,6.6))

plt.bar(e.index, e.forskel, align="center", alpha=0.5)
plt.axis([-0.5,12.5,0,30])
plt.grid(axis="y")
plt.xticks(rotation=45, horizontalalignment='right')
plt.ylabel('Gennemsnitsstigningen i overall', fontsize=11)
plt.subplots_adjust(bottom=0.25)
plt.savefig("club_udvik.pdf")
