from PyQt5 import QtWidgets, uic
from ejercicio2.psp2 import PSP2

class PantallaPsp2(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaPsp2, self).__init__()
        uic.loadUi('gui/ventana_psp_2.ui', self)

        self.logica = PSP2()

        self.input_numseg.setText("10")
        self.input_e.setText("0.00001")


        estilo_resultado = """
            QLabel {
                background-color: #dce8f7;
                border: 2px solid #3a8fd4;
                border-radius: 4px;
                color: #1a1a1a;
                padding: 2px;
            }
        """
        self.label_p.setStyleSheet(estilo_resultado)
        self.label_w.setStyleSheet(estilo_resultado)
        self.label_sumaf.setStyleSheet(estilo_resultado)
        self.label_numseg.setStyleSheet(estilo_resultado)


        estilo_boton= """
            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 4px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """
        self.boton_calcular.setStyleSheet(estilo_boton)

        try:
            self.boton_calcular.clicked.connect(self.ejecutar_calculos)
        except AttributeError as e:
            print(f"Error de nombres en Qt Designer: {e}")

    def ejecutar_calculos(self):
        try:
            x     = float(self.input_x.text().strip())
            dof   = int(self.input_dof.text().strip())
            num_seg = int(self.input_numseg.text().strip())
            E     = float(self.input_e.text().strip())

            res = self.logica.calcular_simpson(x, dof, num_seg, E)

            self.label_p.setText(f"{res['p']:.8f}")
            self.label_w.setText(f"{res['w']:.8f}")
            self.label_sumaf.setText(f"{res['sumaf']:.8f}")
            self.label_numseg.setText(str(res['num_seg']))

            print("\n=== TABLA DE SIMPSON ===")
            print(f"{'i':>4} {'xi':>10} {'f(xi)':>14} {'mult':>6} {'término':>14}")
            print("-" * 52)
            for fila in res['tabla']:
                print(f"{fila['i']:>4} {fila['xi']:>10.6f} {fila['f']:>14.8f} {fila['mult']:>6} {fila['termino']:>14.8f}")
            print("-" * 52)
            print(f"sumaf = {res['sumaf']:.8f}")
            print(f"p     = {res['p']:.8f}")

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Verifica que todos los campos sean números válidos.")
        except Exception as e:
            print(f"Error en el cálculo: {e}")