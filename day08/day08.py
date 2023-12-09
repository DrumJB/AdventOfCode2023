#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:29:01 2023

@author: jachym
"""

with open("input.txt", "r") as file:
    lines =  file.readlines()

class Node:
    
    def __init__(self, input, index):
        self.name = input[0:3]
        self.left = input[7:10]
        self.right = input[12:15]
        self.index = index
    
    def set_left_index(self, lines):
        self.left_index = 0
        for l in range(len(lines)):
            if lines[l][0:3]  == self.left:
                self.left_index = l-2

    def set_right_index(self, lines):
        self.right_index = 0
        for l in range(len(lines)):
            if lines[l][0:3]  == self.right:
                self.right_index = l-2
    
    def return_index(self, input):
        if input == "L":
            return self.left_index
        elif input == "R":
            return self.right_index
        return False
    
    def find_Z(self, instructions, nodes):
        instruction = 0
        index = self.index
        indeces = [self.index]
        cycle = False
        check_span = 1
        while not cycle:
            index = nodes[nodes[index].return_index(instructions[instruction])].index
            indeces.append(index)
            if len(indeces) % check_span == 0:
                for i in range(len(indeces)):
                    for j in range(len(indeces)):
                        if i != j and indeces[i]==indeces[j] and (i-j)%len(instructions):
                            cycle = True
        z = []
        for i in range(len(indeces)):
            if nodes[indeces[i]].name[-1:] == "Z":
                z.append(i)
        return z

instructions = lines[0][:-1]
nodes = []
for l in range(2, len(lines)):
    nodes.append(Node(lines[l], l-2))
indeces = []
for node in nodes:
    node.set_left_index(lines)
    node.set_right_index(lines)
    if node.name[-1:] == "A":
        indeces.append(node.index)
cycles = []
for index in indeces:
    cycles.append(nodes[index].find_Z(instructions, nodes))
print(cycles)