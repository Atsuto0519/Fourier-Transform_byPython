#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import DFT

start = time.time()
N_MIN = 100
N_MAX = 10000
TIMES = 20
separation = (N_MAX - N_MIN) / (TIMES - 1)
total_time = []
for i in range(TIMES) :
    temp_N = (int)(N_MIN + i * separation)
    x = np.arange(temp_N)
    X = DFT.DFT(x)
    temp_time = time.time() - start
    total_time.append([temp_N, temp_time])
    print ("N={0},elapsed_time:{1}".format(N_MIN + i * separation, temp_time) + "[sec]")
elapsed_time = time.time() - start
print ("total_time:{0}".format(elapsed_time) + "[sec]")

# もしすべての計算が終了していたら
if (len(total_time) == TIMES) :
    np.save('total_time_DFT.npy',total_time)

total_time = np.array(total_time).T
plt.plot(total_time[0],total_time[1])
plt.savefig('DFT.png')
