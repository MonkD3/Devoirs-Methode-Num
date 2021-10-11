from numpy import *



def f(u,beta,gamma):
    
    dSdt = - beta * u[0] * u[1]
    dRdt =                        gamma * u[1]
    dIdt =   -dSdt - dRdt
    
    return array([dSdt,dIdt,dRdt])
 
def check(Ustart):
    if type(Ustart) == list :
        return array(Ustart)
    else :
        return Ustart
    

# -------------------------------------------------------------------------    
#
# -2- Schema de d'Euler explicite d'ordre 1
#
  
def epidemicEuler(Xstart,Xend,Ustart,n,beta,gamma):
    X, h = linspace(Xstart,Xend,n+1, retstep = True)
    Ustart = check(Ustart)
    
    U = zeros((len(X), 3))
    U[0] = Ustart
    
    for i in range(len(X) -1):
        U[i+1] = U[i] + h*f(U[i],beta,gamma)

    return X,U
 

# -------------------------------------------------------------------------    
#
# -2- Schema de Taylor classique d'ordre 4
# 
  
def epidemicTaylor(Xstart,Xend,Ustart,n,beta,gamma):
    X,h = linspace(Xstart,Xend,n+1, retstep = True)
    Ustart = check(Ustart)
    
    U = zeros((len(X), 3))
    U[0] = Ustart
    
    multiplicator = array([h, (h**2)/2, (h**3)/6, (h**4)/24])
    for i in range(len(X)-1) :
    
        s0, i0, r0 = U[i]
        s1, i1, r1 = f(U[i], beta,gamma)
        s2, r2 = -beta*(s1*i0 + i1*s0), gamma*i1
        i2 = -(s2 + r2)
        s3, r3 = -beta*(s2*i0 + 2*s1*i1 + i2*s0), gamma*i2
        i3 = -(s3+r3)
        s4, r4 = -beta*(s3*i0 + 3*s2*i1 + 3*s1*i2 + s0*i3), gamma*i3
        i4 = -(s4 + r4)
                
        U[i+1] = U[i] + (multiplicator @ array([[s1,i1,r1],[s2,i2,r2],[s3,i3,r3],[s4,i4,r4]]))

    return X,U

# -------------------------------------------------------------------------    
#
# -3- Schema de Runge-Kutta d'ordre 4
# 
  
def epidemicRungeKutta(Xstart,Xend,Ustart,n,beta,gamma):
    X,h = linspace(Xstart,Xend,n+1, retstep = True)
    Ustart = check(Ustart)
    
    U = zeros((len(X), 3))
    U[0] = Ustart
    
    for i in range(len(X)-1):
        K1 = f(U[i], beta, gamma)
        K2 = f(U[i] + (h/2)*K1,beta,gamma)
        K3 = f(U[i] + (h/2)*K2,beta,gamma) 
        K4 = f(U[i] + h*K3,beta,gamma)
        
        U[i+1] = U[i] + (h/6)*(K1 + 2*K2 + 2*K3 + K4)
    
    
    return X,U

