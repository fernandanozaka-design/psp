import math


class PSP2:
    def __init__(self):
        pass

    def funcion_t(self, xi, dof):
        # Función de distribución t de Student
        num = math.gamma((dof + 1) / 2)
        den = math.sqrt(dof * math.pi) * math.gamma(dof / 2)
        parte1 = num / den
        parte2 = (1 + (xi ** 2) / dof) ** (-(dof + 1) / 2)
        return parte1 * parte2

    def calcular_simpson(self, x, dof, num_seg, E):
        # num_seg debe ser par
        if num_seg % 2 != 0:
            num_seg += 1

        p_anterior = 0
        tabla = []

        while True:
            w = x / num_seg
            sumaf = 0

            for i in range(num_seg + 1):
                xi = i * w
                f = self.funcion_t(xi, dof)

                if i == 0 or i == num_seg:
                    mult = 1
                elif i % 2 != 0:
                    mult = 4
                else:
                    mult = 2

                termino = f * mult
                sumaf += termino

                tabla.append({
                    "i": i,
                    "xi": round(xi, 6),
                    "f": round(f, 8),
                    "mult": mult,
                    "termino": round(termino, 8)
                })

            p = (w / 3) * sumaf

            # Verificar convergencia
            if abs(p - p_anterior) < E:
                break

            p_anterior = p
            num_seg *= 2
            tabla = []

        return {
            "p": p,
            "num_seg": num_seg,
            "w": w,
            "sumaf": sumaf,
            "tabla": tabla
        }