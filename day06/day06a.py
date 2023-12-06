#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:51:44 2023

@author: jachym
"""

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

times = numbers_in_line(0)
distances = numbers_in_line(1)

total = 1
for time in range(len(times)):
    win = 0
    for t in range(times[time]):
        holding = t
        travelling = times[time]-t
        distance = holding * travelling
        if distance > distances[time]:
            win += 1
    total *= win
print(total)