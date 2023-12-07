#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 07:15:29 2023

@author: jachym
"""
from copy import deepcopy as dc

with open("input.txt", "r")  as file:
    lines = file.readlines()

hands = []
for line in lines:
    line = [line.split(" ")[0], int(line.split(" ")[1][:-1])]
    hands.append(line)

def card_value(card):
    values = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    for i in range(len(values)):
        if card == values[i]:
            return i
    print("Er 1", card)

def five_of_kind(hand):
    final = 0
    for x in hand:
        if x != 0:
            final = x
    same = True
    for h in hand:
        if h != final and h != 0:
            same = False
    return same

def four_of_kind(hand):
    final_1 = 0
    final_2 = 0
    for x in hand:
        if x != 0 and final_1 == 0:
            final_1 = x
        if x != 0 and final_1 != 0:
            final_2 = x
    same_x, same_y = 0, 0
    for h in hand:
        if h == final_1 or h == 0:
            same_x += 1
        if h == final_2 or h == 0:
            same_y += 1
    if same_x == 4 or same_y == 4:
        return True
    else:
        return False

def full_house(hand):
    types = []
    jokers = 0
    for h in hand:
        a = True
        if h == 0:
            a = False
            jokers += 1
        for t in types: 
            if h == t[0] and h!=0:
                t[1] += 1
                a = False
        if a:
            types.append([h, 1])
            
    two, three = False, False
    if jokers == 0:
        for t in types:
            if t[1] == 2:
                two = True
            if t[1] == 3:
                three = True
        if two and three: 
            return True 
        else: 
            return False
    elif jokers == 1:
        all_2 = True
        one = False
        three = False
        for t in types:
            if t[1] != 2:
                all_2 = False
            if t[1] == 1:
                one = True
            if t[1] == 3:
                three = True
        if all_2 or (one and three):
            return True
    elif jokers == 2:
        if len(types) == 1:
            return True
        one = False
        two = False
        for t in types:
            if t[1] == 1:
                one = True
            if t[1] == 2:
                two = True
        if one and two:
            return True
    return False
    
def three_pair(hand):
    types = []
    jokers = 0
    for h in hand:
        a = True
        for t in types: 
            if h == t[0]:
                t[1] += 1
                a = False
        if a:
            types.append([h, 1])
        if h == 0:
            jokers += 1
    for t in types:
        if (t[1]+jokers) == 3:
            return True
    return False

def two_pair(hand):
    types = []
    jokers = 0
    for h in hand:
        a = True
        for t in types: 
            if h == t[0]:
                t[1] += 1
                a = False
        if a:
            types.append([h, 1])
        if h == 0:
            jokers += 1
    if jokers == 0:
        if len(types) == 3: return True
    if jokers == 1:
        if len(types) == 4: return True
    if jokers > 1:
        return True
    else:
        return False

def one_pair(hand):
    types = []
    jokers = 0
    for h in hand:
        a = True
        for t in types: 
            if h == t[0]:
                t[1] += 1
                a = False
        if a:
            types.append([h, 1])
        if h == 0:
            jokers += 1
    if jokers == 0:
        if len(types) == 4: return True
    if jokers == 1: 
        if len(types) == 5: return True
    return False

def hand_value(hand):
    arr = []
    for char in hand:
        arr.append(card_value(char))
    value = 0
    if five_of_kind(arr):
        value = 360
    elif four_of_kind(arr):
        value = 300
    elif full_house(arr):
        value = 240
    elif three_pair(arr):
        value = 180
    elif two_pair(arr):
        value = 120
    elif one_pair(arr):
        value = 60
    return value

for hand in hands:
    hand.append(hand_value(hand[0]))
hands = sorted(hands, key=lambda x: x[2])
sorted = False
while not sorted:
    own_sort = True
    for h in range(len(hands)):
        for i in range(len(hands)):
            for x in range(5,0,-1):
                if hands[h][0][:x] == hands[i][0][:x] and hands[h][2] == hands[i][2] and h != i:
                    if card_value(hands[h][0][x]) > card_value(hands[i][0][x]):
                        if h < i:
                            own_sort = False
                            temp = dc(hands[h])
                            hands[h] = hands[i]
                            hands[i] = temp
            if card_value(hands[h][0][0]) > card_value(hands[i][0][0]) and hands[h][2] == hands[i][2]:
                if h < i:
                    own_sort = False
                    temp = dc(hands[h])
                    hands[h] = hands[i]
                    hands[i] = temp                
    if own_sort:
        sorted = True
result = 0
for s in range(len(hands)):
    result += (s+1) * hands[s][1]
print(result)