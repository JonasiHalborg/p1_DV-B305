import matplotlib.pyplot as plt
import pandas as pd
                         
f20 = pd.read_csv('players_20.csv', sep=',')

def subplot6grouped(fil, x, y):

    file = pd.read_csv(fil, sep=',')
    fig, axs = plt.subplots(nrows=3, ncols=2, sharex=True, figsize=(10,5))
    fig.text(0.5, 0.05, 'Alder', ha='center')
    plt.subplots_adjust(hspace=0.2) 
    a = 0
    b = 0
    for i in range(len(y)):
            
        y_value= file.groupby([x])[y[i]].mean()
        staf = file.groupby([x])[y[i]].std()
        
        #a og b bestemmer hvilket plot der bruges
        if i != 0:
            a += 1
        
        if a == 2:
            a = 0
            b += 1
        
        axs[b, a].plot(y_value + staf, 'b:')
        axs[b, a].plot(y_value, 'b-')
        axs[b, a].plot(y_value - staf, 'b:')
        axs[b, a].plot([16, 42], [20, 80], alpha=0) #Plotter her usynglige grafer for at lave akserne ens i hver subplot
        axs[b, a].set_ylabel(y[i])
        axs[b, a].grid(True)
        


    fig.legend(['Gennemsnit + 1 Standardafvigelse', 'Gennemsnit', 'Gennemsnit - 1 Standardafvigelse'], loc=9, borderaxespad=0.001, framealpha=0)
    
    plt.show()

subplot6grouped('players_20.csv', 'age', ['pace','shooting', 'passing', 'dribbling', 'defending', 'physic'])

