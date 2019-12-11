import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression as lr

f20 = pd.read_csv('players_20.csv', sep = ',')
f20 = pd.DataFrame(f20.loc[f20.value_eur != 0])
fig, axes = plt.subplots( 3, 2 )
fig.subplots_adjust(wspace=0.2, hspace=0.6)

c = 0
d = 0
r2 = []

for i in range(5):
    df = pd.DataFrame(f20.loc[f20.international_reputation == i+1])
        
    x = list(zip(df['potential'], df['overall'], df['age']))
    y = np.log(df['value_eur'])
    
    reg = lr().fit(x, y)
    
    y = df['value_eur']
    x = pd.DataFrame({'r':np.exp(reg.predict(x))})
    reg = lr().fit(x, y)
    
    if i != 0:
        d += 1
    
    if d == 2:
        d = 0
        c += 1
    
    axes[c,d].set_yticks([0,50,100,150])
    axes[c,d].set_xticks([0,25,50,75,100,125,150])
    axes[c,d].plot(150, 150, alpha=0)
    axes[c,d].plot(x/1e6, x/1e6, 'r-')
    axes[c,d].plot(x/1e6, y/1e6, 'b.', alpha=0.5)
    axes[c,d].set_title( 'Internationalt omdømme: ' + str(i+1) )
    axes[c,d].grid( True )
    r2.append('Omd. ' + str(i+1) + ': ' + 'R$^2$ = ' + str(round(reg.score(x, y),3)))

leg = fig.legend(r2, markerscale = 0, loc='lower right', framealpha=0)
for item in leg.legendHandles:
    item.set_visible(False)

fig.delaxes(axes[2,1])
fig.text(0.001, 0.5, 'Observeret værdi i mio. euro', va='center', rotation='vertical')
fig.text(0.4, 0.02, 'Modelleret værdi i mio. euro', va='center', rotation='horizontal')
plt.show()
