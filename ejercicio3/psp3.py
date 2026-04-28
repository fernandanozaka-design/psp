class PSP3:
    def __init__(self):
        pass

    def calcular_x(self, p, dof, num_seg=10, tol=0.00001):
        from ejercicio2.psp2 import PSP2
        simpson = PSP2()

        x = 1.0
        d = 0.5
        errorSignoAnterior = 1  # inicializar positivo

        # Paso 2: calcular integral inicial
        res = simpson.calcular_simpson(x, dof, num_seg, tol)
        pCalculada = res['p']

        # Pasos 3 y 4
        if pCalculada < p:
            x = x + d
        else:
            x = x - d
            errorSignoAnterior = p - pCalculada
            d = d / 2

        # Ciclo pasos 5 al 8
        while True:
            res = simpson.calcular_simpson(x, dof, num_seg, tol)
            pCalculada = res['p']

            errorSigno = p - pCalculada
            errorSinSigno = abs(errorSigno)

            # Paso 5: verificar tolerancia
            if errorSinSigno < tol:
                break

            # Paso 6: ajustar d
            if errorSignoAnterior * errorSigno < 0:
                d = d / 2

            errorSignoAnterior = errorSigno

            # Pasos 7 y 8
            if pCalculada < p:
                x = x + d
            else:
                x = x - d

        return {
            "x": x,
            "pCalculada": pCalculada,
            "errorSinSigno": errorSinSigno
        }