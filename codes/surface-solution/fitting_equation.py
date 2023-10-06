import numpy as np
import matplotlib.pyplot as plt
import math

S=5*10**(-5)
V=4*10**(-8)
# time interval for each loop, unit:second
dt = 0.001
# time spots, unit:minute
n_ = [5,10,15,20,25,30,35,40]
n = n_[7]*60/dt
# initial ligand concentration, unit: ug/ml
L_tot_=[0.5, 10, 20, 40, 80]
# if ligand is Igg(MW:50kDa), initial ligand concentration, unit: mol/m^3
L_tot=L_tot_[0]*2*10**(-5)

def get_RL(k_on,k_off,R_tot):
    rl=0
    C = k_on*S/V
    A = k_on*R_tot*L_tot
    B = k_on*(R_tot*S/V+L_tot)+k_off
    data = np.zeros((n,))
    for index in range(n):
        rl = rl + (C*rl**2-B*rl+A)*dt
        data[index]=rl/R_tot