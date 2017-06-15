#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt

# フーリエ変換の関数
def fourier_func(x, t, l) :
    res = []
    c_0 = 0
    
    j = 0
    for x_i in x :
        res.append(0)
        N = np.array(range(K))+1
        for n in N :
            a_n = 0
            b_n = (-2*((-1)**n))/(n*math.pi)
            res[j] += b_n*np.sin((n*math.pi*x_i)/l)
        j += 1
    return res

# 級数を用意
x = np.arange(0, 10, 0.1)
K = 50
t = 0
T = 4

# プロット
plt.plot(x, fourier_func(x, t, T/2))
plt.show()
