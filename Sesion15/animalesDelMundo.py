from herencia import Animal,Perro,Gato


def main():
    snoopy = Perro('Snoopy','blanco','beagle','8 am')
    garfield = Gato('Garfield','naranja','british short hair red',9)
    piolin = Animal('Piolin','amarillo','canario')

    print(f'{snoopy.getNombre()} es un {snoopy.getRaza()}, hace {snoopy.hacerSonido()}'
          f', {snoopy.comer()} para salir a las {snoopy.getHoraSalida()}')
    print(f'{garfield.getNombre()} es un {garfield.getRaza()} y hace {garfield.hacerSonido()}'
          f', {garfield.comer()} y menos mal tengo {garfield.getNumeroVidas()} vidas')
    print(f'{piolin.getNombre()} es un {piolin.getRaza()} y hace {piolin.hacerSonido()}'
          f' y {piolin.comer()}')


if __name__ == "__main__":
    main()
