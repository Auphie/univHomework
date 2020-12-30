import numpy as np
a=np.arange(0,60).reshape(4,3,5)
print('a=',a)
print('a1=',a[0,1,2])
print('a2=',a[:,2])
print('a3=',a[:,:,2])
print('a4=',a[::2,::2,::2])
