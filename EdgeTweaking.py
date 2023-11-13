from Struct import *


def lagrangeMultiplier(t, theta: list, turtle_A: Turtle, turtle_B: Turtle):
    S = []
    L_tol = max(0.0001 * max([abs(turtle_A.L[i] - turtle_B.L[i])
                              for i in range(0, len(turtle_A.L))]), 0.0001)
    alpha = 0
    E = 0
    F = 0
    G = 0
    U = 0
    V = 0
    for i in range(0, len(turtle_A.L)):
        L_AB = max(abs(turtle_A.L[i] - turtle_B.L[i]), L_tol)
        alpha += theta[i]
        E += pow(L_AB, 2) * pow(math.cos(alpha), 2)
        F += pow(L_AB, 2) * math.cos(alpha) * math.sin(alpha)
        G += pow(L_AB, 2) * pow(math.sin(alpha), 2)
        U += ((1 - t) * turtle_A.L[i] + t * turtle_B.L[i]) * math.cos(alpha)
        V += ((1 - t) * turtle_A.L[i] + t * turtle_B.L[i]) * math.sin(alpha)
    U *= 2
    V *= 2
    if E * G - F * F == 0:
        lambda_1 = 0
        lambda_2 = 0
    else:
        lambda_1 = (U * G - V * F) / (E * G - F * F)
        lambda_2 = (E * V - F * U) / (E * G - F * F)
    alpha = 0
    for i in range(0, len(turtle_A.L)):
        L_AB = max(abs(turtle_A.L[i] - turtle_B.L[i]), L_tol)
        alpha += theta[i]
        S.append(- (1 / 2) * pow(L_AB, 2) * (lambda_1 *
                                              math.cos(alpha) + lambda_2 * math.sin(alpha)))
    return S
