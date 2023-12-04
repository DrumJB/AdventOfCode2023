#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:44:31 2023

@author: jachym
"""

with open("input.txt", "r") as file:
    lines = file.readlines()

def find_points(line):
    number = ""
    numbers = []
    other_numbers = []
    winning_numbers = []
    wins = 0
    win = True
    for j in range(len(lines[line])):
        if lines[line][j].isdigit():
            number += lines[line][j]
        else:
            if number != "":
                numbers.append(int(number))
                if not win:
                    other_numbers.append(int(number))
                number = ""
        if lines[line][j] == "|":
            winning_numbers = numbers[1:]
            win = False
    for onum in other_numbers:
        for wnum in winning_numbers:
            if onum == wnum:
                wins += 1
    return wins

def find_points_card(line):
    points = find_points(line)
    cards = points
    if points > 0:
        for j in range(1, points+1):
            cards += find_points_card(line+j)
    return cards

total_cards = len(lines)
for i in range(len(lines)):
   total_cards += find_points_card(i)
   pass
            
print(total_cards)
#print(find_points_card(0))