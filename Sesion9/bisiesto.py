def bisiesto(año):
    if año%4 == 0 and año%100 != 0:
        return True
    if año%400==0:
        return True
    return False

def main():
    lista_años = []
    n = 0
    year = int(input('Ingrese un año: '))
    while n<30:
        if bisiesto(year):
            lista_años.append(year)
            n+=1
        year+=1
    print(lista_años)

if __name__ == "__main__":
    main()