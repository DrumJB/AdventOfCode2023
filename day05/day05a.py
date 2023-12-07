#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:56:33 2023

@author: jachym
"""

import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()

def numbers_in_line(n):
    number = ""
    numbers = []
    for char in lines[n]:
        if char.isdigit():
            number += char
        elif number != "":
            numbers.append(int(number))
            number = ""
    return numbers

def transform(input_num, n):
    transformed_numbers = np.zeros((len(input_num)))
    transformed_bool = np.zeros((len(input_num)), dtype=bool)
    while lines[n] != "\n":
        print(n, lines[n])
        numbers = numbers_in_line(n)
        dest_range, src_range, length = numbers[0], numbers[1], numbers[2]
        for i in range(len(input_num)):
            if input_num[i] >= src_range and input_num[i] <= src_range+length:
                transformed_numbers[i] = input_num[i] + (dest_range-src_range)
                transformed_bool[i] = True
        n += 1
    for i in range(len(input_num)):
        if not transformed_bool[i]:
            transformed_numbers[i] = input_num[i]
    return transformed_numbers, n

seed_range = numbers_in_line(0)
current_t = []
for i in range(int(len(seed_range)/2)):
    for k in range(seed_range[i*2+1]):
        current_t.append(seed_range[2*i]+k)
n = 1
for i in range(7):
   current_t, n = transform(current_t, n+2)
print(current_t.min())