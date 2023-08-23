# temperature is 25°C
# time unit is minute, R_tot and L_tot's concentration unit are both M
dt = 0.1*1/60
n = 20000
# k_on unit is M^(-1)min^(-1), k_off unit is min^(-1)
k_on = 10**7
k_off = 0.033
R_tot = 30*10**(-9)
L_tot = 30*10**(-9)

def binding_rate_vs_time(rl):
    return k_on*rl**2-(k_on*(R_tot+L_tot)+k_off)*rl+k_on*R_tot*L_tot*dt

def recursion(num):
    if num == 0:
        return 0
    else:
        return recursion(num-1)+binding_rate_vs_time(recursion(num-1))

data=[]
for index in range(n):
    data.append([index,recursion(index)])
