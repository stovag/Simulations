from random import randint
import matplotlib.pyplot as plt
import numpy as np

class NodeProps:
    def __init__(self,status):
        self.status = status # 0 = no info, 1 = info received


def multinodes(chance):
    n = 20
    nodesList = [[NodeProps(0) for j in range(n)] for i in range(n)]
    spreadDone = False
    currentSpread = 1
    spreadPerLoop = 0
    spreadRate = []
    curInf = []
    attempts = []
    x=1
    nodesList[0][2].status = 1
    while not spreadDone:
        if (randint(1,100) <= chance):
            for i in range(0,n):
                for j in range(0,n):
                    if nodesList[i][j].status == 1:
                        targetX = randint(0,n-1)
                        targetY = randint(0,n-1)
                        if nodesList[targetX][targetY].status == 0:
                            nodesList[targetX][targetY].status = 1
                            spreadPerLoop+=1
            currentSpread += spreadPerLoop
            curInf.append(currentSpread)
            spreadPerLoop = 0
            spreadRate.append (currentSpread)
            attempts.append(x)
            x+=1
            if currentSpread == n**2:spreadDone = True 

    xpoints = np.array(attempts)
    ypoints = np.array(spreadRate)
    plt.plot(xpoints, ypoints)
    chance = str(chance)
    plt.savefig("Theo/lab5/inforate"+chance+"%.jpg")
    plt.show()

multinodes(100)
multinodes(80)
multinodes(50)
multinodes(30)