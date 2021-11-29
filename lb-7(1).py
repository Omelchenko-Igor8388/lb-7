import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-3,3)
y1 = np.sin(10*x)
y = 2**x*y1

ax.plot(x, y)

plt.show()

