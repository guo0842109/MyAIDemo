
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation
import numpy as np

pi=np.pi
theta=pi/2
trans=np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta),np.cos(theta)]])
array=np.zeros([2,1000])
array[0,:]=np.linspace(0,1,1000)
array[1,:]=np.linspace(0,1,1000)
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.plot(array[0,:],array[1,:])
ax.set_aspect(1)
array2=trans.dot(array)
fig=plt.figure(2)
ax=fig.add_subplot(111)
ax.plot(array2[0,:],array2[1,:])
ax.set_aspect(1)
plt.show()
