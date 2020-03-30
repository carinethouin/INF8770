# import matplotlib.pyplot as py
import numpy as np


def zigzag(initial):
    final = []

    final.append(initial[0][0][0])
    final.append(initial[0][0][1])
    final.append(initial[0][0][2])

    final.append(initial[0][1][0])
    final.append(initial[0][1][1])
    final.append(initial[0][1][2])

    final.append(initial[1][0][0])
    final.append(initial[1][0][1])
    final.append(initial[1][0][2])

    final.append(initial[2][0][0])
    final.append(initial[2][0][1])
    final.append(initial[2][0][2])

    final.append(initial[0][2][0])
    final.append(initial[0][2][1])
    final.append(initial[0][2][2])

    final.append(initial[0][3][0])
    final.append(initial[0][3][1])
    final.append(initial[0][3][2])

    final.append(initial[3][0][0])
    final.append(initial[3][0][1])
    final.append(initial[3][0][2])

    final.append(initial[4][0][0])
    final.append(initial[4][0][1])
    final.append(initial[4][0][2])

    final.append(initial[0][4][0])
    final.append(initial[0][4][1])
    final.append(initial[0][4][2])

    final.append(initial[0][5][0])
    final.append(initial[0][5][1])
    final.append(initial[0][5][2])

    final.append(initial[5][0][0])
    final.append(initial[5][0][1])
    final.append(initial[5][0][2])

    final.append(initial[6][0][0])
    final.append(initial[6][0][1])
    final.append(initial[6][0][2])

    final.append(initial[0][6][0])
    final.append(initial[0][6][1])
    final.append(initial[0][6][2])

    final.append(initial[0][7][0])
    final.append(initial[0][7][1])
    final.append(initial[0][7][2])

    final.append(initial[7][0][0])
    final.append(initial[7][0][1])
    final.append(initial[7][0][2])

    final.append(initial[7][1][0])
    final.append(initial[7][1][1])
    final.append(initial[7][1][2])

    final.append(initial[1][7][0])
    final.append(initial[1][7][1])
    final.append(initial[1][7][2])

    final.append(initial[2][7][0])
    final.append(initial[2][7][1])
    final.append(initial[2][7][2])

    final.append(initial[7][2][0])
    final.append(initial[7][2][1])
    final.append(initial[7][2][2])

    final.append(initial[7][3][0])
    final.append(initial[7][3][1])
    final.append(initial[7][3][2])

    final.append(initial[3][7][0])
    final.append(initial[3][7][1])
    final.append(initial[3][7][2])

    final.append(initial[4][7][0])
    final.append(initial[4][7][1])
    final.append(initial[4][7][2])

    final.append(initial[7][4][0])
    final.append(initial[7][4][1])
    final.append(initial[7][4][2])

    final.append(initial[7][5][0])
    final.append(initial[7][5][1])
    final.append(initial[7][5][2])

    final.append(initial[5][7][0])
    final.append(initial[5][7][1])
    final.append(initial[5][7][2])

    final.append(initial[6][7][0])
    final.append(initial[6][7][1])
    final.append(initial[6][7][2])

    final.append(initial[7][6][0])
    final.append(initial[7][6][1])
    final.append(initial[7][6][2])

    final.append(initial[7][7][0])
    final.append(initial[7][7][1])
    final.append(initial[7][7][2])

    return final
