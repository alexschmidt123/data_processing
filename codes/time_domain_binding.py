import numpy as np
import matplotlib.pyplot as plt
import math
# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both M
dt = 0.00001
# n is the time we repeat this loop
n = 10000000
# k_on unit is M^(-1)s^(-1), k_off unit is s^(-1)
k_on = 5.25*10**6
k_off = 8*10**(-2)
R_tot = 0.5*10**(-9)

L_tot1 = 0.05*10**(-9)
L_tot2 = 0.5*10**(-9)
L_tot3 = 5*10**(-9)
L_tot4 = 50*10**(-9)
L_tot5 = 500*10**(-9)
A1 = k_on*R_tot*L_tot1
A2 = k_on*R_tot*L_tot2
A3 = k_on*R_tot*L_tot3
A4 = k_on*R_tot*L_tot4
A5 = k_on*R_tot*L_tot5
B1 = k_on*(R_tot+L_tot1)+k_off
B2 = k_on*(R_tot+L_tot2)+k_off
B3 = k_on*(R_tot+L_tot3)+k_off
B4 = k_on*(R_tot+L_tot4)+k_off
B5 = k_on*(R_tot+L_tot5)+k_off
data1 = np.zeros((n,))
data2 = np.zeros((n,))
data3 = np.zeros((n,))
data4 = np.zeros((n,))
data5 = np.zeros((n,))

# def binding_rate_vs_time(rl):
#     return k_on*rl**2-(k_on*(R_tot+L_tot)+k_off)*rl+k_on*R_tot*L_tot*dt

# def recursion(num):
#     if num == 0:
#         return 0
#     else:
#         return recursion(num-1)+binding_rate_vs_time(recursion(num-1))

for index in range(n):
    data2[index]=A2/B2*(1-math.exp(-B2*index*dt))
    if index == 0:
        
        rl1 = 0
        rl2 = 0
        rl3 = 0
        rl4 = 0
        rl5 = 0
        data1[index]=rl1
        data2[index]=rl2
        data3[index]=rl3
        data4[index]=rl4
        data5[index]=rl5
    else:
        rl1 = rl1 + (k_on*rl1**2-B1*rl1+A1)*dt
        rl2 = rl2 + (k_on*rl2**2-B2*rl2+A2)*dt
        rl3 = rl3 + (k_on*rl3**2-B3*rl3+A3)*dt
        rl4 = rl4 + (k_on*rl4**2-B4*rl4+A4)*dt
        rl5 = rl5 + (k_on*rl5**2-B5*rl5+A5)*dt
        data1[index]=rl1
        data2[index]=rl2
        data3[index]=rl3
        data4[index]=rl4
        data5[index]=rl5



t = np.arange(0, n, 1) 
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("RL concentration (M) v.s. time (0.00001s)")
plt.plot(t, data1, color="green")
plt.plot(t, data2, color="blue")
plt.plot(t, data3, color="yellow")
plt.plot(t, data4, color="purple")
plt.plot(t, data5, color="orange")
plt.legend(['0.05nM', '0.5nM','5nM','50nM','500nM'])
plt.show()

