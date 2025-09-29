#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import glob
import datetime

from mwc.counter import count_words_in_markdown

# Lazy terminal colouring
time_col = "\033[0;35m"
chapter_col = "\033[0;36m"
reset_col = "\033[0m"
other_md_col = "\033[0;37m"

def main():
    
    argument = ''

    if sys.version_info < (3,):
        print('Python 3 is required. You are using Python 2. You should probably run this script as follows and remember to run from the parent directory:')
        print('python3 scripts/wc.py')
        sys.exit(1)
    
    if len(sys.argv) > 1:
        argument = sys.argv[1]
    else:
        print("No command line argument provided.")
        sys.exit(1)

    file = argument
    try:
        with open(file, 'r', encoding='utf8') as f:
            count = count_words_in_markdown(f.read())
            print("\n")
            print("Total words: ", count)
    except FileNotFoundError:
        print("File to count not found.")
        print("ensure you are calling this script with a path to the file you want counted")
        print("For example: \n python .scripts/wc.py portfolio/report.md")

if __name__ == '__main__':
    main()