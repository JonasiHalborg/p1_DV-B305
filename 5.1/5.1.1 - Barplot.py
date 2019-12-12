import pandas as pd
import matplotlib.pyplot as plt

f20 = pd.read_csv('players_20.csv', sep=',')

age = sorted(f20['age'])
age_count = dict()
for i in age:
    #Her tages hver indeks i kolonnen age.
    #Den for nyligt oprettet ordbog, tæller hver gang en forekomst af en alder opstår. 
    #Ellers tilføjes alderen til ordbogen.
    age_count[i] = age_count.get(i, 0) +1 

x_value = list(age_count.keys())
y_value = list(age_count.values())

plt.minorticks_on()
plt.bar(x_value, y_value)

plt.xlabel('Alder')
plt.ylabel('Antal spillere')

plt.show()


