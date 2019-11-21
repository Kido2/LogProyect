# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    #print (A)
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = '-'+q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

def is_atom(atom,letrasProposicionalesA,letrasProposicionalesB):
    
    if atom in letrasProposicionalesA: return True
    elif atom in letrasProposicionalesB: return True
    return False
# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    #letrasProposicionalesB = [chr(x) for x in range(256, 300)]
    letrasProposicionalesB = [chr(x) for x in range(256, 20000)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    
    L = []
    pila = []
    i = -1
    s = A[0]
    
    while len(A) > 0:
        if is_atom(s,letrasProposicionalesA,letrasProposicionalesB) and len(pila) != 0 and pila[-1] == '-':
            i += 1
            atomo = letrasProposicionalesB[i]
            #print(i)
            pila = pila[:-1]
            pila.append(atomo)
            L.append(atomo + '=-'+ s)
            A = A[1:]
            s = A[0]
            if len(A) > 0:
                s = A[0]
                
                
        elif s == ')':
            w = pila[-1]
            O = pila[-2]
            v = pila[-3]
            #assert w != '(' and O != '(' and v != '(', 'Wrong Tseitin'
            #assert w != ')' and O != ')' and v != ')', 'Wrong Tseitin'
            pila = pila[:len(pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + '=' '('+ v + O + w + ')')
            #print (atomo + '=' '('+ v + O + w + ')')
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    
    B = ''
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
        
    for x in L:
        y = enFNC(x)
        B += 'Y' + y
    
    B = atomo + B
    return B

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == 'O':
            C = C[1:]
        elif s == '-':
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L
    #return C.split('O')

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    '''
    returnList = []
    for string in A.split('Y'):
        returnList.append(Clausula(string))
        
    return returnList
    '''
    #'''
    L = []
    i = 0
    while len(A) > 0: 
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                L.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i +=1
    
    return L
    #'''

# Test enFNC()
# Descomente el siguiente código y corra el presente archivo
#formula = "p=(qYr)"
#formula = 'p=-q'
#print(formaClausal(enFNC(formula))) # Debe obtener qO-pYrO-pY-qO-rOp

# Test Tseitin()
# Descomente el siguiente código y corra el presente archivo
#formula = "(pY-q)"
#letricas = ['p','q']
#print (Tseitin(formula,letricas))
#print(formaClausal(Tseitin(formula,letricas))) # Debe obtener AYpO-AYqO-AY-pO-qOA (la A tiene una raya encima)
#print (formaClausal('AYpO-AYqO-AY-pO-qOA'))


# Test Clausula()
# Descomente el siguiente código y corra el presente archivo
#c = "pO-qOr"
#print(Clausula(c)) # Debe obtener ['p', '-q', 'r']

# Test formaClausal()
# Descomente el siguiente código y corra el presente archivo
#f = "pO-qOrY-sOt"
#print(formaClausal(f)) # Debe obtener [['p', '-q', 'r'], ['-s', 't']]
