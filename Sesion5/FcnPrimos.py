def primo(numero):
    for i in range(2,numero+1):
        if numero%i == 0:
            if numero == i:
                return True
            else:
                return False
            

if __name__=="__main__":
    numero = int(input('Ingrese un numero: '))
    print(primo(numero))
    