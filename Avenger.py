import pygame
from ironman import Ironman
from settings import Settings
import game_func as gf
import sys
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from button import Intro
from scoreboard import Scoreboard


#print("the game should begin")
def runmygame():
    #print("the game begins")
    pygame.init()
    seto=Settings()
    screen=pygame.display.set_mode((seto.width,seto.height))
    #creating object of class ironman
    iron=Ironman(screen,seto)
    pygame.display.set_caption("Avenger")
    game_icon=pygame.image.load("data/iconga.ico")
    pygame.display.set_icon(game_icon)
    #make the play button and intro message
    play_butt=Button(seto,screen,"Play")
    intro=Intro(seto,screen)
    
    stats=GameStats(seto)
    #creating scoreboard object
    score=Scoreboard(seto,screen,stats)
    #create a group of bullets
    bullets=Group()
    thanoss=Group()
    #error:screen.set_caption("Avenger")
    gf.creat_flee(seto,screen,thanoss,iron)
    
    while True:
        #check_event() starts
        gf.check_ev(iron,seto,screen,bullets,thanoss,stats,play_butt,score)
        #check_event() ends
        if stats.game_active:
            iron.update()
            gf.update_bull(seto,screen,thanoss,bullets,iron,stats,score)
            gf.updat_tha(seto,iron,thanoss,stats,screen,bullets,score)
        #print(len(bullets))
        gf.updat_scr(seto,screen,iron,bullets,thanoss,stats,play_butt,intro,score)
        #print("the game end now")

#print("the game ended")

runmygame()
