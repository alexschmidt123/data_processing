import numpy as np
import matplotlib.pyplot as plt
import math
# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both mol/m^3
dt = 0.001
# n is the time we repeat this loop
N = [10**6,10**4,10**2,10]
n = N[3]
# k_on unit is m^3mol^(-1)s^(-1), k_off unit is s^(-1)
S=5*10**(-5)
V=4*10**(-8)
k_on = 32.9
k_off = 2.9*10**(-4)
R_tot = 2.069*10**(-8)

L_tot1 = 0.02586*10**(-5)
L_tot2 = 0.2586*10**(-5)
L_tot3 = 2.586*10**(-5)
L_tot4 = 25.86*10**(-5)
L_tot5 = 258.6*10**(-5)
C = k_on*S/V
A1 = k_on*R_tot*L_tot1
A2 = k_on*R_tot*L_tot2
A3 = k_on*R_tot*L_tot3
A4 = k_on*R_tot*L_tot4
A5 = k_on*R_tot*L_tot5
B1 = k_on*(R_tot*S/V+L_tot1)+k_off
B2 = k_on*(R_tot*S/V+L_tot2)+k_off
B3 = k_on*(R_tot*S/V+L_tot3)+k_off
B4 = k_on*(R_tot*S/V+L_tot4)+k_off
B5 = k_on*(R_tot*S/V+L_tot5)+k_off
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
    if index == 0:
        rl1 = 0
        rl2 = 0
        rl3 = 0
        rl4 = 0
        rl5 = 0
        data1[index]=R_tot-rl1
        data2[index]=R_tot-rl2
        data3[index]=R_tot-rl3
        data4[index]=R_tot-rl4
        data5[index]=R_tot-rl5
    else:
        rl1 = rl1 + (C*rl1**2-B1*rl1+A1)*dt
        rl2 = rl2 + (C*rl2**2-B2*rl2+A2)*dt
        rl3 = rl3 + (C*rl3**2-B3*rl3+A3)*dt
        rl4 = rl4 + (C*rl4**2-B4*rl4+A4)*dt
        rl5 = rl5 + (C*rl5**2-B5*rl5+A5)*dt
        data1[index]=R_tot-rl1
        data2[index]=R_tot-rl2
        data3[index]=R_tot-rl3
        data4[index]=R_tot-rl4
        data5[index]=R_tot-rl5



t = np.arange(0, n, 1) 
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("R surface concentration(mol/m^2) v.s. T (0.001s)")
plt.plot(t, data1, color="red")
plt.plot(t, data2, color="orange")
plt.plot(t, data3, color="green")
plt.plot(t, data4, color="blue")
plt.plot(t, data5, color="purple")
# plt.legend(['[C_L_tot]=0.03375*10^(-5)mol/m^3', '[C_L_tot]=0.3375*10^(-5)mol/m^3','[C_L_tot]=3.375*10^(-5)mol/m^3','[C_L_tot]=33.75*10^(-5)mol/m^3','[C_L_tot]=337.5*10^(-5)mol/m^3'])
plt.show()