import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr

f20 = pd.read_csv('players_20.csv', sep = ',')

x = list(zip(f20['potential'], f20['overall'], f20['age'], f20['international_reputation']))
y = f20['value_eur']

reg = lr().fit(x, y)

#print('R^2 = ', reg.score(x, y))
plt.ylabel('Observeret værdi i mio. euro')
plt.xlabel('Modelleret værdi i mio. euro')
plt.plot(reg.predict(x)/1e6,y/1e6,'b.', alpha=0.5)
plt.plot(reg.predict(x)/1e6,reg.predict(x)/1e6,'r-')

coords = [[8.5,20],[14.5,27],[21.5,34],[27.5,41],[33.5,48]]

for i in range(5):
    plt.annotate(r"$Omdømme: " + str(i+1) + "$", 
             xy=coords[i], 
             rotation=70,
             xycoords="data",
             xytext=[-20,5],
             textcoords="offset points")

plt.tight_layout()
plt.grid()
#plt.savefig('grafer/regression/reg_pot_ov_ag_rep.pdf')
plt.show()