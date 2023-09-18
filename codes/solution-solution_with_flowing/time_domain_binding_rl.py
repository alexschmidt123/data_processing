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
L_tot_e=L_tot[4]
L_tot_ = L_tot_e*10**(-9)
A1 = k_on*R_tot*L_tot_
B1 = k_on*(R_tot+L_tot_)+k_off
B2 = k_on*L_tot_+k_off
data1 = np.zeros((N[0],))
data2 = np.zeros((N[0],))
diff = np.zeros(N[0],)


def binding_product_no_flowing(R_t,L_t,Kd):
    A = R_t+L_t+Kd
    B = R_t*L_t 
    return (A-math.sqrt(A**2-4*B))/2

def binding_product_flowing(R_t,L_t,k_on,k_off):
    A = k_on*L_t+ k_off
    B = k_on*R_t*L_t
    return B/A

def k_d_calculaton(R_t,L_t,RL):
    return (R_t-RL)*(L_t-RL)/RL

for index in range(N[0]):
    if index == 0:
        rl1 = 0
        rl2 = 0
        data1[index]=rl1
        data2[index]=rl2
    else:
        rl1 = rl1 + (k_on*rl1**2-B1*rl1+A1)*dt
        rl2 = rl2 + (-B2*rl2+A1)*dt
        data1[index]=rl1
        data2[index]=rl2
        diff[index] = rl1-rl2
print(diff)
Eq1=binding_product_no_flowing(R_tot,L_tot_,k_off/k_on)
Eq2=binding_product_flowing(R_tot,L_tot_,k_on,k_off)
for i in range(len(N)):
    plt.subplot(2,3, i+1)
    plt.tight_layout(pad=0.5)
    t = np.arange(0,N[i],1)
    data_1=data1[0:N[i]:1]
    data_2=data2[0:N[i]:1]
    plt.xlabel("Time(*0.00001s)")
    plt.ylabel("[RL](M)")
    if i ==0:
        plt.axhline(y=Eq1,color="green",linestyle='dashed')
        plt.axhline(y=Eq2,color="blue",linestyle='dashed')
    plt.plot(t, data_1, color="green")
    plt.plot(t, data_2,color="blue")
    plt.ticklabel_format(useOffset=False)
    plt.legend(['no flowing', 'with flowing'])
k_1=k_d_calculaton(R_tot,L_tot_e,data1[-1])
k_2=k_d_calculaton(R_tot,L_tot_e,data2[-1])
k_eq=[k_1,k_2]
print(k_eq)
plt.suptitle("[RL] v.s. t Plot, when [L_tot]=%s nM" %(L_tot_e),style="italic",fontsize=15)
plt.tight_layout(pad=0.5)
plt.show()


