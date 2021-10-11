# Méthode numérique : Devoir 1.
#
# Auteur : Tihon Nathan, noma : 1085-1900

error_empty_list = ValueError("Bien essayé, mais on ne peut pas diviser par rien")

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
    max_len = len(n) - len(d)
    
    while index <= max_len :
        coeff = num[index]
        multiplier = coeff/div
        quotient.append(multiplier)
        num = substract_from(num, [x*multiplier for x in d], index)
        index += 1
        
    remainder = num[index:]
    
    # Afin d'éliminer les 0 indésirés
    
#     while len(remainder) != 0 and remainder[0] == 0.0:
#         del remainder[0]
        
    return quotient, remainder

# testé avec :
# q = [3,4,-2], d = [1,1], bonne réponse
# q = [4,7,8,7,9], d = [1,2,3], bonne réponse
# q = [8,5,-10,-3,4,-2], d = [1,1], erreur corrigée, bonne réponse
# q = [-27,0,36,-9,18,0,0,0,0], d = [-9,0,0], erreur corrigée, bonne réponse
print(euclide([1,-3,0,4],[1,1]))