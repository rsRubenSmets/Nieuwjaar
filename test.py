from Player import Player
from Game import Spec_game
import save_and_load as sl

if __name__ == '__main__':

    team_1 = "losers"
    team_2 = "alsoLosers"

    # chicky = Player('Chicky', team_1)
    # lisa = Player('Lisa', team_1)
    # meutte = Player('Meutte', team_1)
    # vince = Player('Vince', team_1)
    # yannick = Player('Yannick', team_1)
    #
    # fien = Player('Fien', team_2)
    # gijs = Player('Gijs', team_2)
    # jeff = Player('Jeff', team_2)
    # jerry = Player('Jerry', team_2)
    # thomas = Player('Thomas', team_2)

    game = "poker"
    round = 0

    list_participants = sl.load_list_participants(round)

    sl.save_list_participants([chicky,fien,gijs,jeff,jerry,lisa,meutte,thomas,vince,yannick],round)

    # chicky.add_bps(10,'round1')
    # fien.add_bps(10,'round1')
    # gijs.add_bps(10,'round1')

    dict_game = {
        'p1': chicky,
        'p2': lisa,
        'p3': fien,
        'p4': gijs,
        'game': game,
        'round': round
    }

    outcome_points = {
        chicky: 6,
        lisa: 14,
        fien:10,
        gijs: 10
    }

    outcome_bps = {
        chicky:5,
        lisa:15,
        fien:3,
        gijs:17
    }

    spec_game = Spec_game(dict_game)

    spec_game.process_outcome(outcome_points,outcome_bps)

    coef_team,coef_player = spec_game.get_bc()



    print(f"Player {jeff.get_name()} has {jeff.get_points()} points and {jeff.get_bps()} BPs")

