"""
Author: Haiyue Wu@Purdue
Date: 10-24-2022
Version: 1.0.0
"""

from scipy.special import gamma as ga
from scipy.stats import gamma, beta
import math
import matplotlib.pyplot as plt
import numpy as np

a = 4
q = 5
p = 2

tstep = 20
fig, axs = plt.subplots(5, 1)
fig.set_size_inches(10, 10)
mean, var, skew, kurt = gamma.stats(a, moments='mvsk')

x = np.linspace(0, 50, tstep*3)
t = np.linspace(0,1, tstep*3)
axs[0].plot(x, gamma.pdf(x,4,scale =4),
       'r-', lw=3, alpha=0.6, label='beta pdf')

axs[1].plot(x, gamma.pdf(x, 3, scale =1),
       'r-', lw=3, alpha=0.6, label='a=3 b=1')
axs[1].plot(x, gamma.pdf(x, 5, scale =1),
       'b-', lw=3, alpha=0.6, label='a=5 b=1')
axs[1].plot(x, gamma.pdf(x, 7,scale =1),
       'p-', lw=3, alpha=0.6, label='a=7 b=1')
axs[1].legend()


axs[2].plot(x, gamma.pdf(x, 3, scale =.5),
       'r-', lw=3, alpha=0.6, label='a=3 b=2')
axs[2].plot(x, gamma.pdf(x, 5, scale =.5),
       'b-', lw=3, alpha=0.6, label='a=5 b=2')
axs[2].plot(x, gamma.pdf(x, 7, scale =.5),
       'p-', lw=3, alpha=0.6, label='a=7 b=2')
axs[2].legend()

axs[3].plot(x, gamma.pdf(x, 3, scale =2),
       'r-', lw=3, alpha=0.6, label='a=3 b=.5')
axs[3].plot(x, gamma.pdf(x, 5, scale =2),
       'b-', lw=3, alpha=0.6, label='a=5 b=.5')
axs[3].plot(x, gamma.pdf(x, 7, scale =2),
       'p-', lw=3, alpha=0.6, label='a=7 b=.5')
axs[3].legend()

s = 1
axs[4].plot(t, beta.pdf(t, 6,5, scale =s),
       'r-', lw=3, alpha=0.6, label='a=1 b=.5')
axs[4].plot(t, beta.pdf(t, 7,5, scale =s),
       'b-', lw=3, alpha=0.6, label='a=2 b=.5')
axs[4].plot(t, beta.pdf(t, 8,5, scale =s),
       'p-', lw=3, alpha=0.6, label='a=3 b=.5')

axs[4].plot(t, beta.pdf(t, 9,5, scale =s),
       'p-', lw=3, alpha=0.6, label='a=4 b=.5')

axs[4].plot(t, beta.pdf(t, 10,5, scale =s),
       'p-', lw=3, alpha=0.6, label='a=5 b=.5')

axs[4].plot(t, beta.pdf(t, 20,5, scale =s),
       'p-', lw=3, alpha=0.6, label='a=6 b=.5')
axs[4].legend()


plt.show()