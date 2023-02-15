#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:04:59 2023

@author: julio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# function of t and y, this is the function in y'=f(t,y)
def f(t,y):
    return y-t**2+1

# exact solution of y'=f(x,y)
def y_exact(t):
    return (t+1)**2-0.5*np.exp(t)   


# quick implementation of the Euler Method
def Euler_method(a, b, N, alpha,f): 
    h=(b-a)/N
    w=alpha
    interval=np.linspace(a,b, num=N+1, endpoint=True)
    print("t , w")
    w_list=[]
    for t in interval:
        print(t,"  ",w)
        w_list.append(w)
        w=w+h*f(t,w)
        
        
    return interval, np.array(w_list)


t, w=Euler_method(0,2,10,0.5,f)
y_i=y_exact(t)
diff=np.abs(w-y_i)
print(diff)
plt.plot(t, diff)

plt.ylabel("Error del Método Euler")
plt.xlabel("t")
plt.show()
table=pd.DataFrame(np.array([t,w,y_i,diff]).T,columns=['t','w_i','y_i','|y_i-w_i|'])