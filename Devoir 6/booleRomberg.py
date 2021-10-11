from numpy import *

def boole(U,h,n):
  return (32*sum(U[1:4*n:2]) + 12*sum(U[2:4*n:4]) + 
          14*sum(U[4:4*n:4]) + 7*U[0] + 7*U[-1] )* (2*h/45)


def booleRomberg(f,a,b,n,nmax,tol):
    
    error = tol+1
    X,h = linspace(a,b,4*n+1,retstep=True); U = f(X)
    I = boole(U,h,n)
    
    taille = int(ceil(log(nmax/n)/log(2)))
    rom = zeros((taille, taille))
    rom[0,0] = I
    
    i,j = 1,0
    
    while (error > tol and n*2 < nmax):
        
        calc = lambda i, j : (2**(2*(j+2))*rom[i,j-1] - rom[i-1,j-1])/(2**(2*(j+2)) - 1)
        
        if i == j :
            if i != 0:
                rom[i,j] = calc(i,j)
                
            i += 1
            j = 0
            error = abs(rom[i-1,i-1] - rom[i-1,i-2])
            
        elif j == 0:
            X,h = linspace(a,b,(4*(n*(2**i)))+1,retstep=True); U = f(X)
            rom[i,j] = boole(U,h,n*(2**i))
            j += 1
            
        elif i >= j + 1 :
            rom[i,j] = calc(i,j)
            j += 1
    
    return rom[i-1,i-1],n*2**(i-1),error
