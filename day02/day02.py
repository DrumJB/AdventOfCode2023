#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:15:13 2023

@author: jachym
"""

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

with open("input.txt", "r") as file:
    lines = file.readlines()

power_sum = 0
for line in lines:
    game_number = 0
    blue = 0
    red = 0
    green = 0
    max_blue = 0
    max_red = 0
    max_green = 0
    number = ""
    possible = True
    for i in range(len(line)-1):
        if line[i].isdigit():
            number += line[i]
        else:
            if number != "":
                if line[i+1] == "b" and int(number) > max_blue:
                    blue = int(number)
                    max_blue = blue
                    number = ""
                elif line[i+1] == "r" and int(number) > max_red:
                    red = int(number)
                    max_red = red
                    number = ""
                elif line[i+1] == "g" and int(number) > max_green:
                    green = int(number)
                    max_green = green
                    number = ""
                else: 
                    game_number = int(number)
                    number = ""
    power_sum += blue * green * red
print(power_sum)