
import numpy as np

nInst = 50
currentPos = np.zeros(nInst)


def getMyPosition(prcSoFar):
    nInst, nt = prcSoFar.shape

    if nt < 2:
        return np.zeros(nInst, dtype=int)

    short_win = 20
    long_win = 50

    short_slice = prcSoFar[:, -short_win:]
    long_slice = prcSoFar[:, -long_win:]

    short_ma = np.mean(short_slice, axis=1)
    long_ma = np.mean(long_slice, axis=1)

    signal = np.where(short_ma > long_ma, 1, -1)

    dollar_target = 5000.0
    current_prices = np.where(prcSoFar[:, -1] == 0, 1.0, prcSoFar[:, -1])

    positions = (signal * dollar_target / current_prices).astype(int)
    return positions

