#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import FFT

start_time = time.time()
M_MIN = 1
M_MAX = 100
total_time = np.zeros([int(M_MAX-M_MIN+1),2])
for i in range(M_MIN, M_MAX+1) :
    temp_N = int(np.power(2,i))
    x = np.arange(temp_N)
    X = FFT.DIT(x)
    temp_time = time.time() - start_time
    total_time[i-M_MIN] = [i, temp_time]
    print ("N={0},elapsed_time:{1}".format(temp_N, temp_time) + "[sec]")
elapsed_time = time.time() - start_time
print ("total_time:{0}".format(elapsed_time) + "[sec]")

# もしすべての計算が終了していたら
if (len(total_time) == M_MAX) :
    np.save('total_time_FFT.npy',total_time)

total_time = np.array(total_time).T
plt.plot(total_time[0],total_time[1])
plt.savefig('FFT.png')
