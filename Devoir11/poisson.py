# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 11
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# VOUS POUVEZ IMPORTER TOUS LES PACKAGES PRESENTS SUR LE SERVEUR
from numpy import *
from numpy.linalg import solve
from scipy.sparse.linalg import spsolve
import scipy.sparse as sparse
#
# A MODIFIER
#     - pour modifier le demaine de calcul en retirant
#       le coin supérieur droit
#     - pour tirer profit du caractère creux de la matrice
#
#
def poissonSolve(nCut):
    n = 2*nCut + 1; m = n*n; h = 2/(n-1) 
  
    B = zeros(m)  
    A = sparse.dok_matrix(sparse.eye(m),dtype=float32)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if i > nCut or j < nCut :
                index = i + j*n
                A[index,index] = 4
                A[index,index-1] = -1
                A[index,index+1] = -1
                A[index,index+n] = -1
                A[index,index-n] = -1
                B[index] = 1 
                
    return spsolve((A/(h*h)).tocsr(),B).reshape(n,n)