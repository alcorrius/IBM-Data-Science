#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:38:44 2024

@author: vdotsenko
"""

import numpy as np

a = np.array([0,1,2,3,4])
print(type(a), a.dtype, a.size, a.ndim, a.shape)

u = np.array([1,0])
v = np.array([0,1])
z = u + v
print(z)

z2 = z*2
print(z2)

#2D
a = np.array([[11,12,13], [21,22,23],[31,32,33]])
print(a.ndim, a.shape, a.size)

X = np.array([-1,1])
Y = np.array([1,1])
print(np.dot(X,Y))

X = np.array([[1,0],[0,1]])
Y = np.array([[2,2],[2,2]])
print(np.dot(X,Y))