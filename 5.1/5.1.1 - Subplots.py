# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:58:31 2019

@author: magnu
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
                         
#Indlæser filen og sætter adskillelsen til ","
f20 = pd.read_csv('players_20.csv', sep=',')


def sekssubplots(fil, x, y):
    
    file = pd.read_csv(fil, sep=',')
                       
    plt.figure( figsize = (16, 10), dpi=160)
    
    
    for i in range(len(y)):
            
        y_value= file.groupby([x])[y[i]].mean()
        staf = file.groupby([x])[y[i]].std()
            
        c = i + 1
        plt.subplot(3, 2, c)
            
        plt.plot(y_value + staf)
        plt.plot(y_value)
        plt.plot( y_value - staf)
        plt.xlabel('Age')
        plt.ylabel(y[i]) 
        plt.legend(['+Standardafvigelse', 'Gennemsnit', '- Standardafvigelse'], framealpha=0)
          

def subplot6grouped(fil, x, y):

    file = pd.read_csv(fil, sep=',')
    fig, axs = plt.subplots(nrows=3, ncols=2, sharex=True, figsize=(10,5))
    fig.text(0.5, 0.05, 'Alder', ha='center')
    plt.subplots_adjust(hspace=0.2) # Højden mellem graferne
    a = 0
    b = 0
    for i in range(len(y)):
            
        y_value= file.groupby([x])[y[i]].mean()
        staf = file.groupby([x])[y[i]].std()
        
        if i != 0:
            a += 1
        
        if a == 2:
            a = 0
            b += 1
        
        axs[b, a].plot(y_value + staf, 'b:')
        axs[b, a].plot(y_value, 'b-')
        axs[b, a].plot(y_value - staf, 'b:')
        axs[b, a].set_ylabel(y[i])
        axs[b, a].grid(True)
        


    fig.legend(['Gennemsnit + 1 Standardafvigelse', 'Gennemsnit', 'Gennemsnit - 1 Standardafvigelse'], loc=9, borderaxespad=0.001, framealpha=0)
    #plt.savefig('Alder_kom.pdf')

subplot6grouped('players_20.csv', 'age', ['pace','shooting', 'passing', 'dribbling', 'defending', 'physic'])

