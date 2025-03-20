
def lectura1():
    f = open('dataset//wcm.csv','rt',encoding='utf8')
    datos = f.readlines()
    DB = []
    for i in datos[1:]:
        DB.append(i.rstrip("\n").split(","))
    return DB

# def lectura2():
#     f = open('dataset//wcm.csv','rt',encoding='utf8')
#     datos = f.readlines()
#     DB = []
#     for i in range(len(datos)):
#         DB.append(datos[i].rstrip('\n').split(","))
#     print(DB)

# def lectura3():
#     f = open('dataset//wcm.csv','rt',encoding='utf8')
#     datos = f.readline()
#     DB = []
#     while datos != ['']:
#         DB.append(datos)
#         datos = f.readline().rstrip('\n').split(",")
#     print(DB)

def campeones(DB):
    listaCampeones={}
    for ronda in DB:
        if ronda[12]=='Final':
            if (ronda[2]>ronda[4]) or (ronda[3]>ronda[5]):
                campeon = ronda[0]
            else:
                campeon = ronda[1]

            if campeon not in listaCampeones:
                listaCampeones[campeon]=[ronda[-1]]
            else:
                listaCampeones[campeon].append(ronda[-1])
            print(f'El campeon copa mundo {ronda[-1]} fue {campeon}')
    
    for i in listaCampeones:
        print(f'{i} ha ganado {len(listaCampeones[i])} veces')

def main():
    datos = lectura1()
    #lectura2()
    #lectura3()
    print('Seleccione una de las siguientes opciones: '
    '1. Conocer los ganadores de cada copa mundo. ')

    menu = ['s',campeones]
    opc = int(input('Digite un opción: '))
    
    menu[opc](datos)
    


if __name__ == "__main__":
    main()