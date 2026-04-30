from PyQt5 import QtWidgets, uic
from ejercicio4.psp4 import PSP4

class PantallaPsp4(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaPsp4, self).__init__()
        uic.loadUi('gui/ventana_psp_4.ui', self)

        # Estilo labels de resultados
        estilo_resultado = """
            QLabel {
                background-color: #dce8f7;
                border: 2px solid #3a8fd4;
                border-radius: 4px;
                color: #1a1a1a;
                padding: 2px;
            }
        """
        self.label_r.setStyleSheet(estilo_resultado)
        self.label_r2.setStyleSheet(estilo_resultado)
        self.label_tail.setStyleSheet(estilo_resultado)
        self.label_b0.setStyleSheet(estilo_resultado)
        self.label_b1.setStyleSheet(estilo_resultado)
        self.label_yk.setStyleSheet(estilo_resultado)
        self.label_rango.setStyleSheet(estilo_resultado)
        self.label_upi.setStyleSheet(estilo_resultado)
        self.label_lpi.setStyleSheet(estilo_resultado)

        # Estilo botones
        estilo_boton = """
            QPushButton {
                background-color: #FF69B4;
                color: white;
                border-radius: 4px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #C71585;
            }
        """
        self.boton_caso1.setStyleSheet(estilo_boton)
    
        # Estilo para el botón de calcular (Verde)
        estilo_boton_calcular = """
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 4px;
                padding: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219150;
            }
        """
        self.boton_calcular.setStyleSheet(estilo_boton_calcular)

        self.logica = PSP4()
        self.datos_x = []
        self.datos_y = []

        try:
            self.boton_caso1.clicked.connect(self.cargar_caso1)
            self.boton_calcular.clicked.connect(self.ejecutar_calculos)
        except AttributeError as e:
            print(f"Error de nombres en Qt Designer: {e}")

    def cargar_caso1(self):
        self.datos_x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.datos_y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        print("Caso 1 cargado")

    def ejecutar_calculos(self):
        try:
            if not self.datos_x or not self.datos_y:
                QtWidgets.QMessageBox.warning(self, "Aviso", "Selecciona un caso antes de calcular.")
                return

            xk = float(self.input_xk.text().strip())

            res = self.logica.calcular_todo(self.datos_x, self.datos_y, xk)

            self.label_r.setText(f"{res['r']:.10f}")
            self.label_r2.setText(f"{res['r2']:.10f}")
            self.label_tail.setText(f"{res['tail_area']:.8E}")
            self.label_b0.setText(f"{res['b0']:.10f}")
            self.label_b1.setText(f"{res['b1']:.10f}")
            self.label_yk.setText(f"{res['yk']:.7f}")
            self.label_rango.setText(f"{res['rango']:.7f}")
            self.label_upi.setText(f"{res['upi']:.7f}")
            self.label_lpi.setText(f"{res['lpi']:.7f}")

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Ingresa un valor numérico para Xk.")
        except Exception as e:
            print(f"Error: {e}")