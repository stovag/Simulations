import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np



def one_inf_three():
    n = 1000
    nodes = [0] * n
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1
    nodes[randint(0,n-1)] = 1 #first infection done here to keep the while loop simple
    
    while not infectionDone:
        for i in range(n):
            if nodes[i] == 1: #if the node is infected, target a random node
                for _ in range(3): #since one node is infected, there are 3 nodes to infect
                    target = randint(0,n-1)
                    if nodes[target] == 0: #if the target is not infected, infect it
                        nodes[target] = 1
                        infectedPerLoop+=1
                    currentInfected += infectedPerLoop #buffer variable to keep track of how many nodes were infected in the current loop
                    curInf.append(currentInfected)
                    infectedPerLoop = 0
        infectionRate.append (currentInfected) #append the current infection rate to the list
        attempts.append(x) #append the current attempt to the list
        x+=1
        if currentInfected == n:
            infectionDone = True #if all nodes are infected, stop the loop
    xpoints_13 = np.array(attempts)
    ypoints_13 = np.array(infectionRate)
    return(xpoints_13, ypoints_13)

def one_inf_one():
    n = 1000
    nodes = [0] * n
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1

    nodes[randint(0,n-1)] = 1 #first infection done here to keep the while loop simple

    while not infectionDone:
        for i in range(n):
            if nodes[i] == 1: #if the node is infected, target a random node
                target = randint(0,n-1)
                if nodes[target] == 0: #if the target is not infected, infect it
                    nodes[target] = 1
                    infectedPerLoop+=1
            currentInfected += infectedPerLoop
            curInf.append(currentInfected)
            infectedPerLoop = 0
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        if currentInfected == n:infectionDone = True #if all nodes are infected, stop the loop

    xpoints_11 = np.array(attempts)
    ypoints_11 = np.array(infectionRate)
    return (xpoints_11, ypoints_11) #return 2 arrays to be plotted

def one_inf_one_10pc(): #function below works like the ones above, but with a 10% chance of infection
    n = 1000
    nodes = [0] * n
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1

    nodes[randint(0,n-1)] = 1

    while not infectionDone:
        for i in range(n):
            if nodes[i] == 1:
                if 0<=random.randint(0,9)<=1:
                    target = randint(0,n-1)
                    if nodes[target] == 0:
                        nodes[target] = 1
                        infectedPerLoop+=1
            currentInfected += infectedPerLoop
            curInf.append(currentInfected)
            infectedPerLoop = 0
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        if currentInfected == n:infectionDone = True 

    xpoints_11_10p = np.array(attempts)
    ypoints_11_10p = np.array(infectionRate)
    return(xpoints_11_10p,ypoints_11_10p)

def one_inf_one_50pc(): #function below works like the ones above, but with a 50% chance of infection
    n = 1000
    nodes = [0] * n
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1

    nodes[randint(0,n-1)] = 1

    while not infectionDone:
        for i in range(n):
            if nodes[i] == 1:
                if 0<=random.randint(0,9)<=4:
                    target = randint(0,n-1)
                    if nodes[target] == 0:
                        nodes[target] = 1
                        infectedPerLoop+=1
            currentInfected += infectedPerLoop
            curInf.append(currentInfected)
            infectedPerLoop = 0
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        if currentInfected == n:infectionDone = True 

    xpoints_11_50p = np.array(attempts)
    ypoints_11_50p = np.array(infectionRate)
    return(xpoints_11_50p, ypoints_11_50p)

 #transfer the arrays from the functions above to plot them
a,b = one_inf_one()
c,d = one_inf_three()
e,f = one_inf_one_10pc()
g,h = one_inf_one_50pc()
#plot the arrays
plt.plot(a,b, label = "1o1")
plt.plot(c,d, label = "1o3")
plt.plot(e,f, label = "1o1_10%")
plt.plot(g,h, label = "1o1_50%")
plt.legend()
#plt.savefig("lab2/infectionrate_multi.jpg") disabled since file structure will change
plt.show()