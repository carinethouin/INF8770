# https://github.com/gabilodeau/INF8770

import numpy as np


def quantify(blocks, matrix):
    finals = []
    for block in blocks:
        final = np.zeros_like(block)
        final[:, :, 0] = np.round(np.divide(block[:, :, 0], matrix))
        final[:, :, 1] = np.round(np.divide(block[:, :, 1], matrix))
        final[:, :, 2] = np.round(np.divide(block[:, :, 2], matrix))
        finals.append(final)

    return finals


def invert(blocks, matrix):
    finals = []
    for block in blocks:
        final = np.zeros_like(block)
        final[:, :, 0] = np.round(np.multiply(block[:, :, 0], matrix))
        final[:, :, 1] = np.round(np.multiply(block[:, :, 1], matrix))
        final[:, :, 2] = np.round(np.multiply(block[:, :, 2], matrix))
        finals.append(final)

    return finals
