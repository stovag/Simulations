from random import randint
import matplotlib.pyplot as plt
import numpy as np

class NodeProps: #class for node properties
    def __init__(self,status):
        self.status = status # 0 = no info, 1 = info received

def multinodes(n): #start function with the specified network size
    nodesList = [[NodeProps(0) for j in range(n)] for i in range(n)]
    spreadDone = False
    currentSpread = 1
    spreadPerLoop = 0
    spreadRate = []
    curInf = []
    attempts = []
    x=1
    nodesList[randint(0,n-1)][randint(0,n-1)].status = 1 #set the first node to infected
    while not spreadDone: #while the spread is not done
        for i in range(0,n):
            for j in range(0,n):
                if nodesList[i][j].status == 1: #if the node is infected
                    targetX = randint(0,n-1) #target a random node
                    targetY = randint(0,n-1)
                    if nodesList[targetX][targetY].status == 0: #if the target node is not infected
                        nodesList[targetX][targetY].status = 1 #infect the target node
                        spreadPerLoop+=1
        currentSpread += spreadPerLoop
        curInf.append(currentSpread)
        spreadPerLoop = 0
        spreadRate.append (currentSpread)
        attempts.append(x)
        x+=1
        if currentSpread == n**2:spreadDone = True #if the spread is done, stop the loop

    xpoints = np.array(attempts)
    ypoints = np.array(spreadRate)
    plt.plot(xpoints, ypoints) #plot the spread rate
    #n = str(n) variable conversion to string for the plot file name
    #plt.savefig("Theo/lab6/inforate"+n+".jpg") disabled because file structure will change
    plt.show()

multinodes(50)
multinodes(30)
multinodes(10)
multinodes(5)