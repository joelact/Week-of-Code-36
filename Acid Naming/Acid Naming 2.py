#!/bin/python3

import sys

def acidNaming(acid_name):
    # Complete this function
    prefix = "hydro"
    sufix = "ic"

    if acid_name.endswith(sufix) and acid_name.startswith(prefix):
        return "non-metal acid"
    if acid_name.endswith(sufix):
        return "polyatomic acid"
    return "not an acid"
    

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)
