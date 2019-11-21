def inverse_letra(i):
    return ord(i)-25000
    #return int(i)

def letra(i):
    return chr(25000+i)

def checkMinusParenth(string):
    '''Checks if there is a minus before a left parenthesis in anystring '''

    
    for i in range(len(string)):
        if string[i] == '-':
            if string[i+1] == '(': return 'Error'
    return 'Proper String'

def multiAND(alist):#    '''Receives integer i and returns chr(40000+i)'''
    '''Receives a list and returns equivalent AND between each list element'''
    assert len(alist) > 2,'multiAND received list less than 3 elements'

    returnString = '(' + alist[0] + 'Y' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'Y' + element + ')'

    return returnString

def multiOR(alist):
    '''Receives a list and returns equivalent OR between each list element'''
    assert len(alist) > 2,'multiOR received list less than 3 elements'

    returnString = '(' + alist[0] + 'O' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'O' + element + ')'

    return returnString

def friendly_multiOR(alist):
    '''Receives a list and returns equivalent OR between each list element'''
    if len(alist) == 1: return alist[0]
    elif len(alist) == 2: return '(' + alist[0] + 'O' + alist[1] + ')'
 
    returnString = '(' + alist[0] + 'O' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'O' + element + ')'

    return returnString

def friendly_multiAND(alist):
    '''Receives a list and returns equivalent AND between each list element'''
    if len(alist) == 1: return alist[0]
    elif len(alist) == 2: return '(' + alist[0] + 'Y' + alist[1] + ')'
 
    returnString = '(' + alist[0] + 'Y' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'Y' + element + ')'

    return returnString

def multiNEGAND(alist): 
    '''Receives a list and returns and AND between the negated element of each in list'''
    assert len(alist) > 2,'multiNEGAND received list less than 3 elements'



    returnString = '(' + '-' +alist[0] + 'Y' +'-' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'Y' + '-' +element + ')'

    return returnString

def friendly_multiNEGAND(alist):
    if len(alist) == 1: return '-'+alist[0]
    elif len(alist) == 2: return '(-' + alist[0] + 'Y-' + alist[1] + ')'
    
    returnString = '(' + '-' +alist[0] + 'Y' +'-' +alist[1] + ')'
    for element in alist[2:]:
        returnString = '(' + returnString + 'Y' + '-' +element + ')'

    return returnString

def genRules():
    '''Returns Rules'''

    rule1 = '(({0}Y{1})Y(-{2}Y-{3}))'.format(letra(41),letra(44),letra(42),letra(43))
    rule2 = '(({0}Y{1})Y(-{2}Y-{3}))'.format(letra(42),letra(43),letra(41),letra(44))

    ProfessorRule = '(' + rule1 + 'O' + rule2 + ')'
    
    #get all possibilities
    poss_list =[]
    for i in range(1,21): #get all combinations without repetition
        for j in [x for x in range(1,21) if x > i]:
            poss_list.append((i,j))
    
    ruleholder = []
    for dia in range(1,6): # 1-5
        horas_diarias = []
        for j in range(0,4):
            horas_diarias.append(j*5+dia)
        
        for bloque in horas_diarias:
            ruleholder.append('(' + '-' + letra(bloque) + 'O' +multiNEGAND([letra(x) for x in horas_diarias if x != bloque]) + ')')
    
    days_rule = multiAND(ruleholder)
    
    ruleholder = []
    for dia in range(1,6): # 1-5
        horas_diarias = []
        for j in range(0,4):
            horas_diarias.append(j*5+dia+20)
        for bloque in horas_diarias:
            ruleholder.append('(' + '-'+ letra(bloque) + 'O' +multiNEGAND([letra(x) for x in horas_diarias if x != bloque]) + ')')
   
    days_rule2 = multiAND(ruleholder)

    '''Sessions RULES '''
    
    poss_list =[]
    for i in range(1,21): #get all combinations without repetition
        for j in [x for x in range(1,21) if x > i]:
            poss_list.append((i,j))

    rule = []
    for X,Y in poss_list:
        lista = [letra(X),letra(Y)]+['-'+letra(i) for i in range(1,21) if i != X and i != Y]
        string = multiAND(lista) 
        rule.append(string)
    
    sessions_ruleA1 = multiOR(rule)
    
    #repeat for signature 2
    poss_list =[]
    for i in range(21,41): #get all combinations without repetition
        for j in [x for x in range(21,41) if x > i]:
            poss_list.append((i,j))

    rule = []
    for X,Y in poss_list:
        lista = [letra(X),letra(Y)]+['-'+letra(i) for i in range(21,41) if i != X and i != Y]
        string = multiAND(lista) 
        rule.append(string)
    
    sessions_ruleA2 = multiOR(rule)
    
    whole_rules = multiAND([ProfessorRule,sessions_ruleA1,sessions_ruleA2,days_rule,days_rule2])

    return whole_rules
    
    

def checkParenthesis(string):
    '''returns true if string has same number of open parenthesis as closing parenthesis'''
    left_counter = 0
    right_counter = 0
    for char in string:
        if char == '(': left_counter +=1
        elif char == ')': right_counter +=1
    return left_counter == right_counter











