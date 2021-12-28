import numpy as np
import cmath
import matplotlib.pyplot as plt

pointsx = np.array([])
pointsy = np.array([])

for i in np.linspace(-2,2,2000):
    print(i)
    for j in np.linspace(-2,2,2000):
        c = complex(i,j)
        z = 0
        diverge = False
        for n in np.linspace(1,20,20):
            z = z*z + c
            if (z.real**2 + z.imag**2 > 4):
                diverge = True
                break

        if (diverge == False):
            pointsx = np.append(pointsx, i)
            pointsy = np.append(pointsy, j)
        
plt.scatter(pointsx, pointsy, s=1)
plt.savefig('C:/Users/fotis/Desktop/mandelbrot_python.png',dpi=2000)




