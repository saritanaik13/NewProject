import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(10)
a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))
plt.hist(a, bins='auto') 
plt.title("Histogram with 'auto' bins")
plt.show()