#Sampling 

import numpy as np
import matplotlib.pyplot as plt
l=1
t=np.linspace(0,2,500)
ts=np.linspace(0,2)
sig=10*np.sin(2*np.pi*l*t)
sigsamp=10*np.sin(2*np.pi*l*ts)
sq=np.round(sig*2)/2
sq=np.round(sigsamp*2)/2
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
plt.plot(t,sig)
plt.subplot(2,1,2)
plt.step(ts,sq)