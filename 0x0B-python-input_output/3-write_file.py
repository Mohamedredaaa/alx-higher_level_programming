#!/usr/bin/python3
"""Write to a file method"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
