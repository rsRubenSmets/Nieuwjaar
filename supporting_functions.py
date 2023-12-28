import os
import random
import pickle
from Game import Spec_game

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

def generate_dict(p_1,p_2,game,round):

    dict = {
        'p1': p_1[0],
        'p2': p_1[1],
        'p3': p_2[0],
        'p4': p_2[1],
        'game': game,
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

    dict_1 = generate_dict(players_1_a,players_2_a,games[0],round)
    dict_2 = generate_dict(players_1_b,players_2_b,games[1],round)

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

def load_list_participants(round):
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