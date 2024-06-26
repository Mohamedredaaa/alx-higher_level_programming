#!/usr/bin/python3
"""Read n lines of a text file (UTF8) and print it to stdout."""

def read_lines(filename="", nb_lines=0):
    with open(filename, "r", encoding="UTF-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for index in range(nb_lines):
            print(f.readline(), end="")
