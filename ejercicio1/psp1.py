import math

class PSP1:
    def __init__(self):
        # Quitamos los argumentos de aquí para que no marque error al abrir
        pass

    def calcular_todo(self, listax, listay, xk):
        # Ahora los datos entran directamente a esta función
        n = len(listax)
        s_x = sum(listax)
        s_y = sum(listay)
        s_xy = sum(xi * yi for xi, yi in zip(listax, listay))
        s_x2 = sum(xi**2 for xi in listax)
        s_y2 = sum(yi**2 for yi in listay)

        xavg = s_x / n
        yavg = s_y / n

        # Fórmulas de Regresión
        b1 = (s_xy - (n * xavg * yavg)) / (s_x2 - (n * (xavg**2)))
        b0 = yavg - (b1 * xavg)

        # Correlación
        r_num = (n * s_xy) - (s_x * s_y)
        r_den = math.sqrt(((n * s_x2) - (s_x**2)) * ((n * s_y2) - (s_y**2)))
        r = r_num / r_den
        
        yk = b0 + (b1 * xk)

        return {
            "b0": b0, "b1": b1, "r": r, "r2": r**2, "yk": yk,
            "sum_x": s_x, "sum_y": s_y,
            "sum_x2": s_x2, "sum_y2": s_y2,
            "sum_xy": s_xy,
            "xavg": xavg, "yavg": yavg
        }