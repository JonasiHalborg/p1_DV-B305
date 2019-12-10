# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:49:58 2019

@author: mgejl
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

def fig_plot_avg(fil, x, y):
    ordbog = {'sofifa_id' : 'Id', 'player_url' : 'Spiller URL adresse', 'short_name' : 'Navn',
              'long_name' : 'Fulde navn', 'age' : 'Alder', 'dob' : 'Foedsels dato',
              'height_cm' : 'Hoejde i cm', 'weight_kg' : 'Vaegt i kg', 'nationality' : 'Nationalitet',
              'club' : 'klub', 'overall' : 'Overall', 'potential' : 'Potential',
              'value_eur' : 'Pris i tusind euro', 'wage_eur' : 'Loen i euro',
              'player_positions' : 'Spiller Positioner', 'preferred_foot' : 'Foretrukne fod',
              'international_reputation' : 'Internationalt omdoemme', 'weak_foot' : 'Svage fod',
              'skill_moves' : 'Skill moves', 'work_rate' : 'Work Rate', 'body_type' : 'Kropstype',
              'real_face' : 'Rigtige ansigt', 'release_clause_eur' : 'Frikoebsklausul i euro',
              'player_tags' : 'Spiller tags', 'team_position' : 'Hold position',
              'team_jersey_number' : 'Hold troejenummer', 'loaned_from' : 'Laant fra',
              'joined' : 'Tilslutningsdato', 'contract_valid_until' : 'Kontraktvarighed',
              'nation_position' : 'Landsholdsposition', 'nation_jersey_number' : 'Landshold troejenummer',
              'pace' : 'Pace', 'shooting' : 'Shooting', 'passing' : 'Passing', 'dribbling' : 'Dribbling',
              'defending' : 'Defending', 'physic' : 'Physic', 'gk_diving' : 'Gk diving',
              'gk_handling' : 'Gk handling', 'gk_kicking' : 'Gk kicking', 'gk_reflexes' : 'Gk Reflexes',
              'gk_speed' : 'Gk speed', 'gk_positioning' : 'Gk positioning', 'player_traits' : 'Spilleregenskaber',
              'attacking_crossing' : 'Attacking crossing', 'attacking_finishing' : 'Attacking finishing',
              'attacking_heading_accuracy' : 'Attacking heading accuracy',
              'attacking_short_passing' : 'Attacking short passing', 'attacking_volleys' : 'Attacking volleys',
              'skill_dribbling' : 'Skill dribbling', 'skill_curve' : 'Skill curve',
              'skill_fk_accuracy' : 'Skill fk accuracy', 'skill_long_passing' : 'skill_long_passing',
              'skill_ball_control' : 'Skill ball control', 'movement_acceleration' : 'Movement acceleration',
              'movement_sprint_speed' : 'Movement sprint speed', 'movement_agility' : 'Movement agility',
              'movement_reactions' : 'Movement reactions', 'movement_balance' : 'Movement balance',
              'power_shot_power' : 'Power shot power', 'power_jumping' : 'Power jumping',
              'power_stamina' : 'Power stamina', 'power_strength' : 'Power strength',
              'power_long_shots' : 'Power long shots', 'mentality_aggression' : 'Mentality aggression',
              'mentality_interceptions' : 'Mentality interceptions',
              'mentality_positioning' : 'Mentality positioning', 'mentality_vision' : 'Mentality vision',
              'mentality_penalties' : 'Mentality penalties', 'mentality_composure' : 'Mentality composure',
              'defending_marking' : 'Defending marking', 'defending_standing_tackle' : 'Defending standing tackle',
              'defending_sliding_tackle' : 'Defending sliding tackle', 'goalkeeping_diving' : 'Goalkeeping diving',
              'goalkeeping_handling' : 'Goalkeeping handling', 'goalkeeping_kicking' : 'Goalkeeping kicking',
              'goalkeeping_positioning' : 'Goalkeeping positioning', 'goalkeeping_reflexes' : 'Goalkeeping_reflexes',
              'ls' : 'LS', 'st' : 'St', 'rs' : 'RS', 'lw' : 'LW', 'lf' : 'LF', 'cf' : 'CF', 'rf' : 'RF',
              'rw' : 'RW', 'lam' : 'LAM', 'cam' : 'CAM', 'ram' : 'RAM', 'lm' : 'LM', 'lcm' : 'LCM',
              'cm' : 'CM', 'rcm' : 'RCM', 'rm' : 'RM', 'lwb' : 'LWB', 'ldm' : 'LDM', 'cdm' : 'CDM',
              'rdm' : 'RDM', 'rwb' : 'RWB', 'lb' : 'LB', 'lcb' : 'LCB', 'cb' : 'CB', 'rcb' : 'RCB',
              'rb' : 'RB'}
    
    df1 = pd.DataFrame( fil.loc[fil.international_reputation==1] )
    df2 = pd.DataFrame( fil.loc[fil.international_reputation==2] )
    df3 = pd.DataFrame( fil.loc[fil.international_reputation==3] )
    df4 = pd.DataFrame( fil.loc[fil.international_reputation==4] )
    df5 = pd.DataFrame( fil.loc[fil.international_reputation==5] )
    data = [df1.groupby([x])[y].mean(), df2.groupby([x])[y].mean(), df3.groupby([x])[y].mean(), df4.groupby([x])[y].mean(), df5.groupby([x])[y].mean()]
    datastd = [df1.groupby([x])[y].std(), df2.groupby([x])[y].std(), df3.groupby([x])[y].std(), df4.groupby([x])[y].std(), df5.groupby([x])[y].std()]
    
    xax = np.arange(16,42,0.5532)
    yax = np.arange(48,95)
    
    if len(data) < 3:
        a = 1
        b = math.ceil( len(data) )
            
    else:
        b = 2
        a = math.ceil( len(data) / b )
    
    fig, axes = plt.subplots( a, b )
    fig.subplots_adjust(wspace=0.1, hspace=0.6)
    
    c = 0
    d = 0
    
    for i in range(len(data)):
        if i != 0:
            d += 1
        
        if d == 2:
            d = 0
            c += 1
            
        axes[c,d].plot( data[i] + datastd[i], 'b:' )
        axes[c,d].plot( data[i], 'b-' )
        axes[c,d].plot( data[i] - datastd[i], 'b:' )
        axes[c,d].set_title( 'Internationalt omdoemme: ' + str(i+1) )
        axes[c,d].plot( xax, yax, alpha = 0 )
#        plt.xlabel( 'Internationalt omdoemme: ' + str(i+1), fontsize=12 )
        axes[c,d].grid( True )
    
    if len(data) < a * b:
        fig.delaxes(axes[a - 1, b - 1])
    
    fig.legend(['Gns +/- Standardafvigelse', 'Gennemsnit'], loc='lower right', framealpha=0)
    fig.text(0.001, 0.5, ordbog[y], va='center', rotation='vertical')
    fig.text(0.5, 0.02, ordbog[x], va='center', rotation='horizontal')
    fig.tight_layout()
    plt.savefig( 'Grafer/AverageIntRepPlots/avg-intrep-' + ordbog[y]  + '-over-age.pdf' )
    plt.show()

file = pd.read_csv( 'players_20.csv', sep= ',' )
fig_plot_avg(file, 'age', 'overall')