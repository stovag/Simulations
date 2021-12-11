import numpy as np
from matplotlib import pyplot as plt

nodes = np.zeros(10000)
nodes[r.randint(1, 999)] = 1
infected = 1
l = []

while infected < 1000:
    for i in range(infected):
        target = r.randint(0, 999)
        if nodes[target] == 0:
            nodes[target] = 1
            infected += 1
    l.append(infected)

d = [l[i]-l[i-1] for i in range(1, len(l))]
print("Steps:", len(d))

plt.plot(l)
plt.title("Infected per Step")
plt.show()

plt.plot(d)
plt.title("Infection Rate per Step")
plt.show()
