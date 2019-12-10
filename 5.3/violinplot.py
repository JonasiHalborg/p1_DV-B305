# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:12:26 2019

@author: mgejl
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value

def violin_plt(fil, y):
    ordbog = {'sofifa_id' : 'Id', 'player_url' : 'Spiller URL adresse', 'short_name' : 'Navn',
              'long_name' : 'Fulde navn', 'age' : 'Alder', 'dob' : 'Fødsels dato',
              'height_cm' : 'Højde i cm', 'weight_kg' : 'Vægt i kg', 'nationality' : 'Nationalitet',
              'club' : 'klub', 'overall' : 'Overall', 'potential' : 'Potential',
              'value_eur' : 'Pris i euro', 'wage_eur' : 'Løn i euro',
              'player_positions' : 'Spiller Positioner', 'preferred_foot' : 'Foretrukne fod',
              'international_reputation' : 'Internationalt omdømme', 'weak_foot' : 'Svage fod',
              'skill_moves' : 'Skill moves', 'work_rate' : 'Work Rate', 'body_type' : 'Kropstype',
              'real_face' : 'Rigtige ansigt', 'release_clause_eur' : 'Frikøbsklausul i euro',
              'player_tags' : 'Spiller tags', 'team_position' : 'Hold position',
              'team_jersey_number' : 'Hold trøjenummer', 'loaned_from' : 'Lånt fra',
              'joined' : 'Tilslutningsdato', 'contract_valid_until' : 'Kontraktvarighed',
              'nation_position' : 'Landsholdsposition', 'nation_jersey_number' : 'Landshold trøjenummer',
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
    
    dl1 = list(df1[y])#[float(i) for i in list(df1[y])]
    dl2 = list(df2[y])#[float(i) for i in list(df2[y])]
    dl3 = list(df3[y])#[float(i) for i in list(df3[y])]
    dl4 = list(df4[y])#[float(i) for i in list(df4[y])]
    dl5 = list(df5[y])#[float(i) for i in list(df5[y])]
    data = [dl1, dl2, dl3, dl4, dl5]
    quartile1 = []
    medians = []
    quartile3 = []

    for i in data:
        quartile1.append(np.percentile(i, 25, axis=0))
        medians.append(np.percentile(i, 50, axis=0))
        quartile3.append(np.percentile(i, 75, axis=0))
    
    labels = [1,2,3,4,5]
    fig, ax = plt.subplots(figsize=(7,5))
    
    parts = ax.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)
    
    for pc in parts['bodies']:
        pc.set_facecolor('b')
        pc.set_edgecolor('black')
        pc.set_alpha(1)
    
    whiskers = np.array([
        adjacent_values(sorted_array, q1, q3)
        for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
    whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]
    
    inds = np.arange(1, len(medians) + 1)
    ax.scatter(inds, medians, marker='_', color='white', s=30, zorder=3)
    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
    ax.vlines(inds, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)
    
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlabel('Internationalt omdømme', FontSize=12)
    ax.set_ylabel(ordbog[y], FontSize=12)
    
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
    plt.tight_layout()
    plt.grid(axis='y')
    plt.savefig( 'grafer/violinplots/Violin-plot-over-internationalt-omdoemme--' + ordbog[y]  + '.pdf' )
    plt.show()
    

file = pd.read_csv( 'players_20.csv', sep= ',' )
violin_plt(file, 'overall')