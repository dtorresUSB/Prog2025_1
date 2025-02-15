# # Uso del pass

# for i in range(10):
#     pass                    #Completa el codigo para que no haya error
# print('Finalizó el for')

# print('---------------------------------------------------')
#break

# for j in range(10):
#     print(j)
#     if j==4:
#         break
# print('finalizó el for')

# print('---------------------------------------------------')
# #continue

# for k in range(10):
#     if k==4:
#         continue
#     print(k)
# print('finalizó el for')

# print('---------------------------------------------------')

# num=1
# while num<10:
#     num+=1
#     if num == 4:
#         continue
#     print(num)
    
# print('Finalizó el while')

print('---------------------------------------------------')

secreto=21

numero = int(input('Ingrese un numero del 1 al 100: '))
flag = True

for i in range(10,0,-1):
    print(f'Te quedan {i-1} intentos')
    numero = int(input('Ingrese un numero del 1 al 100: '))
    if numero-10< secreto <numero+10:
        print('Estas cerca')
        continue
    print(f'Lastima {numero} no es el numero')
    if numero == secreto:
        flag = False
        break

if flag:
    print('BOOOOOOOOM!')
