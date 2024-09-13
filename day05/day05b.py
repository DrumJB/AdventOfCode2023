#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:56:55 2023

@author: jachym
"""

# I had to choose completly another way :-(


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

def ranges(n):
    rng = []
    while lines[n] != "\n":
        numbers = numbers_in_line(n)
        dest_range, src_range, length = numbers[0], numbers[1], numbers[2]
        out_range = [dest_range, dest_range+length]
        in_range = [src_range, src_range+length]
        rng.append([in_range, out_range])
        n += 1
    rng.sort(key=lambda x: x[0][0])
    return rng

def merge_ranges(rng_1, rng_2):
    result = []
    for r1 in rng_1:
        common = []
        for r2 in rng_2:
            if r2[0][1] >= r1[1][0] and r2[0][1] <= r1[1][1] and r2[0][0] <= r1[1][0]:
                interval = [[r1[0][0], r1[0][1] - (r1[1][1]-r2[0][1])],
                            [r2[1][0] + (r1[1][0]-r2[0][0]), r2[1][1]]]
                if interval not in common: common.append(interval)
            if r2[0][1] >= r1[1][1] and r2[0][0] >= r1[1][0] and r2[0][0] <= r1[1][1]:
                interval = [[r1[0][0] + (r2[0][0]-r1[1][0]), r1[0][1]],
                            [r2[1][0], r2[1][1] - (r2[0][1]-r1[1][1])]]
                if interval not in common: common.append(interval)
            if r2[0][1] <= r1[1][1] and r2[0][0] >= r1[1][0]:
                interval = [[r1[0][0] - (r2[0][0]-r1[1][0]), r1[0][1] - (r1[1][1]-r2[0][1])],
                            [r2[1][0], r2[1][1]]]
                if interval not in common: common.append(interval)
            
                
        result.extend(common)
    return result

maps = [3, 7, 12, 18, 22, 27, 31]
print(merge_ranges([[[4,8], [1,5]]], [[[3,4], [6,7]], [[1,2], [8,9]]]))