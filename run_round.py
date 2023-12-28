import supporting_functions as sf


if __name__ == "__main__":

    list_games = ['Poker','Fuck the dealer','Cupgame','Quixx','Chapeau','Switch volleybal', 'Wiezen']
    round = 2
    dobbel = 1

    list_participants = sf.load_list_participants(round-1)
    [chicky,fien,gijs,jeff,jerry,lisa,meutte,thomas,vince,yannick] = list_participants

    boitkings = sf.get_boitking_per_team(list_participants)

    game_1,game_2 = sf.generate_random_games(list_participants,boitkings,list_games,round,dobbel)


    outcome_points_1 = {
        chicky: 6,
        vince: 14,
        gijs: 10,
        jerry: 10
    }

    outcome_bps_1 = {
        chicky: 10,
        vince: 2,
        gijs: 9,
        jerry: 6
    }

    outcome_points_2 = {
        lisa:5,
        meutte:15,
        fien:8,
        jeff:17
    }

    outcome_bps_2 = {
        lisa:9,
        meutte:5,
        fien:6,
        jeff:6
    }

    game_1.process_outcome(outcome_points_1,outcome_bps_1)
    game_2.process_outcome(outcome_points_2,outcome_bps_2)

    sf.save_list_participants(list_participants,round)

    x=1