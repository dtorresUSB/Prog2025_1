class Luhn:
    def __init__(self,card):
        self.cardNumber = card

    def valid(self):
        tarjeta = ""
        for digito in self.cardNumber:
            if digito != ' ':
                tarjeta += digito
        print(tarjeta)





Luhn("055 444 285").valid()
#              055444285
#       8273123273520569