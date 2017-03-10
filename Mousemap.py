# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 15:24:55 2017

@author: Corey Pullium
"""

import sys, pygame
pygame.init()

size = width, height = 1000, 700
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0 

offsetX = 70
offsetY = 70
spacing = 100
radius = 30

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
                        
    pygame.draw.rect(screen, WHITE, (10,10,620,620), 2) 
    
    
   # points = [(x,y) for x in range(0:6) for y in range(0:6) i*spacing+offsetX, j*spacing+offsetY]
    
    for i in range (0,6):    
        for j in range (0,6):
            
            pygame.draw.circle(screen, WHITE, [i*spacing+offsetX, j*spacing+offsetY], radius, 5)
#==============================================================================
#             pygame.draw.rect(screen, WHITE, (i*100,j*100,100,100), 2) 
#             pygame.draw.polygon(screen, WHITE, [[i*100, j*100], [(i+1)*100, j*100],[i*100+50, (j+1)*100-50]], 2)
#             pygame.draw.polygon(screen, WHITE, [[i*100, (j+1)*100], [(i+1)*100, (j+1)*100],[i*100+50, j*100+50]], 2)
#             pygame.draw.polygon(screen, WHITE, [[i*100, j*100], [i*100, (j+1)*100],[i*100+50, (j+1)*100-50]], 2)
#             pygame.draw.polygon(screen, WHITE, [[(i+1)*100, j*100], [(i+1)*100, (j+1)*100],[(i+1)*100-50, (j+1)*100-50]], 2)
#==============================================================================
              
    pygame.display.update()