import numpy as np
import matplotlib.pyplot as plt
# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both M
dt = 0.001*1/60
# n is the time we repeat this loop
n = 1000
# k_on unit is M^(-1)min^(-1), k_off unit is min^(-1)
k_on = 10**7
k_off = 0.033
R_tot = 40*10**(-9)
L_tot = 30*10**(-9)
data = np.zeros((n,))
rl = 0

# def binding_rate_vs_time(rl):
#     return k_on*rl**2-(k_on*(R_tot+L_tot)+k_off)*rl+k_on*R_tot*L_tot*dt

# def recursion(num):
#     if num == 0:
#         return 0
#     else:
#         return recursion(num-1)+binding_rate_vs_time(recursion(num-1))

for index in range(n):
    if index == 0:
        rl = 0
        data[index]=rl
    else:
        rl = rl + k_on*rl**2-(k_on*(R_tot+L_tot)+k_off)*rl+k_on*R_tot*L_tot*dt
        data[index]=rl


print(data)

t = np.arange(0, n, 1) 
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("RL concentration v.s. time")
plt.plot(t, data, color="red")

plt.show()

