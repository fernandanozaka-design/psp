import sys
from PyQt5 import QtWidgets
from load.load_menu_principal import PantallaMenu

def Main():
    app = QtWidgets.QApplication(sys.argv)
    # Aquí solo llamamos al Menú
    ventana_principal = PantallaMenu()
    ventana_principal.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()