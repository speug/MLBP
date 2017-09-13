import numpy as np
import matplotlib as plt

u = [1] + 9*[0]
v = [9/10, 1/10] + 8*[0]
Z = np.random.normal(0,1,(100,10))
x1 = np.dot(Z,u)
x2 = np.dot(Z,v)
plt.scatter(x1,x2)
plt.show()
