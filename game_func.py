import sys
import pygame
from bullets import Bullet
from thanos import Thanos
from time import sleep
#a substitute module to have all game functions at one place


def check_ev(iron,settings,screen,bullets,thanoss,stats,play_butt,score):
    #for event checker? keyboard responding
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                iron.move_right=True
            if event.key==pygame.K_LEFT:
                iron.move_left=True
            if event.key==pygame.K_SPACE:
                fire_bull(bullets,settings,screen,iron)
            if event.key==pygame.K_q:
                sys.exit()
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                iron.move_right=False
            if event.key==pygame.K_LEFT:
                iron.move_left=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_b(settings,screen,stats,play_butt,mouse_x,mouse_y,iron,bullets,thanoss,score)


def check_play_b(settings,screen,stats,play_butt,mouse_x,mouse_y,ironman,bullets,thanoss,score):
        '''check if the player chooses to play'''
        butt_clicked=play_butt.rect.collidepoint(mouse_x,mouse_y)
        if butt_clicked and not stats.game_active:
            #reset the level ups to normal
            settings.initialize_dynamic_settings()

            #Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            
            '''reset status of the game'''
            stats.reset_stat()
            stats.game_active=True
            '''Preparing new score and level image'''
            score.prep_score()
            score.prep_highscore()
            score.prep_level()
            score.prep_iron()            
            #empty the list of thanoss and bullets
            thanoss.empty()
            bullets.empty()

            #create a new fleet of aliens
            creat_flee(settings,screen,thanoss,ironman)

        
def fire_bull(bullets,settings,screen,iron):
    if len(bullets)<settings.allowed:
        new_bull=Bullet(settings,screen,iron)
        bullets.add(new_bull)

def updat_scr(sett,screen,ironman,bullets,thanos,stats,play_butt,intro,score):
    screen.fill(sett.bg)
    ironman.blitme()
    #thanos.blitme()
    thanos.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bull()
    #draw the button while the game is inactive
    if not stats.game_active:
        play_butt.draw_butt()
        intro.prep_intro(intro.msg)
    # displaying the score
    score.showscore()
    pygame.display.flip()

def update_bull(setting,screen,thanoss,bullets,ironman,stats,score):
    #update the position of bullets
    bullets.update()
    #get rid of old bullets
    for bull in bullets.copy():
        if bull.rect.y<=0:
            bullets.remove(bull)
    chek_bull_than_collisn(setting,screen,ironman,thanoss,bullets,stats,score)

    
def chek_bull_than_collisn(setting,screen,ironman,thanoss,bullets,stats,score):
    #check for collision with thanos
    #if so remove the bullet and thanos
    collision=pygame.sprite.groupcollide(bullets,thanoss,True,True)
    if collision:
        for than in collision.values():
            stats.score+=setting.point*len(than)
            score.prep_score()
        check_high_score(stats,score)

    '''repopulating the fleet'''
    if len(thanoss)==0:
        '''fleet destroyed'''
        #destroy existing bullets
        bullets.empty()
        #speeding up tha game
        setting.increase_speed()
        #new level
        stats.level+=1
        score.prep_level()
        creat_flee(setting,screen,thanoss,ironman)
    
     
def get_num_th_x(setting,th_width):
    av_spac_x=setting.width-(th_width)
    numb_th_x=int(av_spac_x/(2*th_width))
    return numb_th_x

def get_num_row(setting,ironhei,th_height):
    av_spc_row=setting.height-2*ironhei
    num_row=int(av_spc_row/(1.5*th_height))
    return num_row

def creat_than(setting,screen,th,thanoss,row):  #th=thanos no.
    #create thanos and in a row
    thanos=Thanos(setting,screen)
    th_width=thanos.rect.width
    th_height=thanos.rect.height
    thanos.x=int(1*th_width)+2*th_width*th
    thanos.rect.x=thanos.x
    thanos.y=(0.5*th_height)+row*(1.5*th_height)
    thanos.rect.y=thanos.y
    thanoss.add(thanos)

    
def creat_flee(setting,screen,thanoss,ironman):
    ''' create a alien fleet'''
    #create a fleet
    #find the no. of thanoses in a row
    #spacing = thanos width
    thanos=Thanos(setting,screen)
    th_width=thanos.rect.width
    th_height=thanos.rect.height
    numb_th_x=get_num_th_x(setting,th_width)
    ironhei=ironman.rect.height
    num_th_r=get_num_row(setting,ironhei,th_height)
    #craete thanos row
    for row in range(0,num_th_r):
        for th in range(0,numb_th_x):
            creat_than(setting,screen,th,thanoss,row)


def check_fleet_edges(setting,thanoss):
    ''' respond if fleet has reached any edge'''
    for thanos in thanoss.sprites():
        if thanos.check_edge():
            change_direct(setting,thanoss)
            break

def change_direct(setting,thanoss):
    '''drop the fleet and change direction'''
    for thanos in thanoss.sprites():
        thanos.rect.y+=setting.drop_spe
    setting.direct*=-1

def check_th_bott(setting,stats,screen,ironman,thanoss,bullets,score):
        '''check idf thanos reached the bottom'''
        scr_rect=screen.get_rect()
        for thanos in thanoss.sprites():
            if thanos.rect.bottom>=scr_rect.bottom:
                '''indirectly ironman is hit'''
                iron_hit(setting,stats,screen,ironman,thanoss,bullets,score)
                break
            
def updat_tha(setting,ironman,thanoss,stats,screen,bullets,score):
    '''check if fleet is at edge'''
    '''update positions of all the thanoses in group'''
    check_fleet_edges(setting,thanoss)
    thanoss.update()
    '''check if any thanoss reached bottom and take action if so'''
    check_th_bott(setting,stats,screen,ironman,thanoss,bullets,score)
    ''' look for alien ship collisions'''
    if pygame.sprite.spritecollideany(ironman,thanoss):
        iron_hit(setting,stats,screen,ironman,thanoss,bullets,score)


def iron_hit(setting,stats,screen,ironman,thanoss,bullets,score):
    ''' respond to ironman hit by thanoss'''
    if stats.iron_life>0:
        #decreasing ironmans battery source left
        stats.iron_life-=1

        #update the scoreboard
        score.prep_iron()

        #remove all thanoss and bullets
        bullets.empty()
        thanoss.empty()

        #create a new fleet of thanos
        creat_flee(setting,screen,thanoss,ironman)
        #ironman centered
        ironman.center_iron()

        #Pause
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_high_score(stats,score):
    '''check to see if there's a new high score'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        score.prep_highscore()
    


