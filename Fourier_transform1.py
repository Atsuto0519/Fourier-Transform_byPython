#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt

# フーリエ変換の関数
def fourier_func(x, t) :
    res = []
    c_0 = 0
    
    j = 0
    for x_i in x :
        res.append(0)
        N = np.array(range(K))+1
        for n in N :
            a_n = 0
            b_n = (2*(1-(-1)**n))/(n*math.pi)
            res[j] += a_n*np.cos(n*(x_i+t)) + b_n*np.sin(n*(x_i+t))
        j += 1
    return res

# 級数を用意
x = np.arange(0, 10, 0.1)
K = 10
t = 2*math.pi

# プロット
plt.plot(x, fourier_func(x, t))
plt.show()
