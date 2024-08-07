#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:42:00 2024

@author: vdotsenko
"""

file = open("file1.txt","r")

file.close()

with open("file1.txt", "r") as file1:
    file_stuff = file1.readline(5)
    print(file_stuff)
    file_stuff = file1.readline(5)
    print(file_stuff)
    file_stuff = file1.readline()
    print(file_stuff)
    
    
file = open("file2.txt", "w")
file.write("New Line\n")
file.close()

Lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file2.txt", "a") as file2:
    for line in Lines:
        file2.write(line)