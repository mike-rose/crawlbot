# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 19:06:51 2017

@author: Corey Pullium
"""

import random
import time

grid_w = 6  # width of grid
grid_h = 6  # height of grid

alpha = 0.9
gamma = 0.8
epsilon = 0.7

row = 0
col = 0
row_x = 0
col_x = 0

moveNum = 0
action = -1

class spot():
    
    def __init__(self):
        self.reward = -1
        self.quality = [0, 0, 0, 0]
    
    def policy(self):
        '''
            Deciding what action to take, (greedy or random)
        '''
        global action
        
        if(random.uniform(0,1) < epsilon): 
            action = random.randint(0,3)
        else: 
            best_actions = [i for i, x in enumerate(self.quality) \
                            if x == max(self.quality)]
            action = random.choice(best_actions)

    def takeAction(self):
        '''
        Checking boundries, changing state, and noting reward
        '''
        global row_x, col_x, row, col, action
        
        if(action == 0 and row-1 >= 0):  # up
            row_x = row -1
        elif(action == 1 and row+1 < 6):  # down
            row_x = row +1
        elif(action == 2 and col-1 >= 0):  # left
            col_x = col -1
        elif(action == 3 and col+1 < 6):  # right
            col_x = col +1
        
             
    def updateQ(self):
        '''
        Updating the quality of the action that was just taken
        '''
        global row_x, col_x, row, col, action, moveNum, epsilon
        moveNum += 1
        
        old_q = self.quality[action]
        nextBest = max(state[row_x][col_x].quality)
        nextReward = state[row_x][col_x].reward
        self.quality[action] += alpha*(nextReward + gamma*nextBest - old_q)
        
        if(nextReward == 100):
            #print "Victory!"
            #time.sleep(1)
            #print(moveNum)
            epsilon = epsilon*0.9
            
            #start over
            row, col, row_x, col_x = 0, 0, 0, 0
            moveNum = 0  
            
        elif(nextReward == -100):
            #print "Doom"
            #time.sleep(0.05)
            #print (moveNum)
            
            #start over
            row, col, row_x, col_x = 0, 0, 0, 0
            moveNum = 0  
           
        else:
            row = row_x
            col = col_x
        

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


while (1):
    global row, col, row_x, col_x
    state[row][col].policy()
    state[row][col].takeAction()
    state[row][col].updateQ()
    
    
