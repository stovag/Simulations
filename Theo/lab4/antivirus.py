import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np

class NodeProps:
    def __init__(self,status, infection_lambda):
        self.status = status # 0 = healthy, 1 = infected, 2 = recovered
        self.infection_lambda = infection_lambda # time until node recovers

    
def multinodes(n):
    nodesList = [0] * n
    for i in range(0,n):nodesList[i] = NodeProps(0,0)
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1
    nodesList[5] = NodeProps(1,0)
    while not infectionDone:
        for i in range(n):
            if nodesList[i].status == 1:
                target = randint(0,n-1)
                if nodesList[target].status == 0:
                    nodesList[target].status = 1
                    infectedPerLoop+=1
        for i in range(n):
            if nodesList[i].status == 1:
                nodesList[i].infection_lambda += 1
        for i in range(n):    
            if nodesList[i].infection_lambda == 10:
                nodesList[i].status = 2

        currentInfected += infectedPerLoop
        curInf.append(currentInfected)
        infectedPerLoop = 0
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        if currentInfected == n:infectionDone = True 

    xpoints = np.array(attempts)
    ypoints = np.array(infectionRate)
    plt.plot(xpoints, ypoints)
    n = str(n)
    #plt.savefig("Theo/lab4/infectionrate"+n+".jpg") disabled since file structure will change
    plt.show()

multinodes(50)
multinodes(100)
multinodes(500)
multinodes(1000)
