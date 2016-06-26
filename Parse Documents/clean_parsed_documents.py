"""
This program cleans the parsed documents and removes any unncessary information
"""
import re

with open("../Files and Other codes/parseExample2.txt", "r") as parse_out:
    contents = parse_out.read()
    # before, after = contents.split("Related Links") #split the contents
    # before, after = contents.split("Guides and help")
    before, after = contents.split("Did you find what you were looking for?")
    # before, after = contents.split("Related services and information")
    before = before.lstrip()
    print before
    with open("Supplementary Retirement Benefit.txt", "w") as doc_out:
        doc_out.write(before)

