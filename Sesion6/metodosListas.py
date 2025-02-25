
def agregar(miLista):
    valor = int(input('Que numero desea agregar a la lista: '))
    miLista.append(valor)
    return miLista

def insertar(miLista):
    valor = int(input('Que numero desea ingresar: '))
    idx = int(input('En que posicion desea agregar el numero: '))
    miLista.insert(idx,valor)
    return miLista

def borrar(miLista):
    miLista.clear()
    return miLista

def remover(miLista):
    valor = int(input('Que numero desea remover: '))
    miLista.remove(valor)
    return miLista

def main():
    miLista=[]
    opciones = ['s',agregar,insertar,borrar,remover]
    while 1:
        print('Programa de uso de metodos para listas: \n'
            '1. Agregar un elemento a la lista\n'
            '2. Insertar un elemento a la lista\n'
            '3. Borrar toda la lista\n'
            '4. Remover un numero especifico de la lista\n'
            '0. Salir del programa\n')
        
        opc = int(input('Seleccione una de las anteriores opciones: '))

        if opciones[opc] != 's':
            miLista=opciones[opc](miLista)
        else:
            break
        
        print(miLista)


if __name__=="__main__":
    main()