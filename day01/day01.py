#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:31:22 2023

@author: jachym
"""

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0
names = ["one", "two", "three", "four", "five", 
         "six", "seven", "eight", "nine"]
for line in lines:
    numbers = []
    for i in range(len(line)):
        if line[i].isdigit():
            numbers.append(int(line[i]))
        for j in range(len(names)):
            name = names[j]
            length = len(name)
            if i <= len(line)-length:
                if line[i:i+length] == name:
                    numbers.append(j+1)
    first_digit = numbers[0]
    last_digit = numbers[-1]
    number = first_digit*10 + last_digit
    sum += number
print(sum)