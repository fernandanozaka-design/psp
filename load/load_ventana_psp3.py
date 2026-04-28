from PyQt5 import QtWidgets, uic
from ejercicio3.psp3 import PSP3

class PantallaPsp3(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaPsp3, self).__init__()
        uic.loadUi('gui/ventana_psp_3.ui', self)

        self.logica = PSP3()

        # Valores fijos por defecto
        self.input_numseg.setText("10")
        self.input_tol.setText("0.00001")

        # Estilo para los labels de resultados (Azul claro con borde)
        estilo_resultado = """
            QLabel {
                background-color: #dce8f7;
                border: 2px solid #3a8fd4;
                border-radius: 4px;
                color: #1a1a1a;
                padding: 2px;
            }
        """
        self.label_x.setStyleSheet(estilo_resultado)
        self.label_pcalc.setStyleSheet(estilo_resultado)
        self.label_error.setStyleSheet(estilo_resultado)

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

        try:
            self.boton_calcular.clicked.connect(self.ejecutar_calculos)
        except AttributeError as e:
            print(f"Error de nombres en Qt Designer: {e}")

    def ejecutar_calculos(self):
        try:
            p      = float(self.input_p.text().strip())
            dof    = int(self.input_dof.text().strip())
            num_seg = int(self.input_numseg.text().strip())
            tol    = float(self.input_tol.text().strip())

            res = self.logica.calcular_x(p, dof, num_seg, tol)

            self.label_x.setText(f"{res['x']:.5f}")
            self.label_pcalc.setText(f"{res['pCalculada']:.8f}")
            self.label_error.setText(f"{res['errorSinSigno']:.8f}")

            print(f"x = {res['x']:.5f}")
            print(f"pCalculada = {res['pCalculada']:.8f}")
            print(f"error = {res['errorSinSigno']:.8f}")

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Verifica que todos los campos sean números válidos.")
        except Exception as e:
            print(f"Error en el cálculo: {e}")