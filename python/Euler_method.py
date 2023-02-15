#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:04:59 2023

@author: julio
"""

import numpy as np

def f(t,y):
    return y-t**2+1

def y_exact(t):
    return (t+1)**2-0.5*np.exp(t)   


def Euler_method(a, b, N, alpha,f):
    h=(b-a)/N
    t=a
    w=alpha
    interval=np.linspace(t,b, num=N+1, endpoint=True)
    print("t , w")
    #print(t,"  ",w)
    w_list=[]
    #w_list.append(w)
    for t in interval:
        print(t,"  ",w)
        w=w+h*f(t,w)
        w_list.append(w)
        
    return interval, np.array(w_list)


t, w=Euler_method(0,2,10,0.5,f)
y_i=y_exact(t)
diff=np.abs(w-y_i)
print(diff)
