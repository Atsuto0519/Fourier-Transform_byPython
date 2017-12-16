#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import FFT


f = [6, 1, 3, -4]

F = FFT.DIT(f)

print("f(n)="+str(f))
print("F(n)="+str(F))
