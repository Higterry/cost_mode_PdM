"""
Author: Haiyue Wu@Purdue
Date: 10-19-2022
Version: 1.0.0
"""

from scipy.special import gamma as ga
from scipy.stats import gamma, beta
import math
import matplotlib.pyplot as plt
import numpy as np


"""production features"""
MTTF = 3*50*7 #mean time to failure (days)
N_h = 200 #annual production time (hours)
T_m = 2 #time for maintenance (hours)

C_rep = 20000 #replacement cost ($)
C_mt = 200 #cost for miantenance ($)
C_dt = 5000 # cost due to downtime (S)

c_elec = 10 #electricy ($)
P_equp = 7.5 #power of the equipment (watts)
effi = .9 #equipment efficiency (%)


"""model paprameters"""
#gamma distribution
a = 4
#beta distribution

q = 5
p = 2



"""show the pdfs"""

tstep = 100
fig, axs = plt.subplots(3, 1)
fig.set_size_inches(12, 10)

x = np.linspace(0, 1, tstep*3)
t = np.linspace(0,5000, 5000)
# axs[0,0].plot(x, beta.pdf(x, p,q,scale =.5),
#        'r-', lw=3, alpha=0.6, label='beta pdf')
# axs[0,0].set_title('beta distrinbution')
# axs[0,0].legend()
# axs[0,1].plot(x, gamma.pdf(x, a,scale =1),
#        'r-', lw=3, alpha=0.6, label='gamma pdf')
# axs[0,1].set_title('gamma distrinbution')

"""Predictive miantenance"""
main_thrd = 3000 #do maintenance when reached main_thrd
thre = 2500
cycle_len = []
#number of simulation processes
for i in range(3):
    tm = 0

    xr = 0
    # r = gamma.rvs(a, scale = 10, size=100)
    proc = [0]
    count_mt = 0
    ltm = -100
    while True:
        while proc[-1]<main_thrd:
            temp = proc[-1]
            proc.append(temp+gamma.rvs(a, scale=20))  #random gamma scale = 1/beta
            tm+=1

        xr = beta.rvs(10*(np.exp(tm/100)-1),q,scale =3000) #state after maintenance
        # print(xr)
        proc.append(xr)
        for j in range(T_m):
            proc.append(xr)
            tm+=1
        if tm-ltm<30:
            break
        else:
            ltm = tm

        count_mt+=1

    axs[1].plot(t[0:len(proc)], proc,
                'r-', lw=3, alpha=0.6, label='gamma pdf')
    cycle_len.append(len(proc))


#cost calculation

c = C_mt

"""preventive maintenance"""

peirod = 50
fail_thred = 4000
count_mt_pv = 0
for i in range(3):
    tm = 0
    thre = 1600
    xr = 0
    # r = gamma.rvs(a, scale = 10, size=100)
    proc = [0]
    count_mt = 0
    while proc[-1] < fail_thred:
        for j in range(peirod):
            temp = proc[-1]
            proc.append(temp + gamma.rvs(a, scale=10))
            tm+=1
            if proc[-1]>fail_thred:
                break
        xr = beta.rvs(5*(np.exp(tm/100)-1), q, scale=3000)
        if xr>3000:
            break
        proc.append(xr)
        count_mt_pv+=1
        print(tm,xr)
    axs[2].plot(t[0:len(proc)], proc,
                    'r-', lw=3, alpha=0.6, label='gamma pdf')



plt.show()