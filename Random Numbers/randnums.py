x = list(range(1,11))
y = list(range(1,11))

import random as rd

for j in range(0,10):
    k = rd.randrange(10)
    z = rd.randrange(-10,10)
    y[k] *= z


import matplotlib.pyplot as plt

plt.plot(x,y)
plt.savefig('plot5.png', dpi = 400)
