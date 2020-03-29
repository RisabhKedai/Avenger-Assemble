import pygame
from pygame.sprite import Sprite
class Ironman(Sprite):
    def __init__(self,screen,setting):
        #inheriting from sprite
        super().__init__()
        #choose where ironman appears
        self.screen=screen
        self.setting=setting
        #choose ironmans photo
        self.image=pygame.image.load('data/images.bmp')
        #get a rectangle for the ship
        self.rect=self.image.get_rect()
        self.scr_rect=screen.get_rect()
        self.move_right=False
        self.move_left=False
        #start each new ship at the bottom centerof the screen
        self.rect.centerx=self.scr_rect.centerx
        self.rect.bottom=self.scr_rect.bottom
        self.center=float(self.rect.centerx)

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right<=self.scr_rect.right:
            self.center+=self.setting.speed_fact
        if self.move_left and self.rect.left>=self.scr_rect.left:
            self.center-=self.setting.speed_fact
        self.rect.centerx=self.center
                
        
    def center_iron(self):
        '''centralise ironman'''
        self.center=self.scr_rect.centerx
