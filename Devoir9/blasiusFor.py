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
    x = zeros(nmax)

    a, b = delta

    X_in_a, U_in_a = integrator(0, array([0,0,a]), 5, h, f)
    X_in_b, U_in_b = integrator(0, array([0,0,b]), 5, h, f)
    
    if (U_in_a[-1,2]) * (U_in_b[-1, 2]) > 0:
        return 0, msg[0]

    mid = lambda a, b : a + (b - a)/2
    
    for i in range(len(x)):
        
        x[i] = mid(a, b)
        Ustart_x = array([0,0,x[i]])
        
        X_x, U_x = integrator(0, Ustart_x, 5, h, f)
        
        Uxold = Ux
        Ux = U_x[-1,1]
        
        if abs(Ux - 1) <= tol :
            return x[i],msg[2]
        
        elif Uxold * Ux > 0 :
            a = x[i]
        else :
            b = x[i]
    
    return x[-1],msg[1]
