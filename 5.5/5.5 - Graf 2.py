import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as lr

#Denne graf, er i bund og grund den samme som den uploadet fil 5.5 - Graf 1, blot der er gjort brug af np.exp og np.log.
f20 = pd.read_csv('players_20.csv', sep = ',')
f20 = pd.DataFrame(f20.loc[f20.value_eur != 0])

x = list(zip(f20['potential'], f20['overall'], f20['age']))
y = np.log(f20['value_eur'])

reg = lr().fit(x, y)
predict = reg.predict(x)

plt.xlabel('Modelleret værdi i euro')
plt.ylabel('Observeret værdi i euro')
plt.grid()

plt.plot(np.exp(predict), np.exp(y), 'b.', alpha=0.5)
plt.plot(np.exp(predict), np.exp(predict), 'r-')

plt.show()
