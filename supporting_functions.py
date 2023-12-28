import os
import random
import pickle
from Game import Spec_game
import matplotlib.pyplot as plt

##### FUNCTIONS FOR ROUND INITIALIZATION #####

def get_boitking_per_team(list_participants):
    boitkings = {}
    for p in list_participants:
        t = p.get_team()
        if t in set(boitkings):
            if p.get_bps() > boitkings[t].get_bps():
                boitkings[t] = p
            else:
                pass
        else:
            boitkings[t] = p

    return boitkings

def generate_dict(p_1,p_2,game,round,game_nb):

    dict = {
        'p1': p_1[0],
        'p2': p_1[1],
        'p3': p_2[0],
        'p4': p_2[1],
        'game': game,
        'game_nb': game_nb,
        'round': round
    }
    return dict

def generate_random_games(list_participants,boitkings,list_games,round,dobbel):
    l1,l2 = split_list_participants(list_participants,boitkings)

    rand_1 = dobbel*round
    rand_2 = dobbel*round+2
    rand_3 = dobbel*round+3

    random.seed(rand_1)
    players_1_a = random.sample(l1,2)
    players_1_b = [p for p in l1 if p not in players_1_a]

    random.seed(rand_2)
    players_2_a = random.sample(l2,2)
    players_2_b = [p for p in l2 if p not in players_2_a]

    random.seed(rand_3)
    games = random.sample(list_games,2)

    dict_1 = generate_dict(players_1_a,players_2_a,games[0],round,1)
    dict_2 = generate_dict(players_1_b,players_2_b,games[1],round,2)

    game_1 = Spec_game(dict_1)
    game_2 = Spec_game(dict_2)

    return game_1,game_2

def split_list_participants(list_participants,boitkings):
    l1 = []
    l2 = []

    for p in list_participants:
        if p in boitkings.values():
            pass
        elif len(l1) == 0:
            l1.append(p)
        elif p.get_team() == l1[0].get_team():
            l1.append(p)
        else:
            l2.append(p)

    return l1,l2

##### FUNCTIONS FOR SPECIAL ACTIONS #####

def execute_special_action(player,type,amount,round,ow,name):
    if name == "":
        name = f"special_{type}_{round}"

    if type == 'points':
        if ow:
            player.remove_points(name)
        player.add_points(amount, name)
    elif type == 'bps':
        if ow:
            player.remove_bps(name)
        player.add_bps(amount, name)
    else:
        ValueError(f"Unsupported type {type}")

    overwrite_player(player,round)

def overwrite_player(p,round):

    dir = f'Results/round_{round}'
    name = p.get_name()
    with open(f"{dir}/{name}.pkl", 'wb') as file:
        pickle.dump(p, file)


##### FUNCTIONS FOR SAVING AND LOADING #####

def save_list_participants(list, round):
    dir = f'Results/round_{round}'
    assert not os.path.exists(dir), f"Round {round} results already exist"
    os.mkdir(dir)

    for p in list:
        filename = p.get_name()
        with open(f"{dir}/{filename}.pkl", 'wb') as file:
            pickle.dump(p, file)

def load_list_participants(round):
    list = []
    dir = f'Results/round_{round}'

    for f in os.listdir(dir):
        if "game" in f:
            pass
        else:
            filename = f"{dir}/{f}"

            with open(filename, 'rb') as file:
                p = pickle.load(file)

            list.append(p)

    return list

def save_list_games(list, round):
    dir = f'Results/round_{round}'

    for g in list:
        game_nb = g.get_game_nb()
        path = f"{dir}/game_{game_nb}.pkl"

        assert not os.path.exists(dir), f"Round {round} results already exist"

        with open(path, 'wb') as file:
            pickle.dump(g, file)

def load_list_games(round):
    list = []
    dir = f'Results/round_{round}'

    for f in os.listdir(dir):
        if "game" in f:
            filename = f"{dir}/{f}"

            with open(filename, 'rb') as file:
                g = pickle.load(file)

            list.append(g)
        else:
            pass

    return list

##### FUNCTIONS FOR VISUALIZATION #####

def convert_team_color(team):

    if team == 'losers':
        return 'blue'
    elif team == 'alsoLosers':
        return 'red'

def visualize_leaderboard(round):
    def create_sorted_bar_plot(ax, values, names, colors, title):
        combined = sorted(zip(values, names, colors), reverse=True)
        sorted_values, sorted_names, sorted_colors = zip(*combined)
        bars = ax.bar(range(len(sorted_values)), sorted_values, color=sorted_colors)

        for bar, name in zip(bars, sorted_names):
            # Position the name in the middle of the bar
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, name,
                    ha='center', va='center', rotation=90, color='white', fontsize=10, fontweight='bold')
            # Position the value on top of the bar
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height()}',
                    ha='center', va='bottom', color='black', fontsize=10)

        # Remove x-axis labels and ticks
        ax.set_xticks([])
        ax.set_xlabel('')

        ax.set_title(title)

    list_participants  = load_list_participants(round)

    sorted_points_val_p, sorted_points_name_p, sorted_points_col_p = get_sorted_lists(list_participants, 'points', 'player')
    sorted_bps_val_p, sorted_bps_name_p, sorted_bps_col_p = get_sorted_lists(list_participants, 'bps', 'player')
    sorted_points_val_t, sorted_points_name_t, sorted_points_col_t = get_sorted_lists(list_participants, 'points', 'team')
    sorted_bps_val_t, sorted_bps_name_t, sorted_bps_col_t = get_sorted_lists(list_participants, 'bps', 'team')

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Create each bar plot
    create_sorted_bar_plot(axs[0, 0], sorted_points_val_p, sorted_points_name_p, sorted_points_col_p, 'Punten per speler')
    create_sorted_bar_plot(axs[0, 1], sorted_bps_val_p, sorted_bps_name_p, sorted_bps_col_p, 'Boitpunten per speler')
    create_sorted_bar_plot(axs[1, 0], sorted_points_val_t, sorted_points_name_t, sorted_points_col_t, 'Punten per team')
    create_sorted_bar_plot(axs[1, 1], sorted_bps_val_t, sorted_bps_name_t, sorted_bps_col_t, 'Boitpunten per team')

    # Adjust layout and add a general title
    plt.tight_layout()
    fig.suptitle(f'TUSSENSTAND NA RONDE {round}', fontsize=16, fontweight='bold', va='top')

    # Adjust spacing for the general title
    fig.subplots_adjust(top=0.88)

    # Display the graph
    plt.show()


    x=1

def get_sorted_lists(list_participants,type_points,type_agg):

    vals = []
    names = []
    colors = []

    for p in list_participants:
        if type_points == "points":
            vals.append(p.get_points())
        elif type_points == "bps":
            vals.append(p.get_bps())

        if type_agg == 'player':
            names.append(p.get_name())
        elif type_agg == 'team':
            names.append(p.get_team())

        colors.append(convert_team_color(p.get_team()))

    if type_agg == 'team':
        names_unique = []
        vals_team = []
        [names_unique.append(name) for name in names if name not in names_unique]

        vals_team = []
        for name in names_unique:
            indices = [index for index, value in enumerate(names) if value == name]
            tot_val = sum(vals[i] for i in indices)
            vals_team.append(tot_val)

        vals = vals_team
        names = names_unique
        colors = [convert_team_color(name) for name in names]


    combined = sorted(zip(vals, names, colors), reverse=True)

    sorted_val, sorted_name, sorted_col = zip(*combined)

    return sorted_val, sorted_name, sorted_col

