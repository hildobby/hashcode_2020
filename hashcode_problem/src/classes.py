#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import random
from collections import OrderedDict


class Library(object):
    def __init__(self, lib_id, tot_books, sign_days, ship_books, books):
        self.lib_id = lib_id
        self.tot_books = tot_books
        self.sign_days = sign_days
        self.ship_books = ship_books
        self.books = books
        self.total_cost = 0


class World(object):
    def __init__(self, total_books, tot_libs, scan_days, scores):
        self.total_books = total_books
        self.tot_libs = tot_libs
        self.scan_days = scan_days
        self.scores = scores
        self.libraries = {}
        self.lib_books = OrderedDict()
        self.chosen_books = OrderedDict()
        self.all_chosen_books = set()
        self.current_score = 0

    def __str__(self):
        return f"Total books: {self.total_books}\n" \
                f"Total libraries: {self.tot_libs} \nScan days: " \
                f"{self.scan_days}\n Libraries: {self.libraries}\n"

    def create_library(self, lib_id, tot_books, sign_days, ship_books, books):
        lib = Library(lib_id, tot_books, sign_days, ship_books, books)
        self.libraries[lib_id] = lib

    def random_algo(self):

        counter = 0
        libs = copy.deepcopy(self.libraries)

        # Randomly select libraries for signing process and determine total
        # books scanned
        while counter < self.scan_days and libs:
            lib = random.choice(list(libs.values()))
            counter += lib.sign_days
            if counter > self.scan_days:
                break
            tot_books = lib.ship_books * (self.scan_days - counter)
            if tot_books > lib.tot_books:
                tot_books = lib.tot_books
            self.lib_books[lib.lib_id] = tot_books
            libs.pop(lib.lib_id)

        for lib_id, tot_book in self.lib_books.items():
            sample = random.sample(self.libraries[lib_id].books, k=tot_book)
            self.chosen_books[lib_id] = sample

            for s in sample:
                self.all_chosen_books.add(s)

    def greedy_algo_with_heuristic(self):
        self.average_cost_func()
        self.sort_libraries()

        counter = 0
        for library in self.libraries_list:
            counter += library.sign_days
            if counter > self.scan_days:
                break
            tot_books = library.ship_books * (self.scan_days - counter)
            if tot_books > library.tot_books:
                tot_books = library.tot_books
            self.lib_books[library.lib_id] = tot_books

        for lib_id, tot_book in self.lib_books.items():
            sample = random.sample(self.libraries[lib_id].books, k=tot_book)
            self.chosen_books[lib_id] = sample

            for s in sample:
                self.all_chosen_books.add(s)


    def determine_score(self):
        self.current_score = 0
        for book in self.all_chosen_books:
            self.current_score += self.scores[book]
        print("The score is: ", self.current_score)

    def average_cost_func(self):

        for library in self.libraries:

            total_cost =0

            # loop through the books and count the total cost
            for books in self.libraries[library].books:
                self.libraries[library].total_cost += self.scores[books]

            # define the cost function for every library
            self.libraries[library].total_average_cost = (self.libraries[library].ship_books / self.libraries[library].sign_days) \
                                                     * (self.libraries[library].total_cost / self.libraries[library].tot_books)



    def sort_libraries(self):

        self.libraries_list = [i for i in self.libraries.values()]

        self.libraries_list.sort(key=lambda x: x.total_average_cost, reverse=True)

    def reset(self):
        self.lib_books = OrderedDict()
        self.chosen_books = OrderedDict()
        self.all_chosen_books = set()
        self.current_score = 0
