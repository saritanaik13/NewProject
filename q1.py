import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
np.random.seed(1234)
abc = pd.DataFrame(np.random.randn(10,4),
                   columns=['Col1', 'Col2', 'Col3', 'Col4'])
boxplot = abc.boxplot(column=['Col1', 'Col2', 'Col3'])
plt.show()