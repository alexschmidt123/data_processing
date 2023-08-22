import math

# number is the mean of the pixel number in each hole; l1 is the scale bar length in nanometer; l2 is the scale bar length in pixel
# the output is in nanometer
def pixel2Microns(number, l1, l2):
    return number*l1/l2

print(pixel2Microns(22.39,500,102))
print(pixel2Microns(22.45,1000,144))
print(pixel2Microns(19.94,500,84))
print(pixel2Microns(17.67,1000,118))
print(pixel2Microns(57.3,200,86))
print(pixel2Microns(29.54,500,131))
print(pixel2Microns(31.97,500,132))
print(pixel2Microns(41.66,500,156))