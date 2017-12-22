#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import FFT


f_a = [6, 1, 3, -4]
f_b = [2, -2, -3, 7]

F_a = FFT.DIT(f_a)
F_b = FFT.DIT(f_b)

print("(a)")
print("f(n)="+str(f_a))
print("F(n)="+str(F_a))

print("(b)")
print("f(n)="+str(f_b))
print("F(n)="+str(F_b))
