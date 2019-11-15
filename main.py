from FNC import Tseitin,formaClausal
from DPLL import DPLL
from visual import export_horario
from Rules import genRules,letra,inverse_letra,test_genRules,friendly_multiOR

'''Changeable Variables '''

professor1 = 'Kurt'
professor2 = 'Bernard'
signature1 = 'Lógica I'
signature2 = 'Lógica II'
filename = 'test' #nombre de .jpg a salir




''' EXECUTION '''
    
letras = [letra(i) for i in range(1,45)] #1 to 45
#letras = [letra(i) for i in range(1,21)]

Rules = genRules()

'''
#disponibilidad_professor1 = [3,4,5,8]
#disponibilidad_professor2 = [2,4,7,8]
if disponibilidad_professor1 != 0:
    nodisp1 = ['-'+letra(i) for i in range(1,21) if i not in disponibilidad_professor1]
    add_rule = '(({0}O{1})>'.format(letra(41),letra(43)) + friendly_multiOR(nodisp1) +')'
    Rules = '(' + Rules + 'Y' + add_rule + ')'
    
if disponibilidad_professor2 != 0:
    nodisp2 = ['-'+letra(i+20) for i in range(1,21) if i not in disponibilidad_professor2]
    add_rule = '(({0}O{1})>'.format(letra(42),letra(44)) + friendly_multiOR(nodisp2) +')'
    Rules = '(' + Rules + 'Y' + add_rule + ')'
'''

clausal = formaClausal(Tseitin(Rules,letras))

#print (clausal)
#clausal.append(['-{0}'.format(letra(2))])
#interp = {letra(1):0}
satisfacible,solucion = DPLL(clausal,{})


solucion_filter = {}
for i in solucion.keys():
    if i in letras:
        solucion_filter[i] = solucion[i]

decoded = {}
for i in solucion_filter.keys():
    decoded[inverse_letra(i)] = solucion_filter[i]
print (satisfacible,decoded)


export_horario(decoded,professor1,professor2,signature1,signature2,filename)

