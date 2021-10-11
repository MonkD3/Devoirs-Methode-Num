from numpy import *


def f(u):
    
    du, dv, dw = u
    
    dudt = dv
    dvdt = dw
    dwdt = - du*dw
    
    return array([dudt, dvdt, dwdt])
    
def blasius(delta,nmax,tol,h,integrator):
    
    msg = { 0 : 'Bad initial interval :-(',
       1 :'Increase nmax : more iterations are needed :-(' ,
       2 :'Convergence observed :-)'
       }
    
    a, b = delta

    X_in_a, U_in_a = integrator(0, array([0,0,a]), 5, h, f)
    X_in_b, U_in_b = integrator(0, array([0,0,b]), 5, h, f)
    
    if (U_in_a[-1,1] - 1) * (U_in_b[-1, 1] - 1) > 0:
        return 0, msg[0]

    mid = lambda a, b : a + (b - a)/2

    val = U_in_a[-1,1] 
    iteration = 0
    delta = tol + 1
    
    while delta > tol and iteration < nmax:
        
        x = mid(a, b)
        Ustart_x = array([0,0,x])
        
        X_x, U_x = integrator(0, Ustart_x, 5, h, f)
        
        old_val = val
        val = U_x[-1,1]
        delta = abs(old_val - val)
        
        if val < 1:
            a = x
            iteration += 1
        else :
            b = x
            iteration += 1
            
    if iteration == nmax :
        return x, msg[1]
    else :
        return x,msg[2]
