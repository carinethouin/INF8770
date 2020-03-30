import numpy as np


def isDimMultipleOf16(h, w):
    if h % 16 != 0 or w % 16 != 0:
        return 0
    else:
        return 1


def divider(image, size):
    h = len(image)
    w = len(image[0])

    if isDimMultipleOf16(h, w):
        blocks = []
        row = 0
        while row < h:
            col = 0
            while col < w:
                blocks.append(image[row:row + size, col:col + size])
                col += size
            row += size
        return np.array(blocks)


def invert(blocks, size, initial):
    h = len(initial)
    w = len(initial[0])
    final = np.zeros_like(initial)
    index = 0

    for row in range(0, h, size):
        for col in range(0, w, size):
            final[row:row + size,
                  col:col + size] = blocks[index]
            index += 1

    return final
