
import numpy as np
import matplotlib.pyplot as plt


#%%
plt.plot([-10,3,7,9],[1,4,8,16], "ro-"),
plt.ylabel("Some numbers")
plt.show()


#let's mix matplotlib and numpy



#%%
t = np.arange(0.,5.,0.2)
plt.plot(t ,t*t,'g^')
plt.show()


