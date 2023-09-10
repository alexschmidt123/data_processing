import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate
# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both M
dt = 0.00001
# n is the time we repeat this loop
N = [10**7,10**5,10**3,10**2,10]
# k_on unit is M^(-1)s^(-1), k_off unit is s^(-1)
k_on = 5.25*10**6
k_off = 8*10**(-2)
R_tot = 0.5*10**(-9)
L_tot=[0.05,0.5,5,50,500]
L_tot_e=L_tot[4]
L_tot_ = L_tot_e*10**(-9)
data1 = np.zeros((N[0],))
data2 = np.zeros((N[0],))

def k_d_calculaton1(R_t,L_t,RL):
    return ((R_t-RL)*(L_t-RL)/RL)*10**(9)
def k_d_calculaton2(R_t,L_t,RL):
    return ((R_t-RL)*(L_t)/RL)*10**(9)

k_eq1=[]
k_eq2=[]
for i in range(len(L_tot)):
    L_tot_e=L_tot[i]
    L_tot_ = L_tot_e*10**(-9)
    for index in range(N[0]):
        if index == 0:
            rl1 = 0
            rl2 = 0
            data1[index]=rl1
            data2[index]=rl2
        else:
            rl1 = rl1 + (k_on*rl1**2-(k_on*(R_tot+L_tot_)+k_off)*rl1+k_on*R_tot*L_tot_)*dt
            rl2 = rl2 + (-(k_on*L_tot_+k_off)*rl2+k_on*R_tot*L_tot_)*dt
            data1[index]=rl1
            data2[index]=rl2
    k_1=k_d_calculaton1(R_tot,L_tot_,data1[-1])
    k_2=k_d_calculaton2(R_tot,L_tot_,data2[-1])
    k_eq1.append(k_1)
    k_eq2.append(k_2)
# create data
x = np.arange(len(L_tot))
width = 0.40

# plot data in grouped manner of bar type
plt.bar(x-0.2, k_eq1, width)
plt.bar(x+0.2, k_eq2, width)
plt.xticks(x, L_tot)
plt.xlabel("[L_tot](nM)")
plt.ylabel("k_d(nM)")
plt.legend(["without flowing", "with flowing"])
plt.show()


data = []
for index in range(len(L_tot)):
    data.append([L_tot[index],k_eq1[index],k_eq2[index]])
print (tabulate(data, headers=["[L_tot](nM)", "k_d without flowing(nM)", "k_d with flowing(nM)"]))

