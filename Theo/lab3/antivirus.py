from random import randint
import matplotlib.pyplot as plt
import numpy as np

class NodeProps: #create a class to store the properties of each node
    def __init__(self,status, infection_lambda):
        self.status = status # 0 = healthy, 1 = infected, 2 = recovered
        self.infection_lambda = infection_lambda # time until node recovers

    
n = 1000
nodesList = [0] * n #instantiate an empty list of nodes
for i in range(0,n):nodesList[i] = NodeProps(0,0) #instantiate each node with status 0 (healthy) and infection_lambda 0 (0 epochs since infection)
infectionDone = False
currentInfected = 1
infectedPerLoop = 0
infectionRate = []
attempts = []
x=1
nodesList[5] = NodeProps(1,0) #first infection done here to keep the while loop simple
while not infectionDone: #while the infection is not done
    for i in range(n):
        if nodesList[i].status == 1: #if the node is infected, target a random node
            target = randint(0,n-1) #target a random node
            if nodesList[target].status == 0: #if the target is not infected, infect it
                nodesList[target].status = 1
                infectedPerLoop+=1 #increment the number of infected nodes
    for i in range(n): 
        if nodesList[i].status == 1: #if the node is infected, count one epoch up for every loop
            nodesList[i].infection_lambda += 1
    for i in range(n):    
        if nodesList[i].infection_lambda == 10: #if the node has been infected for 10 epochs, it recovers
            nodesList[i].status = 2

    currentInfected += infectedPerLoop
    infectedPerLoop = 0
    infectionRate.append (currentInfected) 
    attempts.append(x)
    x+=1
    if currentInfected == n:infectionDone = True #if all nodes are infected, stop the loop

xpoints = np.array(attempts)
ypoints = np.array(infectionRate)
plt.plot(xpoints, ypoints)
#plt.savefig("/lab3/infectionrate.jpg") disabled because file structure will change
plt.show()