import random as r

numeroEntero = r.randint(0,10)
numeroDecimal = r.uniform(5,6)
caracteres = r.choice('esternocleidomastoideo')
miLista = ['Hola',10,True,20.9,numeroEntero,
           numeroDecimal,caracteres]
# print(miLista[3])       #Imprimir el dato 3 de miLista
# print(miLista[3:])      #Imprimir a partir del dato 3 de miLista
# print(miLista[:4])      #Imprimir hasta antes del dato 3 de miLista
# print(miLista[:])       #Imprimir todo lo que encuentra en mi lista
# print(miLista[2:4])     #Imprimir valores intermedios entre indice 3 y 4 

segundaLista=[]
for i in range(10):
    segundaLista.append(r.randint(0,10))
print(segundaLista)