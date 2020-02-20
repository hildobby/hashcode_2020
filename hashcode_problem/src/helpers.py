#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import libs
import os
from classes import Library, World


CWD = os.path.dirname(os.path.realpath(__file__))

def load_data(filename):
    """
    Loads data from txt file
    """
    
    with open(filename, 'r') as f:
        head_info = f.readline().rstrip("\n").split(" ")
        head_info = [int(info) for info in head_info]
        books, libraries, scanning = head_info
        scores_info = f.readline().rstrip("\n").split(" ")
        scores = [int(score) for score in scores_info]

        world = World(books, libraries, scanning, scores)
        lib_id, lib_info, books_info = 0, [], []
        for i, l in enumerate(f):
            line = l.rstrip("\n").split(" ")
            if i % 2 == 0:
                lib_info = [int(info) for info in line]
            else:
                books_info = [int(info) for info in line]
                world.create_library(lib_id, lib_info[0], lib_info[1], lib_info[2], books_info)
                lib_id += 1
            
    return world

if __name__ == "__main__":
    filename = os.path.join(CWD, "input", "a_example.txt")
    world = load_data(filename)
    print(world)