from copy import deepcopy
#import pdb
def has_singleatom(A):
    
    for sublist in A:
        if len(sublist) == 1: return True
        
    return False

def has_empty(A):
    for sublist in A:
        if len(sublist) == 0: return True
    return False

def complement(atom): #only receive atoms and negation of them, -A or A
    if atom[0] == '-': return atom[1]
    else: return '-' + atom

def is_negation(atom):
    if atom[0] == '-': return True
    else: return False

def unitPropagate(A,partial):
    #pdb.set_trace()
    while has_singleatom(A):
        for sublist in A:
            if len(sublist) == 1: #Is the single
                pureatom = sublist[0]                
                suppose(pureatom,A,partial) #Suppose it is true and just spread it
                #and remove it from A
                

def find_unassigned(wholelist,I):
    '''Finds unassigned letter '''
    for sublist in wholelist:
        for atom in sublist:
            if is_negation(atom):
                check = complement(atom)
            else: check = atom
            if I.get(check,-1) == -1: return check
            
        

def suppose(pureatom,A,I):
    #''''''Propagates pureatom in A, supposes in I that pureatom is true''''''
    #Has been propagated before so no "pureatoms" just raw suppositions

    #Suppose
    if (is_negation(pureatom)):
        assert I.get(complement(pureatom),-1) == -1,'Acceding defined letter'
        I[complement(pureatom)] = 0
    else:
        assert I.get(pureatom,-1) == -1,'Acceding defined letter'
        I[pureatom] = 1
    
    pureatom_complement = complement(pureatom)
    i = 0
    while i != len(A): #if reaches last element then it is done
        sublist = A[i]
        if pureatom in sublist:
            A.pop(i) #remove whole
            #reset i
            i = 0
            continue
        elif pureatom_complement in sublist: sublist.remove(pureatom_complement) #Just remove that single one
        i +=1

'''
def suppose(pureatom,A,I):
    print (A)
    if len(pureatom) == 1:
        I[pureatom] = 1
    else:
        I[complement(pureatom)] = 0

    A = [sublist for sublist in A if pureatom not in sublist]

    pureatom_complement = complement(pureatom)

    temp = []
    
    aux = []
    for sublist in A:
        if pureatom_complement in sublist:
            temp = sublist
            temp.remove(pureatom_complement)
            aux.append(temp)
        else:
            aux.append(sublist)
    
    A = deepcopy(aux)
'''    
        
def DPLL(S,I):

    unitPropagate(S,I) #Propagate


    if has_empty(S): return 'Insatisfacible',{}
    if len(S) == 0: return 'Satisfacible',I #Is empty
    
    l = find_unassigned(S,I)
    S_prime = deepcopy(S)
    I_prime = deepcopy(I)
    suppose(l,S_prime,I_prime)
    
    maybe,S_prime_prime = DPLL(S_prime,I_prime)

    if maybe == 'Satisfacible': return 'Satisfacible',S_prime_prime 
    else:
        S_prime2 = deepcopy(S)
        I_prime2 = deepcopy(I)
        
        suppose(complement(l),S_prime2,I_prime2)
        
        return DPLL(S_prime2,I_prime2)



def fullDPLL(S,I,letters):
    '''Receives an S I and letters and ensures that I is filled with ONLY letters
    from letters'''
    let = deepcopy(letters)
    sat,sol = modifiedDPLL(S,I,let)

    sol_modified = {}
    for i in sol.keys():#Deletes any extra letters
        if i in letters: 
            sol_modified[i] = sol[i]
            
    return sat,sol_modified
    
def modifiedDPLL(S,I,letters):

    modifiedunitPropagate(S,I,letters) #Propagate
    
    if has_empty(S): return 'Insatisfacible',{}
    if len(S) == 0: return 'Satisfacible',I #Is empty
    
    #l = find_unassigned(S,I)
    #get l from letters
    if len(letters) != 0:
        for i in letters:
            if I.get(i,-1) == -1:
                l = i
                break
        letters.remove(l)
    else:
        l = find_unassigned(S,I)
        
    L_prime = deepcopy(letters)
    
    S_prime = deepcopy(S)
    I_prime = deepcopy(I)
    suppose(l,S_prime,I_prime)
    
    maybe,S_prime_prime = modifiedDPLL(S_prime,I_prime,L_prime)

    if maybe == 'Satisfacible': return 'Satisfacible',S_prime_prime 
    else:
        S_prime2 = deepcopy(S)
        I_prime2 = deepcopy(I)
        
        suppose(complement(l),S_prime2,I_prime2)
        
        return modifiedDPLL(S_prime2,I_prime2,L_prime)

def has_singleatom_modified(A,letters):
    for sublist in A:
        if len(sublist) == 1:
            pureatom = sublist[0]
            if complement(pureatom) in letters or pureatom in letters:
                return True   
    return False
    

    
def modifiedunitPropagate(A,partial,letters):
    
    while has_singleatom_modified(A,letters):
        for sublist in A:
            if len(sublist) == 1: #Is the single
                pureatom = sublist[0]                
                if complement(pureatom) in letters or pureatom in letters:
                    suppose(pureatom,A,partial)
                
                



                
                        
                        
                
        
    
