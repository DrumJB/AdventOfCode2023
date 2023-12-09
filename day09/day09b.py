#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:35:12 2023

@author: jachym
"""

with open("input.txt", "r") as file:
    lines = file.readlines()

def prediction(input):
    null = False
    extrapolations = [input]
    step = 0
    while not null:
        new_extra = []  
        for a in range(len(extrapolations[step])-1, 0, -1):
            new_extra.append(extrapolations[step][a]-extrapolations[step][a-1])
        new_extra.reverse()
        extrapolations.append(new_extra)
        if all([n == 0 for n in new_extra]):
            null = True
        step +=1
    extrapolations[-1].insert(0, 0)
    for e in range(len(extrapolations)-2, -1, -1):
        extrapolations[e].insert(0, extrapolations[e][0]-extrapolations[e+1][0])
    return extrapolations[0][0]

prediction_sum = 0
for line in lines:
    prediction_sum += prediction([int(i) for i in line.split(" ")])
    pass
print(prediction_sum)