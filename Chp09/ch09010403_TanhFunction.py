# ch09010403_TanhFunction.py
import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return ((np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)))

x = np.arange(-10, 10, 0.1) 
y = tanh(x) 

print(x)
print(y)

plt.plot(x, y)
plt.title('tanh function')
plt.show()