from PyQt5 import QtWidgets, uic
from load.load_ventana_psp1 import PantallaPsp1
from load.load_ventana_psp2 import PantallaPsp2

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
        self.btn_salir.setStyleSheet(estilo_boton_menu)

        
        self.btn_psp1.clicked.connect(self.abrir_ejercicio)
        self.btn_psp2.clicked.connect(self.abrir_ejercicio2)
        self.btn_salir.clicked.connect(self.close)

    def abrir_ejercicio(self):
        self.ventana_ejercicio = PantallaPsp1()
        self.ventana_ejercicio.destroyed.connect(self.show)  
        self.ventana_ejercicio.show()
        self.hide()
    
    def abrir_ejercicio2(self):
        self.ventana_ejercicio2 = PantallaPsp2()
        self.ventana_ejercicio2.destroyed.connect(self.show)
        self.ventana_ejercicio2.show()
        self.hide()