#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import built-in libs
import os
from classes import World
from helpers import load_data

CWD = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    filename = os.path.join(CWD, "input", "b_read_on.txt")
    world = load_data(filename)
    world.random_algo()