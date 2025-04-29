#FSK

import numpy as np
import matplotlib.pyplot as plt
data=[1,1,0,0,1,1]
t=np.linspace(0,1,1000)
fsk=np.concatenate([5*np.sin(2*np.pi*(10 if bit else 5)*t[:len(t)//len(data)])for bit in data])
task=np.linspace(0,1,len(fsk))
plt.plot(task,fsk)
plt.title('fsk wavefrom for dat[1,1,0,0,1,1]')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()