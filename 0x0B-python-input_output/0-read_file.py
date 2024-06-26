#!/usr/bin/python3
"""Read file method"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
