from Struct import *
from EdgeTweaking import *


def intrinsicShapeInterpolation(t, turtle_A: Turtle, turtle_B: Turtle):
    theta = []
    L = []
    p_0 = (1 - t) * turtle_A.p_0 + t * turtle_B.p_0
    for i in range(0, len(turtle_A.L)):
        theta.append((1 - t) * turtle_A.theta[i] + t * turtle_B.theta[i])

    S = lagrangeMultiplier(t, theta, turtle_A, turtle_B)

    for i in range(0, len(turtle_A.L)):
        L.append((1 - t) * turtle_A.L[i] + t * turtle_B.L[i] + S[i])
    return Turtle(p_0, theta, L)
