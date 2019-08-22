import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
median = np.percentile(a, 50)
m=np.mean(a)
Quartile_1= np.percentile(a,25)
Quartile_3= np.percentile(a,75)
print(median)
print(m)
print(Quartile_1)
print(Quartile_3)

