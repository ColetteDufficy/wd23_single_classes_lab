class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0 # Zero is a hard coded value thats always the same when we start defining the object

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        return player in self.players
    # # alterntaive code:
    # def has_player(self, player):
    #     if player in self.players:
    #         return True
    #     else:
    #         return False
    
    
    def play_game(self, game_won): #game_won is going to be either true or false
        if game_won:
            self.points += 3
     
    # # altrnative code:    
    # def play_game(self, game_won): #game_won is going to be either true or false
    #     if game_won == True:
    #         self.points - self.points + 3