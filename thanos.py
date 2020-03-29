import pygame
from pygame.sprite import Sprite

class Thanos(Sprite):
    #the aliens class to manage Thanos
    def __init__(self,setting,screen):
        super().__init__()
        self.screen=screen
        self.setting=setting

        '''loading image of thanos'''
        self.image=pygame.image.load('data/thanos.bmp')
        self.rect=self.image.get_rect()

        '''positioning each thanos at the top left'''
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height/2

        '''exact position af each thanos'''
        self.x=float(self.rect.x)


    def blitme(self):
        '''a function to draw thanos'''
        self.screen.blit(self.image,self.rect)


    def update(self):
        ''' moving the thanos right'''
        self.x+=(self.setting.speed_th*self.setting.direct)
        self.rect.x=self.x

    def check_edge(self):
        '''return true if thanos is at edge'''
        scr_rect=self.screen.get_rect()
        if self.rect.right>=scr_rect.right:
            return True
        elif self.rect.left<=scr_rect.left:
            return True
