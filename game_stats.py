class GameStats():
    ''' Track statistics for Avenger Game.'''
    def __init__(self,setting):
        ''' Initialise setting'''
        self.setting=setting
        self.high_score=0
        self.reset_stat()
        #start the game in inactive state.
        self.game_active=False

    def reset_stat(self):
        ''' Initialise statistics that can change during game'''
        self.iron_life=self.setting.iron_batt
        self.score=0
        self.level=1

        
