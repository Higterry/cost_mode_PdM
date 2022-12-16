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
tx = np.linspace(0,500, 500)

"""Predictive miantenance"""
main_thrd = 1000 #do maintenance when reached main_thrd
cycle_len = []
main_count = []
#number of simulation processes
for i in range(1000):
    tm = 0

    xr = 0
    # r = gamma.rvs(a, scale = 10, size=100)
    proc = [0]
    count_mt = 0
    # ltm = -100
    main_index = 1
    q = 5
    t = math.exp(main_index*0.316)-1
    fail_rate = 1.2
    # while True:
    while proc[-1]<main_thrd*fail_rate:
        temp = proc[-1]
        proc.append(temp+gamma.rvs(a, scale=5))  #random gamma scale = 1/beta
        # proc.append(beta.rvs(t*q,q,scale=main_thrd))
        # # print(proc[-1])
        # temp = proc[-1]
        # if temp>=main_thrd*.9: # determin what status to refurbish/replace the pump
        #     # print(main_index)
        #     while proc[-1] < main_thrd:
        #         temp = proc[-1]
        #         proc.append(temp + gamma.rvs(a, scale=4))  # random gamma scale = 1/beta
        #     break
        # # proc.append() #time used for conducting maintenance
        # main_index += 1
        # t = math.exp(main_index * 0.316) - 1

    axs[1].plot(tx[0:len(proc)], proc,'r-', lw=2, alpha=0.6, label='gamma pdf')
    axs[1].axhline(y=1200, color='b', linestyle='--')
    cycle_len.append(len(proc))
    main_count.append(main_index)
cl = np.array(cycle_len)
mc = np.array(main_count)

print(cl.mean(),mc.mean())
plt.show()