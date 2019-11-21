from FNC import Tseitin,formaClausal
from DPLL import DPLL
from visual import export_horario
from Rules import genRules,letra,inverse_letra,friendly_multiNEGAND

'''Variables a cambiar'''

professor1 = 'Kurt'
professor2 = 'Bernard'
signature1 = 'Lógica I'
signature2 = 'Lógica II'
filename = 'test' #Nombre de .jpg a salir

disponibilidad_professor1 = [1,2,3,4,5,8]
disponibilidad_professor2 = [2,4,7,9]
















''' EXECUTION '''
    
letras = [letra(i) for i in range(1,45)] #1 to 45

Rules = genRules()

if disponibilidad_professor1 != 0:
    notdisp = [letra(i) for i in range(1,21) if i not in disponibilidad_professor1]
    addrule = '(' + letra(41)+ '>' + friendly_multiNEGAND(notdisp) + ')'
    Rules = '(' + Rules + 'Y' + addrule + ')'
    
    #same for A2
    notdisp = [letra(i+20) for i in range(1,21) if i not in disponibilidad_professor1]
    addrule = '(' + letra(43)+ '>' + friendly_multiNEGAND(notdisp) + ')'
    Rules = '(' + Rules + 'Y' + addrule + ')'
    
if disponibilidad_professor1 != 0:
    notdisp = [letra(i) for i in range(1,21) if i not in disponibilidad_professor2]
    addrule = '(' + letra(42)+ '>' + friendly_multiNEGAND(notdisp) + ')'
    Rules = '(' + Rules + 'Y' + addrule + ')'
    
    #same for A2
    notdisp = [letra(i+20) for i in range(1,21) if i not in disponibilidad_professor2]
    addrule = '(' + letra(44)+ '>' + friendly_multiNEGAND(notdisp) + ')'
    Rules = '(' + Rules + 'Y' + addrule + ')'
    
    


clausal = formaClausal(Tseitin(Rules,letras))

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


