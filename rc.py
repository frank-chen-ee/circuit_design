import numpy as np
import matplotlib.pyplot as plt

from passive_circuit_analysis import *

start = 1e8
stop  = 80e9
step  = 1e7

f = np.arange(start, stop, step)
s = 1j*2*np.pi*f

r1 = 50
c1 = 750e-15

rclowpass_magnitude_dB = 20*np.log10(abs(voltage_divider(Zr(r1), Zc(c1,s))))

plt.figure()
ax = plt.subplot(111)
plt.semilogx(f, rclowpass_magnitude_dB)
plt.title(r'Ideal RC low pass filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'$\left\|\frac{v_{out}}{v_{in}}\right\|$ (dB)')

plt.show()
