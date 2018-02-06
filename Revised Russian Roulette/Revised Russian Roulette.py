#!/bin/python3

import sys

def revisedRussianRoulette(doors, length):
    # Complete this function
    temp = list(doors)

    cont_max = 0
    cont_min = 0

    size = length - 1

    for i in doors:
        if i == 1:
            cont_max += 1
    
    for i in range(size):
        if temp[i] == 1:
            cont_min += 1
            if temp[i+1] == 1:
                temp[i+1] = 0

    if temp[size] == 1:
        cont_min += 1

    result = []
    result.append(cont_min)
    result.append(cont_max)

    return result

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors, n)
    print (" ".join(map(str, result)))