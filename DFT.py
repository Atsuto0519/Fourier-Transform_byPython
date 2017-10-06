#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def DFT(x) :
    """
    概要:　   
    @param x:
    @return  
    """
    
    N = len(x)     
    W_N = []
    X=np.zeros(N,dtype=complex)
    for k in range(N):
        re=0
        im=0
        for n in range(N):
            n_comp = complex(np.cos(2*np.pi*k*n/N), -np.sin(2*np.pi*k*n/N))
            W_N.append(n_comp)
            re+=n_comp.real*x[n]
            im+=n_comp.imag*x[n]
        X[k]=complex(re,im)
    return X, np.array(W_N).reshape(N, N).tolist()

def IDFT(X) :
    """
    概要:　    
    @param X: 
    @return   
    """

    N = len(X)
    W_N = []
    x=np.zeros(N,dtype=complex)
    for k in range(N):
        re=0
        im=0
        for n in range(N):
            n_comp = complex(np.cos(2*np.pi*k*n/N), np.sin(2*np.pi*k*n/N))
            W_N.append(n_comp)
            tmp=n_comp*X[n]/N
            re+=tmp.real
            im+=tmp.imag
        x[k]=complex(re,im)
    return x, np.array(W_N).reshape(N, N).tolist()
