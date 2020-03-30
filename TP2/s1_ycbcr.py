import numpy as np


def limits(value):
    if value > 255:
        return 255
    elif value < 0:
        return 0
    return value


def getY(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    return limits(y)


def getCb(b, y):
    cb = 128 + 0.564 * (b - y)
    return limits(cb)


def getCr(r, y):
    cr = 128 + 0.713 * (r - y)
    return limits(cr)


def rgbToYcbcr(initial):
    h = len(initial)
    w = len(initial[0])
    final = np.zeros_like(initial)

    for row in range(h):
        for col in range(w):
            r = initial[row][col][0]
            g = initial[row][col][1]
            b = initial[row][col][2]
            y = getY(r, g, b)
            if row % 2 == 0:
                if col % 2 == 0:
                    final[row][col][0] = y
                    final[row][col][1] = getCb(b, y)
                    final[row][col][2] = getCr(r, y)
                else:
                    final[row][col] = final[row][col - 1]
                    final[row][col][0] = y
            else:
                final[row] = final[row - 1]
                final[row][col][0] = y

    return final


def getR(y, cr):
    r = y + 1.403 * (cr - 128)
    return limits(r)


def getG(y, cr, cb):
    g = y - 0.714 * (cr - 128) - 0.344 * (cb - 128)
    return limits(g)


def getB(y, cb):
    b = y + 1.773 * (cb - 128)
    return limits(b)


def ycbcrToRgb(initial):
    h = len(initial)
    w = len(initial[0])
    final = np.zeros_like(initial)

    for row in range(h):
        for col in range(w):
            y = initial[row][col][0]
            cb = initial[row][col][1]
            cr = initial[row][col][2]
            final[row][col][0] = getR(y, cr)
            final[row][col][1] = getG(y, cr, cb)
            final[row][col][2] = getB(y, cb)

    return final
