#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def BIT_REVERSE(i,N) :
    """
    概要:　   高速フーリエ変換のための並び替えビット反転
    @param i:変換前信号i番目
    @return :変換後信号i番目
    """

    res = 0

    N-=1
    while (N > 0) :
        res = (res << 1) | (i & 1)

        N >>= 1
        i >>= 1

    return res

def DIT(x) :
    """
    概要:　   時間間引き高速フーリエ変換
    @param x:元信号
    @return :フーリエ変換信号
    """

    # Decimation-In-Time FFT
    N = len(x)

    # Calc to use W
    W = [complex(np.cos(2*np.pi*i/N), -np.sin(2*np.pi*i/N)) for i in range(int(N/2))]

    # set init values with bit reversed
    X = [x[BIT_REVERSE(i,N)] for i in range(N)]
    X = np.array(X,dtype=complex)

    # butterfly diagrams
    b = 2
    while (b <= N) :
        i = 0
        count = 0
        split = N/b
        while (i < N) :
            if (i % b < b/2) :
                k = int(i + b/2)
                temp = X[i]
                X[k] *= W[int(count*split)]
                X[i] += X[k]
                X[k] = temp - X[k]
                count+=1
                count%=int(b/2)
            i+=1
        b <<= 1

    return X

def DIF(x) :
    """
    概要:　   周波数間引き高速フーリエ変換
    @param X:フーリエ変換信号
    @return :元信号
    """

    # Decimation-In-Frequency FFT
    x = list(x)
    N = len(x)

    # Calc to use W
    W = [complex(np.cos(2*np.pi*i/N), -np.sin(2*np.pi*i/N)) for i in range(int(N/2))]
    x = x.copy()

    # butterfly diagrams
    b = N
    while (b > 1) :
        i = 0
        count = 0
        split = N/b
        while (i < N) :
            if (i % b < b/2) :
                k = int(i + b/2)
                temp = x[i]
                x[i] += x[k]
                x[k] = temp - x[k]
                x[k] *= W[int(count*split)]
                count+=1
                count%=int(b/2)
            i+=1
        b >>= 1

    X = np.array(x,dtype=complex)
    for i in range(N) :
        X[i] = x[BIT_REVERSE(i,N)]

    return X
