import pygame, sys, eztext
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,240))
screen.fill((255,255,255))
clock = pygame.time.Clock()
baseFont = pygame.font.SysFont(None, 30)
BLACK = (0,0,0)

question = eztext.Input(maxlength=20, color=BLACK, prompt='What is your name? ')

while True:
    clock.tick(30)
    events = pygame.event.get()
    txt = ''

    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    question.draw(screen)
    question.update(events)
    yourname = 'Your name is ' + question.value
    yournameTxt = baseFont.render(yourname, True, BLACK)
    yournameRect = yournameTxt.get_rect()
    yournameRect.top = 50
    screen.blit(yournameTxt, yournameRect)
    

    pygame.display.flip()
