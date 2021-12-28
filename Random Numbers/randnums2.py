x = list(range(1,110))
y = list(range(1,110))

import random as rd

for j in range(0,100):
    k = rd.randrange(100)
    z = rd.randrange(-10,10)
    y[k] *= z


import matplotlib.pyplot as plt

plt.plot(x,y)
plt.savefig('plot7.png', dpi = 400)
