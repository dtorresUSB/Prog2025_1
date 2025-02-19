from FcnPrimos import primo

def imprimir(valor):
    if valor:
        print('El numero es primo')
    else:
        print('El numero no es primo')



if __name__=="__main__":
    print(__name__)
    numero = int(input('Ingrese un numero: '))
    resultado = primo(numero)
    imprimir(resultado)
