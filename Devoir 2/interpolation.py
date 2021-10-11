# Méthodes numériques : devoir 2
#
# Autheur : Nathan Tihon, noma : 1085-1900

from numpy import *
from numpy.linalg import solve
import time

my_error = ValueError("""Il m'est impossible de calculer l'interpolation respectueuse de l'environnement car vous n'avez pas respecté l'environnement.
                         PS : soit la longueur du tableau n'est pas correcte soit il y a l'origine quelque part :)""")

def interpolation(X,U,x):
    start_time = time.time()
    length_X = len(X)
    
    if length_X % 2 == 0 :
        raise my_error
    if 0 in list(X) or 0 in list(x):
        raise my_error

    n = (length_X - 1)//2
    
    A = mat(array([X**i for i in range(-n,n+1)]).T)
    coeff = solve(A, U.T)
    
    abscisses = mat(array([x**i for i in range(-n, n + 1)]).T)
    u = (abscisses @ coeff).transpose()
    
    print("Time executed :", time.time() - start_time)
    return(u.real) 
