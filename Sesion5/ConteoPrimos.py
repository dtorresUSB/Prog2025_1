from FcnPrimos import primo

cantidad = int(input('Cuantos primos desea generar: '))

n=0         #cantidad de numeros primos encontrados
numero=2 
txt = ''
while n < cantidad:
    if primo(numero):
        txt += f'{numero}, '        #txt = txt + f'{numero}, '
        n+=1
    numero+=1

print(txt.rstrip(", ")+".")