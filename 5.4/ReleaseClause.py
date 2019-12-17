import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Indlæser filen og sætter adskillelsen til ","
f20 = pd.read_csv('players_20.csv', sep=',')


# Fjerner kolonner fra tabellen, som vi nok ikke kommer til at bruge.
del f20["sofifa_id"], f20["player_url"], f20["long_name"], f20["dob"], f20["real_face"], f20["body_type"],\
    f20["player_tags"], f20["team_jersey_number"], f20["loaned_from"], f20["work_rate"], f20["nation_position"], \
    f20["nation_jersey_number"], f20["player_traits"], f20["goalkeeping_diving"],\
    f20["goalkeeping_handling"], f20["goalkeeping_kicking"], f20["goalkeeping_positioning"], f20["goalkeeping_reflexes"]
# Urelevant for "release_clause_eur" og "potential"
del f20["height_cm"], f20["weight_kg"], f20["joined"], f20["player_positions"]
f20 = f20.iloc[:, 0:-61] # afskær de sidste 61 kolonner, iloc funktionen bruges til at vælge data ud fra kolonner

# Inddeler de forskellige positioner i målmand, defensiv, midbane, offensiv og reservespillere
list_gk = ["GK"]
list_def = ["CB", "LB", "RB", "LCB", "RCB", "LWB", "RWB"]
list_mid = ["CAM", "CDM", "CM", "LAM", "LCM", "RCM", "LDM", "RDM", "LM", "RM", "RAM"]
list_off = ["CF", "LS", "RS", "ST", "LW", "RW", "LF", "RF"]
list_sub = ["SUB", "RES"]

df = f20.groupby(["team_position"]).mean()

f20_1e6 = f20.copy()

f20_1e6.release_clause_eur = f20_1e6.release_clause_eur / 1e6
f20_1e6.value_eur = f20_1e6.value_eur / 1e6

log = f20_1e6.copy()
log.release_clause_eur = np.log(log.release_clause_eur)


# /// RELEASE CLAUSE EUR ///

def boxage():

    f20_1e6.boxplot(by='age', column=['release_clause_eur'], grid=False, showfliers=False, showmeans=True)
    plt.xlabel("Alder")
    plt.ylabel("Frikøbsklausul i 10 mio. €")


    plt.title("")
    plt.suptitle("")

    plt.show()

def position():

    def category(pos):
        if pos in list_gk:
            return 'GK'
        elif pos in list_def:
            return 'DEF'
        elif pos in list_mid:
            return 'MID'
        elif pos in list_off:
            return 'OFF'
        elif pos in list_sub:
            return 'SUB'

    liste = []

    for i in df.index:
        liste.append(category(i))

    f21 = pd.DataFrame(df)
    f21.index = liste

    f2000 = f21.iloc[:, 8:9]
    f2000 = f2000.groupby([f2000.index]).mean()
    f2000 = f2000 / 1e5
    f2000 = f2000.reindex(index=["GK", "DEF", "MID", "OFF", "SUB"])

    plt.grid(zorder=0, axis="y")
    plt.xlabel("Position")
    plt.ylabel("Frikøbsklausul i mio. €")
    plt.bar(f2000.index, f2000["release_clause_eur"])
    plt.show()

def overallpotential3i1():
    fig = plt.figure()
    fig.text(0.075, 0.5, 'Frikøbsklausul i mio. €', va='center', fontsize=12, rotation='vertical')
    fig.text(0.5, 0.035, "Gennemsnit", fontsize=12, ha='center')
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,4)

    grouped_potential = f20_1e6.groupby(["potential"])["release_clause_eur"].mean()
    grouped_overall = f20_1e6.groupby(["overall"])["release_clause_eur"].mean()
    standard_potentiale = f20_1e6.groupby(["potential"])["release_clause_eur"].std()
    standard_overall = f20_1e6.groupby(["overall"])["release_clause_eur"].std()

    ax1.plot(grouped_potential, "r.")
    ax1.plot(grouped_overall, "b.")
    ax1.grid(True)
    ax1.legend(["Potentiale", "Overall"])

    ax2.plot(grouped_overall, "b.")
    ax2.plot(grouped_overall + standard_overall, "b:", alpha=0.75)
    ax2.plot(grouped_overall - standard_overall, "b:", alpha=0.75)
    ax2.grid(True)
    ax2.legend(["Overall", "+/- Standardafvigelsen"])

    ax3.plot(grouped_potential, "r.")
    ax3.plot(grouped_potential + standard_potentiale, "r:", alpha=0.75)
    ax3.plot(grouped_potential - standard_potentiale, "r:", alpha=0.75)
    ax3.grid(True)
    ax3.legend(["Potentiale", "+/- Standardafvigelsen"])

    plt.show()

def exp_groupoverall_rc():
    plt.grid(True)
    plt.xlabel("Gennemsnitslig overall score")
    plt.ylabel("Frikøbsklausul i mio. €")
    grouped_overall = log.groupby(["overall"])["release_clause_eur"].mean()
    grouped_overallf20 = f20_1e6.groupby(["overall"])["release_clause_eur"].mean()

    plt.plot(grouped_overallf20, "b.")

    x = grouped_overall.index
    y = grouped_overall

    z = np.polyfit(x, y, 1)
    a, b = z

    reg_a, reg_b = np.exp([a, b])

    def f(t):
        return reg_a**t * reg_b

    plt.plot(x, f(x), "r-")
    plt.legend(["Overall", "Eksponentiel regression"])

    plt.show()

def subplot6grouped():
    fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)
    plt.axis([0, 100, 0, 200])
    fig.text(0.05, 0.5, 'Frikøbsklausul i mio. €', va='center', rotation='vertical')
    plt.subplots_adjust(hspace=0.2) # Højden mellem graferne

    axs[0, 0].plot(f20_1e6.groupby(["pace"])["release_clause_eur"].mean(), "b.")
    axs[0, 0].set_xlabel("Pace")
    axs[0, 0].grid(True)

    axs[0, 1].plot(f20_1e6.groupby(["shooting"])["release_clause_eur"].mean(), "b.")
    axs[0, 1].set_xlabel("Shooting")
    axs[0, 1].grid(True)

    axs[0, 2].plot(f20_1e6.groupby(["passing"])["release_clause_eur"].mean(), "b.")
    axs[0, 2].set_xlabel("Passing")
    axs[0, 2].grid(True)

    axs[1, 0].plot(f20_1e6.groupby(["dribbling"])["release_clause_eur"].mean(), "b.")
    axs[1, 0].set_xlabel("Dribbling")
    axs[1, 0].grid(True)

    axs[1, 1].plot(f20_1e6.groupby(["defending"])["release_clause_eur"].mean(), "b.")
    axs[1, 1].set_xlabel("Defending")
    axs[1, 1].grid(True)

    axs[1, 2].plot(f20_1e6.groupby(["physic"])["release_clause_eur"].mean(), "b.")
    axs[1, 2].set_xlabel("Physic")
    axs[1, 2].grid(True)

    plt.show()

def valuewage():
    fig = plt.figure()
    fig.text(0.075, 0.5, 'Frikøbsklausul i mio. €', va='center', fontsize=9, rotation='vertical')

    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    grouped_value = f20_1e6.groupby(["value_eur"])["release_clause_eur"].mean()
    grouped_wage = f20_1e6.groupby(["wage_eur"])["release_clause_eur"].mean()

    ax1.plot(grouped_value, "b.")
    ax1.grid(True)
    ax1.set_xlabel("Værdi i mio. €")
    ax1.legend(["Værdi"])

    ax2.plot(grouped_wage, "b.")
    ax2.grid(True)
    ax2.set_xlabel("Løn i €")
    ax2.legend(["Løn"])
    plt.show()