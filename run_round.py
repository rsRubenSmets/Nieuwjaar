
if __name__ == "__main__":

    list_games = ['Poker','Fuck the dealer','Cupgame','Quixx','Chapeau','Switch volleybal', 'Wiezen']
    round = 2
    dobbel = 1

    list_participants = sl.load_list_participants(round-1)
    [chicky,fien,gijs,jeff,jerry,lisa,meutte,thomas,vince,yannick] = list_participants

    boitkings = get_boitking_per_team(list_participants)

    game_1,game_2 = generate_random_games(list_participants,boitkings,list_games,round,dobbel)


    outcome_points_1 = {
        jeff: 6,
        jerry: 14,
        meutte: 10,
        vince: 10
    }

    outcome_bps_1 = {
        jeff: 6,
        jerry: 14,
        meutte: 10,
        vince: 10
    }

    outcome_points_2 = {
        gijs:5,
        thomas:15,
        lisa:3,
        yannick:17
    }

    outcome_bps_2 = {
        gijs:5,
        thomas:15,
        lisa:3,
        yannick:17
    }

    game_1.process_outcome(outcome_points_1,outcome_bps_1)
    game_2.process_outcome(outcome_points_2,outcome_bps_2)

    sl.save_list_participants(list_participants,round)

    x=1