#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:52:07 2023

@author: jachym
"""
import numpy as np
import math as m

with open("input.txt", "r") as file:
    lines = file.readlines()

time = ""
for char in lines[0]:
    if char.isdigit():
        time += char
time = int(time)

dist = ""
for char in lines[1]:
    if char.isdigit():
        dist += char
dist = int(dist)

# solve qudratic equation
t1 = (time + np.sqrt(time**2 - 4*dist))/2
t2 = (time - np.sqrt(time**2 - 4*dist))/2
print(abs(int(t1)-int(t2)))