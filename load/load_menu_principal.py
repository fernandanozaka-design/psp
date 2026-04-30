from PyQt5 import QtWidgets, uic
from load.load_ventana_psp1 import PantallaPsp1
from load.load_ventana_psp2 import PantallaPsp2
from load.load_ventana_psp3 import PantallaPsp3
from load.load_ventana_psp4 import PantallaPsp4

class PantallaMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaMenu, self).__init__()
        uic.loadUi('gui/ventana_menu.ui', self)

        
        estilo_boton_menu = """
            QPushButton {
                background-color: #FF69B4;
                color: white;
                border-radius: 4px;
                padding: 6px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #FFB6C1;
            }
        """
        self.btn_psp1.setStyleSheet(estilo_boton_menu)
        self.btn_psp2.setStyleSheet(estilo_boton_menu)
        self.btn_psp3.setStyleSheet(estilo_boton_menu)  
        self.btn_psp4.setStyleSheet(estilo_boton_menu)
        self.btn_salir.setStyleSheet(estilo_boton_menu)

        
        self.btn_psp1.clicked.connect(self.abrir_ejercicio)
        self.btn_psp2.clicked.connect(self.abrir_ejercicio2)
        self.btn_psp3.clicked.connect(self.abrir_ejercicio3)
        self.btn_psp4.clicked.connect(self.abrir_ejercicio4)
        self.btn_salir.clicked.connect(self.close)

    def abrir_ejercicio(self):
        try:
            self.ventana_ejercicio = PantallaPsp1()
            self.ventana_ejercicio.destroyed.connect(self.show)
            self.ventana_ejercicio.show()
            self.hide()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo abrir PSP1:\n{e}")
            self.show()

    def abrir_ejercicio2(self):
        try:
            self.ventana_ejercicio2 = PantallaPsp2()
            self.ventana_ejercicio2.destroyed.connect(self.show)
            self.ventana_ejercicio2.show()
            self.hide()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo abrir PSP2:\n{e}")
            self.show()

    def abrir_ejercicio3(self):
        try:
            self.ventana_ejercicio3 = PantallaPsp3()
            self.ventana_ejercicio3.destroyed.connect(self.show)
            self.ventana_ejercicio3.show()
            self.hide()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo abrir PSP3:\n{e}")
            self.show()

    def abrir_ejercicio4(self):
        try:
            self.ventana_ejercicio4 = PantallaPsp4()
            self.ventana_ejercicio4.destroyed.connect(self.show)
            self.ventana_ejercicio4.show()
            self.hide()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo abrir PSP4:\n{e}")
            self.show()