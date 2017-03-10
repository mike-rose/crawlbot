# -*- coding: utf-8 -*-
"""
this makes the png 
"""

import sys, pygame, random, time
from pygame.draw import lines as line
from pygame.draw import circle

grid_w, grid_h = 6, 6

alpha = 0.9
gamma = 0.8
epsilon = 0.9
epsilonRate = 0.95
iterations = 10000

row, col, row_x, col_x, moveNum = 0, 0, 0, 0, 0

class spot():

    def __init__(self):
        self.reward = -1
        self.quality = [0, 0, 0, 0]  # up, right, down, left

    def policy(self):
        '''
            Deciding what action to take (highest quality or random)
        '''
        if(random.uniform(0,1) < epsilon):
            action = random.randint(0,3)
        else:
            best_actions = [i for i, x in enumerate(self.quality) \
                            if x == max(self.quality)]
            action = random.choice(best_actions)
        return action
    
    def updateQ(self, action):
        '''
        Updating the quality of the action that was just taken
        '''
        global row_x, col_x, row, col, moveNum, epsilon
        moveNum += 1

        old_q = self.quality[action]
        nextBest = max(state[row_x][col_x].quality)
        nextReward = state[row_x][col_x].reward
        self.quality[action] += alpha*(nextReward + gamma*nextBest - old_q)

        if(abs(nextReward) == 100):
            if(nextReward < 0):
                pass
                #print("Doom after " + str(moveNum) + " moves.")
            elif(nextReward > 0):
                #print("Victory after " + str(moveNum) + " moves.")
                epsilon = epsilon*epsilonRate
            # start over
            row, col, row_x, col_x = 0, 0, 0, 0
            moveNum = 0

        else:
            # keep going
            row = row_x
            col = col_x

def takeAction():
    '''
    Checking boundries, changing state, and noting reward
    '''
    global row_x, col_x, row, col
    
    action = state[row][col].policy()  # get an action
    
    if(action == 0 and row-1 >= 0):  # up
        row_x = row -1
    elif(action == 1 and col+1 < 6):  # right
        col_x = col +1
    elif(action == 2 and row+1 < 6):  # down
        row_x = row +1
    elif(action == 3 and col-1 >= 0):  # left
        col_x = col -1

    state[row][col].updateQ(action)  # update quality
    

def maxQ():
    maxq = -100
    for i in range(0,grid_w):
        for j in range(0,grid_h):
            if max(state[i][j].quality) > maxq:
                maxq = max(state[i][j].quality)
    return maxq

def minQ():
    minq = 100
    for i in range(0,grid_w):
        for j in range(0,grid_h):
            if min(state[i][j].quality) < minq:
                minq = min(state[i][j].quality)
    return minq
    
def color(quality):
    r,g = 0,0
    if (quality < 0):
        r = 255*quality/(-100)
    elif (quality > 0):
        g = 255*quality/(100)
    return (r,g,0)


state = [[spot() for y in range(0,grid_h)] for x in range(0,grid_w)]

setattr(state[0][3], 'reward', -100)
setattr(state[0][4], 'reward', -100)
setattr(state[0][5], 'reward', -100)
setattr(state[3][0], 'reward', -100)
setattr(state[3][1], 'reward', -100)
setattr(state[3][2], 'reward', -100)
setattr(state[5][3], 'reward', -100)
setattr(state[5][4], 'reward', -100)
setattr(state[5][5], 'reward', -100)
setattr(state[5][0], 'reward', 100)


############################################
#              START GUI
############################################
size = width, height = 400, 400
pixWid = width/grid_w
offset = pixWid/2
qThick = pixWid/8
ll = pixWid/16
rad = pixWid/4
############################################

pygame.init()
gui = pygame.display.set_mode(size)

for s in range(iterations):
    '''  
    A single movement/action/update...
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
    
    takeAction()

    for i in range(0, grid_h):
        for j in range(0, grid_w):

            x,y = j*pixWid+offset, i*pixWid+offset
            circle(gui, (190,190,190), (x,y), rad, 0)
            
            q = state[i][j].quality  # [up-q, right-q, down-q, left-q]
            
            line(gui,color(q[0]),True,((x-ll,y-rad),(x-ll,y-pixWid+rad)),ll*2)
            line(gui,color(q[1]),True,((x+rad,y-ll),(x+pixWid-rad,y-ll)),ll*2)
            line(gui,color(q[2]),True,((x+ll,y+rad),(x+ll,y+pixWid-rad)),ll*2)
            line(gui,color(q[3]),True,((x-rad,y+ll),(x-pixWid+rad,y+ll)),ll*2)
            
    pygame.display.update()


# highlight the best route
moveDelay = 0.25
row, col, movNum = 0, 0, 0

circle(gui,(0,191,255),(offset,offset),rad,0)
pygame.display.update()

while(state[row][col].reward < 99):
    time.sleep(moveDelay)
    best_actions = [i for i, b in enumerate(state[row][col].quality) \
                                if b == max(state[row][col].quality)]
    action = random.choice(best_actions)
        
    if(action == 0):    # up
        row += -1
    elif(action == 1):  # right
        col += 1
    elif(action == 2):  # down
        row += 1
    elif(action == 3):  # left
        col += -1
    
    moveNum += 1
    circle(gui,(0,191,255),(col*pixWid+offset,row*pixWid+offset),rad,0)
    pygame.display.update()
    
    
# close 5 seconds after completion
time.sleep(5)
pygame.quit(); sys.exit();
  

