from numpy import *
def booleEasy(f,a,b,n):
    
    h = (b-a)/(n*4)

    pas = 4*h
    ab_max = b + h
    
    ab_1 = arange(a, ab_max, pas)[0:n]
    ab_2 = arange(a + pas, ab_max, pas)[0:n]
    ab_3 = arange(a + h, ab_max, pas)[0:n]
    ab_4 = arange(a + 3*h, ab_max, pas)[0:n]
    ab_5 = arange(a + 2*h, ab_max, pas)[0:n]
     
    I_n = (7*(f(ab_1) + f(ab_2)) + 32*(f(ab_3)+f(ab_4))+ 12*f(ab_5))
    return ((2*h)/45)*sum(I_n)
  
def booleFun(f,a,b,n,nmax,tol):
    
    iteration = int(n)
    
    I_n = booleEasy(f,a,b,iteration)
    I_2n = booleEasy(f,a,b,2*iteration)
    
    errorEst = abs(I_2n - I_n)
    
    while 2*iteration <= nmax and errorEst >= tol :
        
        iteration *= 2
        
        I_n = I_2n
        I_2n = booleEasy(f,a,b,2*iteration)
        
        errorEst = abs(I_2n - I_n)
    
    return I_2n,iteration,errorEst 