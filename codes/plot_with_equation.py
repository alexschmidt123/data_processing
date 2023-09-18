import numpy as np
from matplotlib import pyplot as plt

# k_on = 32.9
# k_off = 2.9*10**(-4)
# R_tot = 2.069*10**(-8)
# L_tot_=[0.02586,0.2586,2.586,25.86,258.6]
# time = [10**5,10**3,10,0.1,0.01]
# t_max=time[4]
# color=['red','orange','green','blue','purple']
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.xlabel('Time (second)')
# plt.ylabel('RL density (mol/m^2)')
# plt.suptitle("[RL] v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
# for index in range(len(L_tot_)):
#     L_tot = L_tot_[index]*10**(-5)
#     A = k_on*R_tot*L_tot
#     B = k_on*L_tot+k_off
#     t = np.linspace(0, t_max, 300)
#     y = A/B*(1-np.exp(-B*t))
#     plt.plot(t, y, color=color[index])
# plt.show()

# k_on = 32.9
# k_off = 2.9*10**(-4)
# R_tot = 2.069*10**(-8)
# L_tot_=[0.02586,0.2586,2.586,25.86,258.6]
# time = [10**5,10**3,10,0.1,0.01]
# t_max=time[4]
# color=['red','orange','green','blue','purple']
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.xlabel('Time (second)')
# plt.ylabel('R density (mol/m^2)')
# plt.suptitle("[R] v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
# for index in range(len(L_tot_)):
#     L_tot = L_tot_[index]*10**(-5)
#     A = k_on*R_tot*L_tot
#     B = k_on*L_tot+k_off
#     t = np.linspace(0, t_max, 300)
#     y = R_tot-A/B*(1-np.exp(-B*t))
#     plt.plot(t, y, color=color[index])
# plt.show()

k_on = 32.9
k_off = 2.9*10**(-4)
R_tot = 2.069*10**(-8)
L_tot_=[0.02586,0.2586,2.586,25.86,258.6]
time = [10**5,10**3,10,0.1,0.01]
t_max=time[0]
for index in range(len(L_tot_)):
    L_tot = L_tot_[index]*10**(-5)
    A = k_on*R_tot*L_tot
    B = k_on*L_tot+k_off
    y = A/B*(1-np.exp(-B*t_max))
    print((R_tot-y)*L_tot/y)