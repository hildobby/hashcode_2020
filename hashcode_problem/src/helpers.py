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
            if l == "\n":
                break
            line = l.rstrip("\n").split(" ")
            if i % 2 == 0:
                lib_info = [int(info) for info in line]
                print(lib_info)
            else:
                books_info = [int(info) for info in line]
                world.create_library(lib_id, lib_info[0], lib_info[1], lib_info[2], books_info)
                lib_id += 1

            
    return world

def write_data(filename, world):
    """
    Write data to txt file
    """
    # Writes to the output file
    with open(filename, 'w') as f:
        f.write("{}\n".format(str(len(world.lib_books))))
        for i in world.lib_books.keys():
            f.write("{} {}\n".format(str(i), str(len(world.chosen_books[i]))))
            f.write("{}\n".format(' '.join(map(str,world.chosen_books[i]))))

if __name__ == "__main__":
    text_name = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]
    for f_name in text_name:
        input_filename = os.path.join(CWD, "input", "{}.txt".format(f_name))
        world = load_data(input_filename)
        world.random_algo()
        output_filename = os.path.join(CWD, "output", "{}.txt".format(f_name))
        write_data(output_filename, world)
        print(world)
        world.average_cost_func()

        world.sort_libraries()


