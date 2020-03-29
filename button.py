import pygame.font

class Button():

    def __init__(self,setting,screen,msg):
        '''initialize button attribtes'''

        self.screen=screen
        self.scr_rect=screen.get_rect()

        #set the dimensions and properties of the button
        self.width,self.height=200,50
        self.butt_color=(0,255,20)
        '''actually font and color of the text'''
        self.font=pygame.font.SysFont('Arial',48)
        self.text_color=(255,255,255)


        #Built the button's rect object and center it
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.scr_rect.center


        #the button message needs to be prepped only once
        self.prep_msg(msg)


    def prep_msg(self,msg):
        ''' turning the message to an image'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.butt_color)
        self.msg_image_rect=self.msg_image.get_rect()
        '''centering text image on button'''
        self.msg_image_rect.center=self.rect.center


    def draw_butt(self):
        self.screen.fill(self.butt_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)




class Intro():
    def __init__(self,setting,screen):
        self.msg=[
            "Here is one possibility of the 14 million which Dr.Strange saw.",
            "Thanos used Dr.Strange's strange power to multiply himself.",
            "As usual our hero Ironman decided to defeat Thanos using his Mark.Blur suit",
            "But he wants you to control the suit",
            "Press -> to move right and <- to move left.",
            "Press Spacebar to hurl Energy blasts.",
            "Press q to quit any moment",
            "Good Luck saving the world.",
            ]
        self.screen=screen
        self.scr_rect=screen.get_rect()
        
        #set the dimensions and properties of intro text
        #self.width,self.height=700,250
        '''actually font and color of the text'''
        self.font=pygame.font.SysFont(None,14)
        self.text_color=(0,0,0)

        #the button message needs to be prepped only once

    def prep_intro(self,msg):
        ''' turning the message to an image'''
        ctr=0
        for k in msg:
            msg_image=self.font.render(k,True,self.text_color,(255,255,255))
            msg_image_rect=msg_image.get_rect()
            '''centering text image on button'''
            msg_image_rect.centerx=self.scr_rect.centerx
            msg_image_rect.centery=self.scr_rect.centery+75+(20*ctr)
            ctr+=1
            self.draw_mess(msg_image,msg_image_rect)
            
    def draw_mess(self,img,rect):
        self.screen.blit(img,rect)
        
