
def espaciado(texto):
    palabra=''
    for i in texto:
        if i != ' ':
            palabra+=i
    return palabra


def palindromo(texto):
    longitud = len(texto)//2
    for i in range(longitud):
        if texto[i]!=texto[len(texto)-1-i]:
            return False
    return True

if __name__=="__main__":
    texto = input('Ingrese una frase o palabra\n').lower().strip()
    #texto = espaciado(texto.lower().strip())
    print(palindromo(texto))