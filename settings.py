class Settings:
    def __init__(self):
        self.width=800
        self.height=600
        self.bg=(255,255,255)
        #ironman speed factor
        self.speed_fact=0.65

        #bullet info
        self.bull_speed=1
        self.bull_width=20
        self.bull_height=15
        self.bull_color=(30,130,255)
        self.allowed=3

        #thanos info
        self.speed_th=0.6
        self.drop_spe=5
        #direction -1 for left 1 for right
        self.direct=1

        #game stats
        self.iron_batt=3 #ironman's battery


        #the games dynamic settings
        self.speed_upfactor=1.1
        '''how quickly thanos comes down'''

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''initialize the dynamic settings of the game'''
        self.speed_fact=0.75
        self.bull_speed=1
        self.speed_th=0.6
        #fleet direction of 1 represents right ; -1 represents left
        self.direct=1
        #score per thanos
        self.point=5

    def increase_speed(self):
        '''initialize the dynamic settings of the game'''
        self.speed_fact=0.75
        self.bull_speed=1
        self.point*=2
        self.speed_th*=self.speed_upfactor
        self.drop_spe*=self.speed_upfactor
        #fleet direction of 1 represents right ; -1 represents left
        self.direct=1
        
        
        
        
