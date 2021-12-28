x = list(range(1,110))
y = list(range(1,110))

import random as rd

for j in range(0,100):
    k = rd.randrange(1, 100)
    z = rd.randrange(1, k)
    y[k] /= z


import matplotlib.pyplot as plt

plt.plot(x,y)
plt.savefig('plot8.png', dpi = 400)
