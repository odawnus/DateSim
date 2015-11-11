#Veronica Update
from pygame.locals import *
import pygame, sys, eztext
import time
import random


pygame.init()


display_width = 800
display_height = 600
txtbox_width = 650
txtbox_height = 50

black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)

textDisplay = pygame.display.set_mode((txtbox_width,txtbox_height))
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
scene1 = pygame.image.load('scene1.jpg')
scene2 = pygame.image.load('scene2.jpg')
scene3 = pygame.image.load('scene3.jpg')
scene4 = pygame.image.load('scene4.jpg')
gameExit = False
changescene = 0



   
def s1q2():
    pygame.draw.rect(textDisplay,black,(100,480,650,50))
    
def s1q3():
    pygame.draw.rect(textDisplay,black,(100,480,650,50))
    
def s1q4():
    pygame.draw.rect(textDisplay,black,(100,480,650,50))
    


def game_loop():
    x = (display_width * 0)
    y = (display_height * 0)
    b = (display_width * 0.45)
    m = (display_height * 0.8)
    changescene = 0
    txtbx = eztext.Input(maxlength=200, x=120,y=490,color=(255,255,255), prompt='Hi, My name is Carol. What is your name? ')
    
    
    
    while not gameExit:


        if changescene == 0:
            
            gameDisplay.blit(scene1,(x,y))
            s1q2()
            txtbx.draw(textDisplay)
            pygame.display.update()
            clock.tick(30)
            events = pygame.event.get()
         
            

            for event in events:
                
                # update txtbx
                txtbx.update(events)
                
                # blit txtbx on the sceen
                txtbx.draw(textDisplay)
                pygame.display.flip()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                   
                    # refresh the display
                    pygame.draw.rect(textDisplay,black,(200,480,650,50))
                    gameDisplay.blit(scene2,(x,y))
                    s1q3()
                    
                    val = txtbx.update(events)
                    sceneText2 = 'Hi, {}!, What Do you want to do?'.format(val)
                    txtbx = eztext.Input(maxlength=200, x=120,y=490, color=(255,255,255), prompt=sceneText2)
                    txtbx.draw(textDisplay)
                    pygame.display.update()
                    changescene = 2
                    
                   
                    
                    
                   
        if changescene == 2:
          clock.tick(30)
          
          events = pygame.event.get()
          for event in events:
              # update txtbx
              txtbx.update(events)
              # blit txtbx on the sceen
              txtbx.draw(textDisplay)
              pygame.display.flip()
              if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
               
                # refresh the display
                pygame.draw.rect(textDisplay,black,(200,480,650,50))
                gameDisplay.blit(scene3,(x,y))
                s1q4()
                val = txtbx.update(events)
                sceneText3 = 'Ok, Lets {}!'.format(val)
                txtbx = eztext.Input(maxlength=200, x=120,y=490, color=(255,255,255), prompt=sceneText3)
                txtbx.draw(textDisplay)
                pygame.display.update()
                changescene = 3
                


  
  
       
       
        
    
        
        
    



    

        
        

  
game_loop()

