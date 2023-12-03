#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:34:20 2023

@author: jachym
"""

with open("input.txt", "r") as file:
    lines = file.readlines()

gear_sum = 0
possible_gear = []
for i in range(len(lines)):
    num_length = 0
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            num_length += 1
        else:
            if num_length > 0:
                number = int(lines[i][j-num_length:j])
                # evaluating parts of engine
                counted = False
                for x in range(i-1, i+2):
                    for y in range(j-num_length-1, j+1):
                        try:
                            if lines[x][y]=="*":
                                found = False
                                for g in possible_gear:
                                    if g[1] == x and g[2]==y:
                                        gear_sum += g[0]*number
                                if not found:
                                    possible_gear.append([number, x, y])
                        except IndexError:
                            pass
                num_length = 0
print(gear_sum)
                            