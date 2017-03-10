# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 19:06:51 2017

@author: Corey Pullium
"""
import numpy as np
import random
import time

grid_w = 6
grid_h = 6

reward = 0 
moveNum = 0
 
alpha = 0.9
gamma = 0.8
epsilon = 0.5

row = 0
col = 0

row_next = 0
col_next = 0

class spot():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.action = 0
        self.reward = -1
        self.quality = self.up, self.down, self.right, self.left = 0, 0, 0, 0

    
    def Qupdate():
    '''
    Updating the quality of the action that was just taken
    '''
    Current_Q = state[row][col].action
    Next_Qmax = max(state[row_next][col_next].quality)
    
    Current_Q += alpha*(reward + gamma*Next_Qmax - Current_Q)
    
    Q[row][col].action = Current_Q

    
        
state = [[spot(x,y) for y in range(0,grid_h)] for x in range(0,grid_w)]

state[0][3].reward = -100
state[0][4].reward = -100
state[0][5].reward = -100
state[3][0].reward = -100
state[3][1].reward = -100
state[3][2].reward = -100
state[5][3].reward = -100
state[5][4].reward = -100
state[5][5].reward = -100    
state[5][0].reward = 100
     
     
 
def Policy():
    '''
        Deciding what action to take, (greedy or random)
    '''
    if(random.uniform(0,1) < epsilon): 
        action = random.randint(0,3)
    else: 
        Max_actions = [i for i, x in enumerate(state[row][col].quality) if x == max(state[row][col].quality)]
        action = random.choice(Max_actions)
    return action

def TakeAction(action):
    '''
    Checking boundries, changing state, and noting reward
    '''
    global reward, row, col, row_next, col_next
    move = { 'up':0, 'right':1,'down':2,'left':3 }
    
    if(action == move['up'] and row-1 >= 0):
            row_next = row-1
            
    elif(action == move['right'] and col+1 < 6):
            col_next = col + 1
            
    elif(action == move['down'] and row+1 < 6):
            row_next = row + 1
            
    elif(action == move['left'] and col-1 >= 0):
            col_next = col - 1
            
    reward = state[row_next][col_next].reward
    
    print("State:",row, col, action, "State':", row_next, col_next, "R", reward)


def checkExit():
    '''
        Check to see if you Won/Lost or need to keep going
    '''
    global moveNum, row, col, row_next, col_next, epsilon
    
    if(abs(reward) == 100):
       if(reward == 100):
           print "Victory!!!!!!!!!!!!!!!!!!!!!!!"
           time.sleep(3)
       elif(reward == -100):
           print "Doom"
           time.sleep(0.5)
       print (moveNum)
       
       row, col, row_next, col_next = 0, 0, 0, 0
       
       moveNum = 0  
       
    else:
        row = row_next
        col = col_next
        moveNum += 1   

while (1):       
    Policy()
    TakeAction()
    Qupdate()
    checkExit()
