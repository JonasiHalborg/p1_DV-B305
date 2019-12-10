# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:53:55 2019

@author: magnu
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f20 = pd.read_csv('players_20.csv', sep=',')

def plt_graf( fil, x, y, plot_style, title, highlight ):
        
    #Definerer filen efter indtastede "fil" i funktionskaldet.
    file = pd.read_csv(fil, sep=',')
    
    #Opretter to tomme lister og en tom string, til navngivning af graferne.
    label = []
    
    #Tjekker om y er en liste eller tuple, for at kunne behandle dataet
    #efter hensigten.
    if type(y) == tuple or type(y) == list:
        if type(plot_style) == tuple or type(plot_style) == list:
            if len( plot_style ) < len( y ):
                print('\nWarning!\nLength of plot_style is less then length of y\n'
                      'Extend plot_style by:' + str(len( y ) - len( plot_style )))
        
        #Kører listen for y definitioner igennem, plotter og tjekker navnene.
        for i in range(len(y)):
            string_to_list = []
            list_to_string = ''
            #Tjekker hvordan man vil have sine grafer plottet.
            if type(plot_style) == tuple or type(plot_style) == list:
                if len( plot_style ) < len( y ):
                    if i == highlight[0]:
                        plt.plot( file.groupby([x])[y[i]].mean(), linewidth=highlight[1] )
                    else:
                        plt.plot( file.groupby([x])[y[i]].mean() )
                    
                
                else:
                    plt.plot( file.groupby([x])[y[i]].mean(), plot_style[i] )
            
            else:
                if i == highlight[0]:
                    plt.plot( file.groupby([x])[y[i]].mean(), linewidth=highlight[1] )
                else:
                    plt.plot( file.groupby([x])[y[i]].mean() )
                
            
            
            #Tjekker om der er en "_" titlen for y-værdierne, erstatter
            #med "-", og opretter en label liste for hver graf.
            if '_' in y[i]:
                for digit in y[i]:
                    string_to_list.append( digit )
                
                for digit in string_to_list:
                    if digit == '_':
                        list_to_string += '-'
                    
                    else:
                        list_to_string += digit
                
                label.append( '$' + list_to_string[10:]+ '$' )
              
            else:
                label.append( '$' + str(y[i]) + '$' )
    
    plt.legend(label)
    plt.xlabel('Alder')
    plt.ylabel('Mentalitet')
    plt.grid( True )
    #plt.savefig( title+ '.pdf' )
    plt.show()
    
plt_graf('players_20.csv', 'age', ['mentality_aggression', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure', 'mentality_interceptions'], '', 'Alderens virkning på mental', [1,3])
#plt_graf('players_20.csv', 'age', ['pace'], '', 'Pacefuckers', [0, 1]) #Kan forklare hvorfor mentality-positioning bliver så dårlig med alderen i den overstående graf
plt_graf('players_20.csv', 'age', ['pace', 'mentality_positioning'], '', 'he',[0, 1])
