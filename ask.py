#ASK

import numpy as np
import matplotlib.pyplot as plt
data=[1,1,0,1]
fc=10
t=np.linspace(0,1,1000)
ask=np.concatenate([(5 if bit else 0)*np.sin(2*np.pi*fc*t[:len(t)//len(data)])for bit in data])
task=np.linspace(0,1,len(ask))
plt.plot(task,ask)
plt.title('ASK waveform for data[1,1,0,1]')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()