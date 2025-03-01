from random import randint as r

def matriz(filas,columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])           #Creando el espacio de las filas
        for j in range(columnas):
            matriz[i].append(r(0,100))      #Llena las filas
    print(matriz)    
    return matriz
    
def impresion(datos):
    for i in datos:
        print(i)

def escalar(matriz):
    numero = int(input('Ingrese el valor escalar de la matriz: '))
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = matriz[i][j] * numero
    return matriz

def main():
    print('inicio del programa')
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    datos = matriz(filas,columnas)
    impresion(datos)
    datos = escalar(datos)
    impresion(datos)

if __name__ == "__main__":
    main()
