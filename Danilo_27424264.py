#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


def derivada(f, h = 0.01):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _


def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.

    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """
    def polinomio(x):
        i = 0
        while (i < n):
            if (i == 0):
                asig1 = f(x0)
                fun = f
            else:
                asig2 = derivada(fun)
                fun = asig2
                asig3 = asig2 (x0)
                asig1 = asig1 + ( asig3*((x-x0)**i)/math.factorial(i) )  
            i = i + 1 
        return asig1
    return polinomio


if __name__ == '__main__':
    f = lambda x: math.sin(x)
    taylor = polinomio_taylor(f,0,4)
    print("valor real:",taylor(0.3))
    pass