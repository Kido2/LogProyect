from visual import export_horario
'''Changeable Variables '''
professor1 = 'Kurt'
professor2 = 'Bernard'
signature1 = 'Lógica I'
signature2 = 'Lógica II'
filename = 'test' #nombre de .jpg a salir

ejemplo = {}
for i in range(1,44):
    ejemplo[i] = 0

for i in [17,5,8,21,34,44,41]:
    ejemplo[i] = 1

#Diccionario de ejemplo

export_horario(ejemplo,professor1,professor2,signature1,signature2,filename)
