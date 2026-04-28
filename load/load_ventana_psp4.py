from PyQt5 import QtWidgets, uic
from ejercicio4.psp4 import PSP4 # Tu lógica matemática

class PantallaPsp4(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaPsp4, self).__init__()
        uic.loadUi('gui/ventana_psp_4.ui', self)
        
        self.logica = PSP4()
        self.datos_x = []
        self.datos_y = []

        # Valores por defecto
        self.input_significancia.setText("0.70")

        # --- ESTILOS ---
        estilo_resultado = "QLabel { background-color: #dce8f7; border: 2px solid #3a8fd4; border-radius: 4px; padding: 2px; }"
        estilo_boton_calc = "QPushButton { background-color: #27ae60; color: white; font-weight: bold; border-radius: 4px; }"
        
        # Aplicar a los nuevos campos (asegúrate que los nombres coincidan con tu .ui)
        self.label_rango.setStyleSheet(estilo_resultado)
        self.label_upi.setStyleSheet(estilo_resultado)
        self.label_lpi.setStyleSheet(estilo_resultado)
        self.label_sigma.setStyleSheet(estilo_resultado)
        self.boton_calcular.setStyleSheet(estilo_boton_calc)

        # Conexiones
        self.boton_caso1.clicked.connect(self.cargar_caso1)
        # ... conectar caso 2, 3 y 4 igual que en PSP1 ...
        self.boton_calcular.clicked.connect(self.ejecutar_calculos)

    def cargar_caso1(self):
        # Datos del Test 1 de tu documento
        self.datos_x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.datos_y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        self.input_xk.setText("386")
        print("Caso Test 1 cargado")

    def ejecutar_calculos(self):
        try:
            xk = float(self.input_xk.text().strip())
            sig = float(self.input_significancia.text().strip())
            
            if not self.datos_x:
                return

            # Llamamos a la lógica del Programa 4
            res = self.logica.calcular_rangos(self.datos_x, self.datos_y, xk, sig)

            # Llenamos los labels
            self.label_yk.setText(f"{res['yk']:.4f}")
            self.label_rango.setText(f"{res['rango']:.4f}")
            self.label_upi.setText(f"{res['upi']:.4f}")
            self.label_lpi.setText(f"{res['lpi']:.4f}")
            self.label_sigma.setText(f"{res['std_dev']:.4f}")
            self.label_t.setText(f"{res['t']:.5f}")
            
            # También podrías mostrar b0 y b1 para verificar
            self.label_b0.setText(f"{res['b0']:.4f}")
            self.label_b1.setText(f"{res['b1']:.4f}")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error: {str(e)}")