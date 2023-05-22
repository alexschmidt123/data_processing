#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

x_data = np.array([ 20,16,8,6,4,1,0 ])
y_data = np.array([ 179,126,122,117,73,55,44])

def model_f(x,F,R,K):
    return 40+(F-40)*(R+K+x-math.sqrt((R+K+x)^2-4*R*x))/(2*R)

popt, pcov = curve_fit(model_f, x_data, y_data, p0=[179,1,1])
# a_opt, b_opt, c_opt = popt
# x_model = np.linspace(min(x_data), max(y_data), 100)
# y_model = fit_f(x_model, a_opt, b_opt, c_opt) 
# plt.scatter(x_data, y_data)
# plt.plot(x_model, y_model, color='r')
# plt.xlabel("IgG Concentration (10^-7 M)")
# plt.ylabel("Fluorescence Intensity (a.u.)")
# plt.show()
print(pop)