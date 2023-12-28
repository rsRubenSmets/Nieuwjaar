import supporting_functions as sf


if __name__ == "__main__":

    list_games = ['Poker','Fuck the dealer','Cupgame','Quixx','Chapeau','Switch volleybal', 'Wiezen']
    round = 2
    [chicky,fien,gijs,jeff,jerry,lisa,meutte,thomas,vince,yannick]  = sf.load_list_participants(round)
    player = chicky
    type = 'bps' #points or bps
    amount = -5
    overwrite = False
    key = ""


    sf.execute_special_action(player,type,amount,round,overwrite,key)

    [chicky,fien,gijs,jeff,jerry,lisa,meutte,thomas,vince,yannick]  = sf.load_list_participants(round)

    points = chicky.get_points()

    x=1


