import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #a class for the bullets

    def __init__(self,setting,screen ,iron):
        """Create a bullet object at ships position"""
        super().__init__()
        self.screen=screen

        #create a bullet rect at (0,0) and then set current position
        self.rect=pygame.Rect(0,0,setting.bull_width,setting.bull_height)
        self.rect.centerx=iron.rect.centerx
        self.rect.top=iron.rect.top

        #storimg the bullets position
        self.y=float(self.rect.y)

        self.color=setting.bull_color
        self.speed=setting.bull_speed


    def update(self):
        #updating the bullets position
        self.y-=self.speed
        #update the  rect position
        self.rect.y=self.y


    def draw_bull(self):
        """drawing the bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
    
        
        
        
