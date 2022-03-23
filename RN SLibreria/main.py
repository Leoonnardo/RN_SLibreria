import sys
from tkinter.tix import Tree
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from RN import *
import random


class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view.ui", self)
        self.botonIngresar.clicked.connect(self.ingresarDatos)
    
    def generarWs(self):
        listWs = []
        for i in range(2):
            ws = round(random.uniform(-1, 1), 4)
            listWs.append(ws)
        print(listWs)
        #Retorna lista de Ws random
        return listWs

    def ingresarDatos(self):
        ws = ""
        ws = self.generarWs()

        print("Ws = ", ws)
        self.ws.setText(f'{ws}')
        n = self.n1.text()
        print(n)

        iteraciones(n, ws)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())