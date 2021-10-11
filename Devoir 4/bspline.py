from numpy import *

# def b(t,T,i,p):
# 
#     if p == 0:
#         return (T[i] <= t)*(t < T[i+1])
#     
#     else:
#         u  = 0.0 if T[i+p ]  == T[i]   else (t-T[i])/(T[i+p]- T[i]) * b(t,T,i,p-1)
#         u += 0.0 if T[i+p+1] == T[i+1] else (T[i+p+1]-t)/(T[i+p+1]-T[i+1]) * b(t,T,i+1,p-1)
#         return u

def b(t,T,i,p):
    
    if p == 0 :
        return (T[i] <= t)*(t < T[i+1])
    else:
        u = 0 if T[i+p ]  == T[i] else S(i,p,t,T)*b(t,T,i,p-1) 
        u += 0 if T[i+p+1] == T[i+1] else (1 - S(i+1,p,t,T))*b(t,T,i+1,p-1)
        return u
        
def S(i,p,t,T):
    
    s = (t - T[i])/(T[i+p] - T[i]) if T[i] < T[i+p] else 0
    return s
    
def bspline(X,Y,t):
    
    # Permet de répéter les trois premiers points de contrôles pour avoir une courbe fermée
    X_c = append(X, X[0:3])
    Y_c = append(Y, Y[0:3])

    
    p = 3 # DEGRE
    m = min(len(X_c),len(Y_c)) # Nombre de points de contrôles
    n = m + p # Nombre de noeuds
    k = [x for x in range(0,m)] # = n-p-1
    
    T = arange(-p,m+4,1) # Noeuds
    
    x = array([b(t,T,i,p) for i in k]).T
    
    x_sol = x @ X_c
    y_sol = x @ Y_c

    return x_sol,y_sol