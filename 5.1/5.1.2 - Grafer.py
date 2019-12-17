import pandas as pd
import matplotlib.pyplot as plt

f20 = pd.read_csv('players_20.csv', sep=',')

def plt_graf( fil, x, y, highlight ):
        
    file = pd.read_csv(fil, sep=',')
    
    #Opretter tom liste og en tom string, til navngivning af graferne.
    label = []
    
    if type(y) == list:

        
        #Kører listen for y definitioner igennem, plotter og tjekker navnene.
        for i in range(len(y)):
            string_to_list = []
            list_to_string = ''
                    
            
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
    plt.ylabel('Mentalitet') #Kommenteres ud hvis det er grafen for pace og positiniong der plottes
    plt.grid( True )
    plt.show()
    
plt_graf('players_20.csv', 'age', ['mentality_aggression', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure', 'mentality_interceptions'], [1,3])
plt_graf('players_20.csv', 'age', ['pace', 'mentality_positioning'], [0, 1])
