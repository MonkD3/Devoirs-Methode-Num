# Méthode numériques : Devoir 3
#
# Autheur : Nathan Tihon, noma : 1085-1900


from numpy import *
from numpy.linalg import solve

def approximation(X,Y,U,x,y) :
    """ Fonction d'approximation biquadratique.
    Params :
        X : Abscisses des points à approximer (tableau)
        Y : Ordonnée des points à approximer (tableau)
        U : Côt des points à approximer (tableau)
            Les trois tableaux ci-dessus ont les mêmes dimensions
            
        x : Abscisses des points à rendre (tableau)
        y : Ordonnée des points à rendre (tableau)
            Les deux tableaux ci-dessus ont les mêmes dimensions
    Returns :
        a : Coefficient des fonctions de bases (tableau de taille 9)
        uh : Côte (valeur) des points d'abscisses x et d'ordonnée y (tableau de même dimension que x et y)
    """
    
    # Exemple de dico de fonctions :
#     phi = lambda id,x : {
#         0 : lambda x: x*(1+x)/2,
#         1 : lambda x: -x*(1-x)/2,
#         2 : lambda x: (1-x)*(1+x)  
#         }[id](x)
    
    # Définition du dictionnaire des fonctions de bases
    
#     biquad = {}
#     biquad["Phi_0"] = lambda x,y : x*(1+ x)*y*(1 + y)/4
#     biquad["Phi_1"] = lambda x,y : -x*(1-x)*y*(1+y)/4
#     biquad["Phi_2"] = lambda x,y : x*(1-x)*y*(1-y)/4
#     biquad["Phi_3"] = lambda x,y : -x*(1+x)*y*(1-y)/4
#     biquad["Phi_4"] = lambda x,y : (1+x)*(1-x)*y*(1+y)/2
#     biquad["Phi_5"] = lambda x,y : -x*(1 - x)*(1 - y)*(1 + y)/2
#     biquad["Phi_6"] = lambda x,y : -(1 - x)*(1 + x)*y*(1 - y)/2
#     biquad["Phi_7"] = lambda x,y : x*(1 + x)*(1 - y)*(1 + y)/2
#     biquad["Phi_8"] = lambda x,y : (1 - x)*(1 + x)*(1 - y)*(1 + y)

    # Autre manière (peut être plus élégante)
# 
#     phi = lambda id,x,y : { 0 : lambda x,y : x*(1+ x)*y*(1 + y)/4,
#                             1 : lambda x,y : -x*(1-x)*y*(1+y)/4,
#                             2 : lambda x,y : x*(1-x)*y*(1-y)/4,
#                             3 : lambda x,y : -x*(1+x)*y*(1-y)/4,
#                             4 : lambda x,y : (1+x)*(1-x)*y*(1+y)/2,
#                             5 : lambda x,y : -x*(1 - x)*(1 - y)*(1 + y)/2,
#                             6 : lambda x,y : -(1 - x)*(1 + x)*y*(1 - y)/2,
#                             7 : lambda x,y : x*(1 + x)*(1 - y)*(1 + y)/2,
#                             8 : lambda x,y : (1 - x)*(1 + x)*(1 - y)*(1 + y)
#                             }[id](x,y)
# 
#     Vandermonde = ones((9, len(X)))
#     
#     for j in range(9):
#         # Vandermonde[j,:] = biquad["Phi_{}".format(j)](X,Y)
#         Vandermonde[j,:] = phi(j,X,Y)
# 
#     Approx = Vandermonde @ Vandermonde.T
#     
#     b = Vandermonde @ U
#     coeff = solve(Approx, b)
#     print(coeff)
# 
#     uh = zeros((len(x), len(y)))
# 
#     for i in range(9):
# #         uh += coeff[i]*biquad["Phi_{}".format(i)](x,y)
#         uh += coeff[i]*phi(i,x,y)
#         


    # Test encore autre manière, peut être plus efficace :
    phi_0 =lambda x,y : x*(1+ x)*y*(1 + y)/4
    phi_1 =lambda x,y : -x*(1-x)*y*(1+y)/4
    phi_2 =lambda x,y : x*(1-x)*y*(1-y)/4
    phi_3 =lambda x,y : -x*(1+x)*y*(1-y)/4
    phi_4 =lambda x,y : (1+x)*(1-x)*y*(1+y)/2
    phi_5 =lambda x,y : -x*(1 - x)*(1 - y)*(1 + y)/2
    phi_6 =lambda x,y : -(1 - x)*(1 + x)*y*(1 - y)/2
    phi_7 =lambda x,y : x*(1 + x)*(1 - y)*(1 + y)/2
    phi_8 =lambda x,y : (1 - x)*(1 + x)*(1 - y)*(1 + y)
    
    phi = lambda x,y : array([phi_0(x,y),phi_1(x,y),phi_2(x,y),phi_3(x,y),phi_4(x,y),phi_5(x,y),phi_6(x,y),phi_7(x,y),phi_8(x,y)])
        
    Vandermonde = phi(X,Y)
            
    Approx = Vandermonde @ Vandermonde.T
    
    b = Vandermonde @ U
    coeff = solve(Approx, b)
    
    uh =  phi(y,x).T @ coeff

    return coeff, uh
