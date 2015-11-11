#use arrows keys to cycle thru options
#
from pygame.locals import *
import pygame, sys, eztext
import time
import random




pygame.init()




display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
scene1 = pygame.image.load('scene1.jpg')
scene2 = pygame.image.load('scene2.jpg')
scene3 = pygame.image.load('scene3.jpg')
scene4 = pygame.image.load('scene4.jpg')



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/1.2))
    gameDisplay.blit(TextSurf, TextRect)        
        


def prsenter():
    message_display('Press Enter')

    
def s1q2():
    pygame.draw.rect(gameDisplay,black,(130,480,550,50))
    
def s1q3():
    pygame.draw.rect(gameDisplay,black,(130,480,550,50))
    
def s1q4():
    pygame.draw.rect(gameDisplay,black,(130,480,550,50))
    

def start_screen():
    startscrn = 1
    while startscrn == 1:
        gameDisplay.fill(black)
        message_display("Press Space")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE: startscrn = 0 
    

def game_loop():
    x = (display_width * 0)
    y = (display_height * 0)
    b = (display_width * 0.45)
    m = (display_height * 0.8)
    
    chgsc = 0
    pygame.event.clear
    questions = 'Hi, What is your name? '
    pygame.draw.rect(gameDisplay,black,(130,480,550,50))
    message_display("")
    txtbx = eztext.Input(maxlength=45, color=(255,255,255), prompt= questions)
    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT: quit()
            txtbx.update(events)
            if event.type == KEYDOWN:
                if event.key == K_RETURN: chgsc=eztext.gametext
                txtbx.restart(events)
            if event.type == KEYUP:
                if event.key == K_RETURN: txtbx.restart(events)
         
        txtbx.set_pos((140),(495))
        txtbx.draw(gameDisplay)
        pygame.display.update()




        
            
            

            


      
        changescene = chgsc
        if (changescene == 0):
            gameDisplay.blit(scene1,(x,y))
        if (changescene == 1):
            
            gameDisplay.blit(scene1,(x,y))
        if (changescene == 2):
            questions = 'Question 2'
            gameDisplay.blit(scene1,(x,y))
        if (changescene >= 3):
            gameDisplay.blit(scene1,(x,y))
        if changescene <= 0:
            s1q2()
        if changescene >= 1:
            s1q2()
        if changescene >= 2:
            s1q3()
        if changescene >= 3:
            s1q4()
        if chgsc==1:
            eztext.gametext2 = 1     
        if chgsc==2:
            eztext.gametext2 = 2
        if chgsc==3:
            eztext.gametext2 = 3
      
        clock.tick(15)
        pygame.display.flip()
    



    

        
        
start_screen()
game_loop()
pygame.display.update()
pygame.quit()

