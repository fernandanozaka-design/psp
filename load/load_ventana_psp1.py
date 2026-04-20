from PyQt5 import QtWidgets, uic
from ejercicio1.psp1 import PSP1

class PantallaPsp1(QtWidgets.QMainWindow):
    def __init__(self):
        super(PantallaPsp1, self).__init__()
        uic.loadUi('gui/ventana_psp_1.ui', self)
        
        self.logica = PSP1()
        self.datos_x = []
        self.datos_y = []

        try:
            self.boton_caso1.clicked.connect(self.cargar_caso1)
            self.boton_caso2.clicked.connect(self.cargar_caso2)
            self.boton_caso3.clicked.connect(self.cargar_caso3)
            self.boton_caso4.clicked.connect(self.cargar_caso4)
            self.boton_calcular.clicked.connect(self.ejecutar_calculos)
        except AttributeError as e:
            print(f"Error de nombres en Qt Designer: {e}")
        
        # Estilo para los labels de resultados
        estilo_resultado = """
            QLabel {
                background-color: #dce8f7;
                border: 2px solid #3a8fd4;
                border-radius: 4px;
                color: #1a1a1a;
                padding: 2px;
            }
        """
        self.label_b0.setStyleSheet(estilo_resultado)
        self.label_b1.setStyleSheet(estilo_resultado)
        self.label_yk.setStyleSheet(estilo_resultado)
        self.label_r.setStyleSheet(estilo_resultado)
        self.label_r2.setStyleSheet(estilo_resultado)


        estilo_boton = """
            QPushButton {
                background-color: #3a8fd4;
                color: white;
                border-radius: 4px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #2272b5;
            }
        """

        estilo_boton_calcular = """
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
        
        self.boton_caso1.setStyleSheet(estilo_boton)
        self.boton_caso2.setStyleSheet(estilo_boton)
        self.boton_caso3.setStyleSheet(estilo_boton)
        self.boton_caso4.setStyleSheet(estilo_boton)
        self.boton_calcular.setStyleSheet(estilo_boton_calcular)

    def cargar_caso1(self):
        self.datos_x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.datos_y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        print("Caso 1 cargado")

    def cargar_caso2(self):
        self.datos_x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.datos_y = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
        print("Caso 2 cargado")

    def cargar_caso3(self):
        self.datos_x = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        self.datos_y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        print("Caso 3 cargado")

    def cargar_caso4(self):
        self.datos_x = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        self.datos_y = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
        print("Caso 4 cargado")

    def ejecutar_calculos(self):
        try:
            if not self.datos_x or not self.datos_y:
                QtWidgets.QMessageBox.warning(self, "Aviso", "Selecciona un caso antes de calcular.")
                return
            texto = self.input_xk.text().strip()  
            if not texto:
                QtWidgets.QMessageBox.warning(self, "Aviso", "Ingresa un valor para Xk.")
                return
            valor_xk = float(texto)

            res = self.logica.calcular_todo(self.datos_x, self.datos_y, valor_xk)

            self.label_b0.setText(f"{res['b0']:.4f}")  
            self.label_b1.setText(f"{res['b1']:.4f}")  
            self.label_yk.setText(f"{res['yk']:.4f}")
            self.label_r.setText(f"{res['r']:.4f}")
            self.label_r2.setText(f"{res['r2']:.4f}")

            print(f"sum_x={res['sum_x']}, sum_y={res['sum_y']}, "
                  f"sum_x2={res['sum_x2']}, sum_y2={res['sum_y2']}, "
                  f"sum_xy={res['sum_xy']}, xavg={res['xavg']}, yavg={res['yavg']}")

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "El valor de Xk debe ser un número.")
        except Exception as e:
            print(f"Error en el cálculo: {e}")