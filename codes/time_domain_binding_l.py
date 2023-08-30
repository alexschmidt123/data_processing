import numpy as np
import matplotlib.pyplot as plt
import math
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
L_tot_e=L_tot[0]
L_tot1 = L_tot_e*10**(-9)
A1 = k_on*R_tot*L_tot1
B1 = k_on*(R_tot+L_tot1)+k_off
data1 = np.zeros((N[0],))

for index in range(N[0]):
    if index == 0:
        
        rl1 = 0
        data1[index]=L_tot1-rl1
    else:
        rl1 = rl1 + (k_on*rl1**2-B1*rl1+A1)*dt
        data1[index]=L_tot1-rl1
for i in range(len(N)):
    plt.subplot(2,3, i+1)
    plt.tight_layout(pad=0.5)
    t = np.arange(0,N[i],1)
    data=data1[0:N[i]:1]
    print(data)
    plt.xlabel("Time(*0.0001s)")
    plt.ylabel("[L](M)")
    plt.plot(t, data)
plt.suptitle("[L] v.s. t Plot, when [L_tot]=%s nM" %(L_tot_e),style="italic",fontsize=15)
plt.tight_layout(pad=0.5)
plt.show()


