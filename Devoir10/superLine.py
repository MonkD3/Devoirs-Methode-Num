from numpy import *
from numpy.linalg import solve,norm
 
#
# -1- Droite au sens de moindres carrés usuels
# 
  
def superLineInitialGuest(X,U):
    
    A = array([power(X,i) for i in range(2)]).T
    b,a = solve(A.T@A, A.T@U)
    
    return array([a,b])
  
  
#
# -------------------------------------------------------------------------
#
# -2- Iteration de Newton-Raphson pour obtenir
#     les coefficients d'une droite minimisant la "vraie distance" entre 
#     les données et la droite  
# 
 

def superLineIterate(X,U,alpha):
    
    a,b = alpha
    
    # Variables intermédiaires :
    z = 1 + a*a
    y = z*z
    dist = U - a*X - b

    # Dérivées partielles premières :
    part_a = -(2*a/y)*(dist@dist) - (2/z)*(dist@X)
    part_b = -(2/z)*sum(dist)
     
    gradient = array([part_a, part_b])

    # Dérivées partielles secondes :
    part_a_a = ((-2*z + 8*a*a)/(y*z))*(dist@dist) + (4*a/y)*(X@dist) + (4*a/y)*sum(dist) + (2/z)*(X@X)
    part_a_b = (4*a/y)*sum(dist) + (2/z)*sum(X)
    part_b_b = (2/z)*len(X)

    hessienne = array([[part_a_a, part_a_b],[part_a_b, part_b_b]])
    
    dalpha = solve(hessienne, -gradient)
    
    return dalpha
  

