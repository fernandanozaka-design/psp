import math
# Importamos la lógica de los ejercicios anteriores
from ejercicio1.psp1 import PSP1
from ejercicio3.psp3 import PSP3

class PSP4:
    def __init__(self):
        # Instanciamos las clases anteriores para reutilizar su código
        self.psp1 = PSP1()
        self.psp3 = PSP3()

    def calcular_rangos(self, listax, listay, xk, significancia):
        """
        Calcula el Rango, UPI y LPI dado un conjunto de datos, un valor a predecir y una significancia.
        significancia: Generalmente 0.70 (70%) o 0.90 (90%)
        """
        n = len(listax)
        dof = n - 2

        # 1. Cálculos Base (PSP 1) 
        res_psp1 = self.psp1.calcular_todo(listax, listay, xk)
        b0 = res_psp1['b0']
        b1 = res_psp1['b1']
        yk = res_psp1['yk']
        xavg = res_psp1['xavg']

        # 2. Varianza y Desviación Estándar 
        # sum((yi - b0 - b1*xi)^2)
        suma_varianza = sum((yi - b0 - (b1 * xi))**2 for xi, yi in zip(listax, listay))
        
        # Validación para evitar división por cero si n <= 2
        if dof <= 0:
            raise ValueError("Se requieren al menos 3 pares de datos para calcular el rango.")
            
        std_dev = math.sqrt((1 / dof) * suma_varianza)

        # 3. Valor t de Student (PSP 3) 
        # Si la significancia es 70% (0.70), el área p buscada de un lado de la curva es 0.35
        p = significancia / 2.0
        
        # Llamamos al PSP 3 (que usará el PSP 2 por debajo). Usamos valores estándar para num_seg y tol
        res_psp3 = self.psp3.calcular_x(p, dof, num_seg=10, tol=0.00001)
        t = res_psp3['x']

        #  4. Rango 
        suma_denominador_rango = sum((xi - xavg)**2 for xi in listax)
        
        if suma_denominador_rango == 0:
            termino_raiz = 0 # Prevenir división por cero si todas las x son iguales
        else:
            termino_raiz = math.sqrt(1 + (1/n) + ((xk - xavg)**2 / suma_denominador_rango))
            
        rango = t * std_dev * termino_raiz

        #  5. UPI y LPI 
        upi = yk + rango
        lpi = yk - rango
        
        # En la industria, a veces el límite inferior no puede ser negativo para tiempo/líneas de código
        if lpi < 0:
            lpi = 0

        return {
            "rango": rango,
            "upi": upi,
            "lpi": lpi,
            "t": t,
            "std_dev": std_dev,
            "yk": yk,
            "dof": dof,
            "b0": b0,
            "b1": b1
        }