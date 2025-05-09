import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic
import serial
from PyQt5.QtCore import QTimer

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.puerto()
        self.initGUI()
        

    def initGUI(self):
        uic.loadUi('segundos.ui',self)
        self.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.leer_puerto)
        self.timer.start(100)

    def leer_puerto(self):
        if self.ser.in_waiting > 0:
            dato = self.ser.readline().decode('utf-8').strip()
            self.label_respuesta.setText(str(dato))

    def puerto(self):
        puerto = 'COM5'
        velocidad = 9600
        self.ser = serial.Serial(puerto, velocidad)
        
def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()