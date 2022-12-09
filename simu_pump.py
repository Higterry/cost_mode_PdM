"""
Author: Haiyue Wu wu1254@Purdue
Date: 11-30-2022
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


T_m = 2 #time for maintenance (hours)

fig, axs = plt.subplots(2, 1)
t = np.linspace(0,500, 500)

"""Predictive miantenance"""
main_thrd = 1000 #do maintenance when reached main_thrd
thre = 2500
cycle_len = []
#number of simulation processes
for i in range(1):
    tm = 0

    xr = 0
    # r = gamma.rvs(a, scale = 10, size=100)
    proc = [0]
    count_mt = 0
    ltm = -100

    while proc[-1]<main_thrd:
        temp = proc[-1]
        proc.append(temp+gamma.rvs(a, scale=5))  #random gamma scale = 1/beta
        tm+=1


    axs[1].plot(t[0:len(proc)], proc,
                'r-', lw=2, alpha=0.6, label='gamma pdf')
    cycle_len.append(len(proc))

plt.show()