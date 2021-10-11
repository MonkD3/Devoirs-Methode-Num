from numpy import *


def stabilityGear(x,y,order):
    
    z = x + 1j*y
    
    coef = { 1 : array([1,1]),
            2 : array([2/3,4/3,-1/3]),
            3 : array([6/11,18/11,-9/11,2/11]),
            4 : array([12/25,48/25,-36/25,16/25,-3/25]),
            5 : array([60/137,300/137,-300/137,200/137,-75/137,12/137]),
            6 : array([60/147,360/147,-450/147,400/147,-225/147,72/147,-10/147])
            }
    
    coeff = coef[order]    
    gain = zeros_like(z)    
    for i in range(len(z)):
        for j in range(len(z[i])):
            gain[i,j] = max(abs(roots([coeff[0]*z[i,j] - 1, *coeff[1:]])))
            
    # gain = array([[max(abs(roots([coeff[0]*z[i,j] - 1, *coeff[1:]]))) for j in range(len(z[i]))] for i in range(len(z))])
    
    return abs(gain),coeff
