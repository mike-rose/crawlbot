# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 19:06:51 2017

@author: Corey Pullium
"""
import numpy as np
import random
import time


Q = np.zeros((6,6,4))     #State/action map


R = np.ones((6,6))        #Reward map 
R *= -1                 #Moving gets small negative reward
R[0][3:] = -100
R[3][:3] = -100
R[5][3:] = -100
R[5][0] = 100
 
Reward = 0 
moveNum = 0
 
 
alpha = 0.9
gamma = 0.8
epsilon = 0.5

Row = 0
Col = 0

Row_Prime = 0
Col_Prime = 0

Action = 0
Max_actions = {}


def Policy():
    '''
        Deciding what action to take, (greedy or random)
    '''
    global Action
    if(random.uniform(0,1) < epsilon): 
        Action = random.randint(0,3)
    else: 
        Max_actions = [i for i, x in enumerate(Q[Row][Col]) if x == max(Q[Row][Col])]
        Action = random.choice(Max_actions)

def TakeAction():
    '''
    Checking boundries, changing state, and noting reward
    '''
    global Reward, Row, Col, Row_Prime, Col_Prime
    
    if(Action == 0):
        if(Row-1 >= 0): 
            Row_Prime -= 1
            
    if(Action == 1):
        if(Col+1 < 6): 
            Col_Prime += 1
            
    if(Action == 2):
        if(Row+1 < 6): 
            Row_Prime += 1
            
    if(Action == 3):
        if(Col-1 >= 0): 
            Col_Prime -= 1
            
    Reward = R[Row_Prime][Col_Prime]
    
    print("State:",Row, Col, Action, "State':", Row_Prime, Col_Prime, "R", Reward)

def Qupdate():
    '''
    Updating the quality of the action that was just taken
    '''
    global Q
    Current_Q = Q[Row][Col][Action]
    Next_Qmax = max(Q[Row_Prime][Col_Prime])
    
    Current_Q += alpha*(Reward + gamma*Next_Qmax - Current_Q)
    
    Q[Row][Col][Action] = Current_Q

def checkExit():
    '''
        Check to see if you Won/Lost or need to keep going
    '''
    global moveNum, Row, Col, Row_Prime, Col_Prime
    
    if(abs(Reward) == 100):
       if(Reward == 100):
           print "Victory!!!!!!!!!!!!!!!!!!!!!!!"
           time.sleep(3)
       elif(Reward == -100):
           print "Doom"
           time.sleep(0.5)
       print (moveNum)
       
       Row, Col, Row_Prime, Col_Prime = 0, 0, 0, 0
       
       moveNum = 0  
       
    else:
        Row = Row_Prime
        Col = Col_Prime
        moveNum += 1   

while (1):       
    Policy()
    TakeAction()
    Qupdate()
    checkExit()
