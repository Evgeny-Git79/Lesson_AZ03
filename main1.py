import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 100)

plt.hist(data,1000)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('График')

plt.show()


