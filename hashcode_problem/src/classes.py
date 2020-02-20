#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Library(object):
    def __init__(self, lib_id, tot_books, sign_days, ship_books, books):
        self.lib_id = lib_id
        self.tot_books = tot_books
        self.sign_days = sign_days
        self.ship_books = ship_books
        self.books = books


class World(object):
    def __init__(self, total_books, tot_libs, scan_days, scores):
        self.total_books = total_books
        self.tot_libs = tot_libs
        self.scan_days = scan_days
        self.scores = scores
        self.libraries = {}

    def __str__(self):
        return f"Total books: {self.total_books}\n" \
                f"Total libraries: {self.tot_libs} \nScan days: " \
                f"{self.scan_days}\n Libraries: {self.libraries}\n"

    def create_library(self, lib_id, tot_books, sign_days, ship_books, books):
        lib = Library(lib_id, tot_books, sign_days, ship_books, books)
        self.libraries[lib_id] = lib



    def average_cost_func(self):

        for library in self.libraries:

            total_cost =0

            # loop through the books and count the total cost
            for books in self.libraries[library].books:
                total_cost +=self.scores[books]

            # define the cost function for every library
            self.libraries[library].total_average_cost = (self.libraries[library].ship_books / self.libraries[library].sign_days) \
                                                     * (total_cost / self.libraries[library].tot_books)


