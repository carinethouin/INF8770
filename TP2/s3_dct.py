# https://github.com/gabilodeau/INF8770

import numpy as np
import scipy.fftpack as dctpack


def dct(blocks):
    finals = []
    for block in blocks:
        final = np.zeros_like(block)
        final[:, :, 0] = dctpack.dct(dctpack.dct(
            block[:, :, 0]-128, axis=0, norm='ortho'), axis=1, norm='ortho')
        final[:, :, 1] = dctpack.dct(dctpack.dct(
            block[:, :, 1]-128, axis=0, norm='ortho'), axis=1, norm='ortho')
        final[:, :, 2] = dctpack.dct(dctpack.dct(
            block[:, :, 2]-128, axis=0, norm='ortho'), axis=1, norm='ortho')
        finals.append(final)

    return finals


def invert(blocks):
    finals = []
    for block in blocks:
        final = np.zeros_like(block)
        final[:, :, 0] = dctpack.idct(dctpack.idct(
            block[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho') + 128
        final[:, :, 1] = dctpack.idct(dctpack.idct(
            block[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho') + 128
        final[:, :, 2] = dctpack.idct(dctpack.idct(
            block[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho') + 128
        finals.append(final)

    return finals
