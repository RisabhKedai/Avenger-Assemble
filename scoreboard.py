import pygame.font
from pygame.sprite import Group
from ironman import Ironman

class Scoreboard():
    ''' a class for storing the scores'''
    def __init__(self,setting,screen,stats):
        """Initialise the iniial scorekeeping attributes"""
        self.screen=screen
        self.scr_rect=screen.get_rect()
        self.setting=setting
        self.stats=stats

        #Font settings for scoring info
        self.scor_color=(30,30,30)
        self.font=pygame.font.SysFont("Corbel",20)

        #Prepare the initial scores images
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_iron()

    def prep_score(self):
        '''turn the score to an image'''
        #rounding the score
        round_scor=int(round(self.stats.score,-1))
        score_str="{:,}".format(round_scor)
        score_str="SCORE : "+score_str
        self.scor_img=self.font.render(score_str,True,self.scor_color,self.setting.bg)

        #setting where the score will appear on screen
        self.scor_rect=self.scor_img.get_rect()
        self.scor_rect.right=self.scr_rect.right-20
        self.scor_rect.top=self.scr_rect.top+20

    def prep_highscore(self):
        '''turn the highscore to an rendered image'''
        high_score=int(round(self.stats.high_score,-1))
        high_str="{:,}".format(high_score)
        high_str="HIGHSCORE : "+high_str
        self.high_img=self.font.render(high_str,True,self.scor_color,self.setting.bg)

        #center the high score on top
        self.high_score_rect=self.high_img.get_rect()
        self.high_score_rect.centerx=self.scr_rect.centerx
        self.high_score_rect.top = self.scor_rect.top

    def prep_level(self):
        '''turning level to img'''
        self.level_img=self.font.render("LEVEL :"+str(self.stats.level),True,self.scor_color,self.setting.bg)
        #position the level below score
        self.level_rect=self.level_img.get_rect()
        self.level_rect.top=self.scor_rect.bottom+10
        self.level_rect.right=self.scr_rect.right-10

    def prep_iron(self):
        '''show how many ironmans are left'''
        self.irons=Group()
        for suit_no in range(self.stats.iron_life):
            iron=Ironman(self.screen,self.setting)
            iron.rect.x=10+suit_no*iron.rect.width
            iron.rect.y=10
            self.irons.add(iron)


    def showscore(self):
        '''draw the score and level to screen'''
        self.screen.blit(self.scor_img,self.scor_rect)
        self.screen.blit(self.high_img,self.high_score_rect)
        self.screen.blit(self.level_img,self.level_rect)
        self.irons.draw(self.screen)
