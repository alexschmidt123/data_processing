import numpy as np
import math
from matplotlib import pyplot as plt
k_on = 2.7*10**5
k_off = 1.4*10**(-4)
L_tot_=[13.89, 27.78, 55.56, 138.89, 277.78]
time = [1000,100,10,1]
t_max=time[0]
color=['purple','blue','orange','green','red']
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.xlabel('Time (s)')
plt.ylabel('RL fraction (%)')
plt.suptitle("f_RL v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
for index in range(len(L_tot_)):
    L_tot = L_tot_[index]*10**(-9)
    B = k_on*L_tot+k_off
    t = np.linspace(0, t_max, 300)
    y = (1-np.exp(-B*t))*k_on*L_tot/B
    plt.plot(t, y, color=color[index])
    t1=L_tot_[index]/0.06849
    t2=(math.log(2))/B
    print("Ligand Concentration: %i ug/ml, Reaction's Half life: %i seconds" %(t1,t2))
plt.legend(['ligand:0.5 ug/ml','ligand:1 ug/ml','ligand:2 ug/ml','ligand:5 ug/ml','ligand:10 ug/ml'])
plt.show()