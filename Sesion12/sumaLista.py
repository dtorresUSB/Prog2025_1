from random import randint as r

def aleatorio():
    listaDatos = []
    n = int(input('Cantidad de numero aleatorios'))
    for i in range(n):
        listaDatos.append(r(0,10))
    return listaDatos

def sumaLista(datos):
    if len(datos)> 1:
        numero = datos[0]
        datos.pop(0)
        resultado = numero + sumaLista(datos)
    else:
        return datos[0]
    return resultado



if __name__=="__main__":
    datos = aleatorio()
    print(datos)
    print(sumaLista(datos))