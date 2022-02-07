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
    nodes[randint(0,n-1)] = 1

    while not infectionDone:
        for i in range(n):
            for j in range(3):
                if nodes[i] == 1:
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

    nodes[randint(0,n-1)] = 1

    while not infectionDone:
        for i in range(n):
            if nodes[i] == 1:
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

    xpoints_11 = np.array(attempts)
    ypoints_11 = np.array(infectionRate)
    return (xpoints_11, ypoints_11)

def one_inf_one_10pc(): 
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

def one_inf_one_50pc():
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

a,b = one_inf_one()
c,d = one_inf_three()
e,f = one_inf_one_10pc()
g,h = one_inf_one_50pc()

plt.plot(a,b, label = "1o1")
plt.plot(c,d, label = "1o3")
plt.plot(e,f, label = "1o1_10%")
plt.plot(g,h, label = "1o1_50%")
plt.legend()
plt.savefig("lab2/infectionrate_multi.jpg")
plt.show()