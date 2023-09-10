import numpy as np
import matplotlib.pyplot as plt
import math
# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both M
dt = 0.001
# n is the time we repeat this loop
N = [10**6,10**4,10**2,10]
# k_on unit is M^(-1)s^(-1), k_off unit is s^(-1)
S=5*10**(-5)
V=4*10**(-8)
k_on = 32.9
k_off = 2.9*10**(-4)
R_tot = 2.069*10**(-8)
L_tot=[0.02586,0.2586,2.586,25.86,258.6]
L_tot_e=L_tot[4]
L_tot1 = L_tot_e*10**(-5)
C = k_on*S/V
A1 = k_on*R_tot*L_tot1
B1 = k_on*(R_tot*S/V+L_tot1)+k_off
data1 = np.zeros((N[0],))

for index in range(N[0]):
    if index == 0:
        rl1 = 0
        data1[index]=L_tot1-rl1*S/V
    else:
        rl1 = rl1 + (C*rl1**2-B1*rl1+A1)*dt
        data1[index]=L_tot1-rl1*S/V
for i in range(len(N)):
    plt.subplot(2,2, i+1)
    plt.tight_layout(pad=0.5)
    t = np.arange(0,N[i],1)
    data=data1[0:N[i]:1]
    print(data)
    plt.xlabel("Time(*0.001s)")
    plt.ylabel("[L](mol/m^3)")
    plt.plot(t, data)
    plt.ticklabel_format(useOffset=False)
plt.suptitle("[L] v.s. t Plot, when [L_tot]=%s*10^(-5) mol/m^3" %(L_tot_e),style="italic",fontsize=15)
plt.tight_layout(pad=0.5)
plt.show()


