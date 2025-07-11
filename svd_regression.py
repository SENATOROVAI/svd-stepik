import matplotlib.pyplot as plt  
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np.vstack([x, np.ones(len(x))]).T

#array([[ 0.,  1.],
#       [ 1.,  1.],
#       [ 2.,  1.],
#       [ 3.,  1.]])

m, c = np.linalg.lstsq(A, y)[0]
print(m,c)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
