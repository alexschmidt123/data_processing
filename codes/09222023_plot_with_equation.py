import numpy as np
import math
from matplotlib import pyplot as plt

# k_on = 4.18*10**5/60
# k_off = 1.75*10**(-3)/60
# L_tot_=[0.6849,2.0548,3.4246,5.4794,6.8493]
# time = [2000,200,20,2]
# t_max=time[0]
# color=['purple','blue','orange','green','red']
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.xlabel('Time (s)')
# plt.ylabel('RL fraction (%)')
# plt.suptitle("f_RL v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
# for index in range(len(L_tot_)):
#     L_tot = L_tot_[index]*10**(-7)
#     B = k_on*L_tot+k_off
#     t = np.linspace(0, t_max, 300)
#     y = 1-np.exp(-B*t)
#     plt.plot(t, y, color=color[index])
#     t1=L_tot_[index]/0.06849
#     t2=(math.log(2))/B
#     print("Ligand Concentration: %i ug/ml, Reaction's Half life: %i seconds" %(t1,t2))
# # plt.legend(['ligand:10ug/ml','ligand:30ug/ml','ligand:50ug/ml','ligand:80ug/ml','ligand:100ug/ml'])
# plt.show()


# t=np.linspace(40, 70, 300)
# R= 69-64*np.exp(12.3-0.31*t)
# plt.plot(t, R)
# plt.show()



# k_on = 0.997*10**4/60
# k_off = 7.56*10**(-5)/60
# L_tot_=[1.654]
# time = [4000,400,40,4]
# t_max=time[3]
# color=['red','blue','orange','green','red']
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.xlabel('Time (s)')
# plt.ylabel('RL fraction (%)')
# plt.suptitle("f_RL v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
# for index in range(len(L_tot_)):
#     L_tot = L_tot_[index]*10**(-5)
#     B = k_on*L_tot+k_off
#     t = np.linspace(0, t_max, 300)
#     y = 1-np.exp(-B*t)
#     plt.plot(t, y, color=color[index])
# # plt.legend(['ligand:10ug/ml','ligand:30ug/ml','ligand:50ug/ml','ligand:80ug/ml','ligand:100ug/ml'])
# plt.show()


# k_on = 0.6917*10**4/60
# k_off = 6.62*10**(-5)/60
# L_tot_=[1.786]
# time = [4000,400,40,4]
# t_max=time[3]
# color=['red','blue','orange','green','red']
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# plt.xlabel('Time (s)')
# plt.ylabel('RL fraction (%)')
# plt.suptitle("f_RL v.s. t Plot, based on function, with flowing",style="italic",fontsize=15)
# for index in range(len(L_tot_)):
#     L_tot = L_tot_[index]*10**(-5)
#     B = k_on*L_tot+k_off
#     t = np.linspace(0, t_max, 300)
#     y = 1-np.exp(-B*t)
#     plt.plot(t, y, color=color[index])
# # plt.legend(['ligand:10ug/ml','ligand:30ug/ml','ligand:50ug/ml','ligand:80ug/ml','ligand:100ug/ml'])
# plt.show()
k_on1 = 0.997*10**4/60
k_off1 = 7.56*10**(-5)/60
L_tot1=1.654*10**(-5)
k_on2 = 0.6917*10**4/60
k_off2 = 6.62*10**(-5)/60
L_tot2=1.786*10**(-5)
B1 = k_on1*L_tot1+k_off1
B2 = k_on2*L_tot2+k_off2
t1=(math.log(2))/B1
t2=(math.log(2))/B2
print(t1,t2)