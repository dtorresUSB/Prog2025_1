
def recursion(n):
    if n>0:
        resultado =(2*n-1)+recursion(n-1)
    else:
        resultado = 0
    return resultado



if __name__=="__main__":
    num = int(input('Cantidad de numeros impares: '))
    print(recursion(num))