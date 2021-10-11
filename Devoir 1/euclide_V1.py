# Méthode numérique : Devoir 1.

import time

error_empty_list = ValueError("Bien essayé, mais on ne peut pas diviser par rien")

start_time = time.time()

def multiply_by(liste, multiplier):    
    
    new_list = [x*multiplier for x in liste]

    return new_list

def substract_from(list1, list2, index):
    """list1 is longer than list2"""
    
    new_list = list1
    i = 0
    for item in list2:
        new_list[index + i] -= item
        i += 1

    return new_list

def euclide(n,d):
    
    if len(d) == 0 :
        raise error_empty_list
    
    quotient = []
    
    index = 0
    div = d[0]
    
    num = list(n) # Si l'on ne fait pas list(), modifie le "numerator" sur le programme de test car c'est une deepcopy.
    
    for coeff in num:
        if num[index] != 0:
            multiplier = coeff/div
            quotient += [multiplier]
            num = substract_from(num, multiply_by(d, multiplier), index)
            index += 1
        else :
            remainder = num[index:]
            return quotient, remainder
        
# Cette partie du code a été enlevée car 4% plus longue que celle ci dessus.
# Pour 10k itérations, celle cis à mit 0.047709sec tandis que l'autre à mit 0.045942sec
#     while num[-len(d)] != 0:
#         coeff = num[index]
#         if coeff % div != 0 : break
#         multiplier = coeff//div
#         quotient += [multiplier]
#         num = substract_from(num, multiply_by(d, multiplier), index)
#         index += 1
# testé avec :
# q= [3,4,-2], d = [1,1], bonne réponse
# q = [4,7,8,7,9], d = [1,2,3], bonne réponse
# q = [8,5,-10,-3,4,-2], d = [1,1], erreur corrigée, bonne réponse

print(euclide([-27,0,36,-9,18,0,0,0,0],[-9,0,0]))
    