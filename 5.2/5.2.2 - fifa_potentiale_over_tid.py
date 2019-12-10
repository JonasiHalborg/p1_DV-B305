# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:55:52 2019

@author: jonas
"""

import pandas as pd
import matplotlib.pyplot as plt

#Indlæser filen og sætter adskillelsen til ","
f15=pd.read_csv('players_15.csv', sep=',')
f16=pd.read_csv('players_16.csv', sep=',')
f20=pd.read_csv('players_20.csv', sep=',')

# Fjerner kolonner fra tabellen, som vi slet ikke kommer til at bruge.
x = f15[["sofifa_id","short_name","age","overall","potential","club"]]
y = f20[["sofifa_id","short_name","age","overall","potential","club","value_eur"]]
z = f16[["sofifa_id","short_name","value_eur"]]

# Bruger .groupby til at lave "sofifa_id" om til index og tilføjer alderen som kollonne
f15_group = x.groupby(["sofifa_id"])["age"].sum()
f20_group = y.groupby(["sofifa_id"])["age"].sum()

# Bruger .concat funktionen til at samle de 2 aldere og give dem hver især deres egen column navn.
# Bruger .dropna funktionen, som fjerner alle rækker med et NaN Element. 
# Dvs. Vi fjerner de spillere som ikke har været med i Fifa 15 og Fifa 20
# Returnerer et index med de spillere som var med i Fifa 15 og Fifa 20
def sofifa_id_fifa15_20():
    f20_bed_alder = pd.concat([f15_group,f20_group], axis=1)
    f20_bed_alder.columns = ["age15","age20"]
    a = f20_bed_alder.dropna(subset=['age15', 'age20'])
    return a.index

#Jeg gør det samme med overall og potential - Virker ikke med strings.
b = f15.groupby(["sofifa_id"])["age","overall","potential"].sum()
c = f20.groupby(["sofifa_id"])["age","overall","potential"].sum()

#Samler dem og bruger så igen .dropna til at fjerne de spillere som ikke var med i FIFA 15 eller FIFA 20
d = pd.concat([b,c], axis=1)
d.columns = ["age15","overall15","potential15","age20","overall20","potential20"]
e = d.dropna(subset=["age15","overall15","potential15","age20","overall20","potential20"])

#Disse funktioner tager forskellen mellem f15 og f20 overall og skriver alt information omkring de spillere
#Som har udviklet sig mere end 27.

def udvikling_fifa15_til_fifa20(e, n):
    a = list()
    for row in range(len(e.age15)):   
        b = list(e['overall20'])[row] - list(e["overall15"])[row]
        if b >= n:
            a.append(e.index[row])
    return pd.Series(a)

f = udvikling_fifa15_til_fifa20(e, 27)

def udviklede_spillere_info(f, y):
    a = list()
    for i in range(len(f)):
        for x in range(len(y.sofifa_id)):
            if y.sofifa_id[x] == f[i]:
                a.append(y.iloc[x])  
    return pd.DataFrame(a, index=[f.index])

g = udviklede_spillere_info(f, y)
h = udviklede_spillere_info(f, x)

f20_bed_club = g.groupby(['short_name'])['potential',"overall"].mean()
#Gør det samme med FIFA 15
f15_bed_club = h.groupby(['short_name'])['potential',"overall"].mean()


#Dette stykke kode gør at jeg kan ændre størrelsen på figuren
#fig, axe returnerer en tuple 
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,5))
plt.plot(f20_bed_club, "d")
plt.plot(f15_bed_club, "d")

#Alt muligt MAtpslopplipplop
plt.legend(["FIFA 20 - potentiale","FIFA 20 - overall", "FIFA 15 - potentiale","FIFA 15 - overall"], loc=4)
plt.axis([-0.5,7.5,30,95])
plt.grid(axis="y")
plt.ylabel('Bedømmelse')
plt.xlabel('Spiller')
plt.title('Top Udvikling - FIFA 15 og FIFA 20')
plt.savefig('over_udv.pdf')
