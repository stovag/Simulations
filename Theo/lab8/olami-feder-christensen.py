from random import randint, randrange
import random
import matplotlib.pyplot as plt
import numpy as np

size = 20
surface = [[random.uniform(0,4) for j in range (size)]for i in range(size)]  #instantiate the surface with random values
flow = surface #on the first step, flow is the same as surface
status = [[0 for j in range(size)] for i in range(size)] #instantiate the status list with 0s

for _ in range (2000): #run the simulation for 2000 steps 
    for i in range(20):
        for j in range(20):
            if surface[i][j] >=4.0: critAchieved = True #check if the critical value has been reached in any position
    if (critAchieved == False): #if not
        for i in range(20):
            for j in range(20):
                surface[i][j] += 0.001 #add the Fout value to every cell in the surface
    else: #if it has been reached   
        for i in range(20):
            for j in range(20):
                if flow[i][j] >= 4.0: #find the cells where Fcrit has been reached
                    status[i][j] = 1 #set the status of the cell to 1
                    force = flow[i][j] / 4 #calculate the impact to neighbours
                    flow[i][j] = 0 #set the flow value to 0
                    surface[i][j] = 0 #set the surface value to 0
                    if i == 0: #add the force to the neighbours checking for out of bound values
                        if j == 0:
                           flow[i+1][j] += force
                           flow[i][j+1] += force
                        elif j == 19:
                           flow[i+1][j] += force
                           flow[i][j-1] += force
                        else:
                           flow[i+1][j] += force
                           flow[i-1][j] += force
                           flow[i][j+1] += force
                    elif i == 19:
                        if j == 0:
                           flow[i-1][j] += force
                           flow[i][j+1] += force
                        elif j == 19:
                           flow[i-1][j] += force
                           flow[i][j-1] += force
                        else:
                           flow[i-1][j] += force
                           flow[i][j+1] += force
                           flow[i][j-1] += force
                    else:
                        flow[i-1][j] += force
                        flow[i+1][j] += force
                        flow[i][j+1] += force
                        flow[i][j-1] += force
#that's pretty much all i can figure out 
                        



