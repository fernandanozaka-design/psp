import math
from ejercicio1.psp1 import PSP1
from ejercicio2.psp2 import PSP2
from ejercicio3.psp3 import PSP3

class PSP4:
    def __init__(self):
        self.psp1 = PSP1()
        self.psp2 = PSP2()
        self.psp3 = PSP3()

    def calcular_todo(self, listax, listay, xk, num_seg=10, tol=0.00001):
        n = len(listax)
        dof = n - 2

        # ── PSP1: regresión lineal ──
        res1 = self.psp1.calcular_todo(listax, listay, xk)
        r    = res1['r']
        r2   = res1['r2']
        b0   = res1['b0']
        b1   = res1['b1']
        yk   = res1['yk']
        xavg = res1['xavg']

        # ── Tail area: x = |r| * sqrt(n-2) / sqrt(1-r²) ──
        x_tail = abs(r) * math.sqrt(n - 2) / math.sqrt(1 - r2)
        res2   = self.psp2.calcular_simpson(x_tail, dof, num_seg, tol)
        p      = res2['p']
        tail_area = 1 - 2 * p

        # ── PSP3: t(0.35, dof) ──
        res3 = self.psp3.calcular_x(0.35, dof, num_seg, tol)
        t_val = res3['x']

        # ── Sigma ──
        sigma = math.sqrt(
            (1 / (n - 2)) * sum((yi - b0 - b1 * xi) ** 2
                                for xi, yi in zip(listax, listay))
        )

        # ── Rango ──
        sum_xi_xavg2 = sum((xi - xavg) ** 2 for xi in listax)
        raiz = math.sqrt(1 + (1 / n) + ((xk - xavg) ** 2 / sum_xi_xavg2))
        rango = t_val * sigma * raiz

        # ── UPI y LPI ──
        upi = yk + rango
        lpi = yk - rango

        return {
            "r": r, "r2": r2,
            "tail_area": tail_area,
            "b0": b0, "b1": b1,
            "yk": yk,
            "t_val": t_val,
            "sigma": sigma,
            "rango": rango,
            "upi": upi,
            "lpi": lpi
        }