import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression as lr

f20 = pd.read_csv('players_20.csv', sep = ',')
f20 = pd.DataFrame(f20.loc[f20.value_eur != 0]) #De spillere med en værdi på 0 tages ikke hensyn til i den følgende udregning

x = list(zip(f20['potential'], f20['overall'], f20['age']))
y = f20['value_eur']

reg = lr().fit(x, y) #Her udregnes regression ved hjælp af LinearRegression
predict = reg.predict(x) #Predict er den modelleret pris for hver spiller

plt.xlabel('Modelleret værdi i euro')
plt.ylabel('Observeret værdi i euro')
plt.grid()

#Nedenunder er plot koden for at få minustal til at stå på venstre side af y-aksen.
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(predict, y, 'b.', alpha=0.5)
plt.plot(predict, predict, 'r-') #Identitetslinjen

plt.show()
