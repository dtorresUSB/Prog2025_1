import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        uic.loadUi('calculadora.ui',self)
        self.show()

        self.calcular.clicked.connect(self.imprimir)

    def imprimir(self):
        self.resultado.setText('Funcionó')
        
def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()