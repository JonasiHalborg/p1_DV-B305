import matplotlib.pyplot as plt
import pandas as pd

#Lister defineres for spillerposition.
list_gk = ["GK"]
list_def = ["CB", "LB", "RB", "LCB", "RCB", "LWB", "RWB"]
list_mid = ["CAM", "CDM", "CM", "LAM", "LCM", "RCM", "LDM", "RDM", "LM", "RM", "RAM"]
list_off = ["CF", "LS", "RS", "ST", "LW", "RW", "LF", "RF"]
list_sub = ["SUB", "RES"]

f20 = pd.read_csv('players_20.csv', sep = ',')

#Overflødige attributter fjernes
del f20["sofifa_id"], f20["player_url"], f20["short_name"], f20["dob"], f20["long_name"],\
f20["nationality"], f20["club"], f20["value_eur"], f20["wage_eur"] , f20["player_positions"], f20["preferred_foot"],\
f20["international_reputation"], f20["weak_foot"], f20["skill_moves"], f20["work_rate"], f20["body_type"],\
f20["real_face"], f20["player_tags"], f20["team_jersey_number"], f20["loaned_from"], f20["joined"],\
f20["contract_valid_until"], f20["nation_position"], f20["nation_jersey_number"], f20["player_traits"],\
f20["release_clause_eur"], f20["age"], f20["height_cm"], f20["weight_kg"]

#Datasættet  grupperes  efter  spillernes  position.
f20 = f20.groupby (["team_position"]).mean()

plt.imshow(f20 , cmap="YlOrRd") #Heatmap  genereres  ud fra  dataframen  f20.

plt.colorbar(orientation = 'vertical') #Farveskala  tilføjes.

plt.xticks(range(len(f20.columns)),f20.columns , rotation =90) #Tekst på x-aksen  indsættes.

plt.yticks(range(len(f20.index)),f20.index) #Tekst på y-aksen  indsættes.

plt.show()
