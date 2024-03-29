# ch09010404_ReLUFunction.py
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-10, 10, 0.1)
y = relu(x)

print(x)
print(y)

plt.plot(x, y)
plt.title('ReLU function')
plt.show()