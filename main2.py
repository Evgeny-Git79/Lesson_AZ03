import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
print(x)
y = np.random.rand(10)
print(y)

plt.scatter(x,y)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('График')

plt.show()
