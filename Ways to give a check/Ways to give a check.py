#!/bin/python3

import sys

def findPawn(board):
    point = []
    for i in range(8):
        if board[1][i] == "P":
            point.append(1)
            point.append(i)
            return point
    return point


def findBlackKing(board):
    point = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == "k":
                point.append(i)
                point.append(j)
                return point
    return point

def swap(board, x):
    aux = board[0][x]
    board[0] = "".join(board[0][0:x] + board[1][x] + board[0][x+1:8])
    board[1] = "".join(board[1][0:x] + aux + board[1][x+1:8])

def driveDiagonal(board, pawn, bKing):
    if pawn[1] == 0:
        for i in range(1, 8):
            if bKing[0] == i and bKing[1] == i:
                return True    
    if pawn[1] == 7:
        for i in range(6, -1, -1):
            if bKing[0] == i and bKing[1] == i:
                return True  
    
    for i in range(8):
        point = [i, pawn[1] - i]
        if point[1] >= 0:
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True
    
    for i in range(8):
        point = [i, pawn[1] + i]
        if point[1] <= 7:
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True

    return False

def checkQueen(board, pawn, bKing):
    #checks horizontal
    if pawn[0] == bKing[0]:
        return True
    #checks vertical
    if pawn[1] == bKing[1]:
        return True
    
    return driveDiagonal(board, pawn, bKing)

def checkKnight(board, pawn, bKing):

    y = pawn[0] + 1
    x = pawn[1] - 2

    if x >= 0:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 2
    x = pawn[0] - 1

    if x >= 0:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 1
    x = pawn[1] + 2

    if x < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 2
    x = pawn[0] + 1

    if x < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    return False



def waysToGiveACheck(board):
    # Complete this function

    #find position of the pawn to promote next
    pawn = findPawn(board)

    #find position of the black king to check the ways to check
    bKing = findBlackKing(board)

    #promote the pawn
    swap(board, pawn[1])
    pawn[0] = 0

    #check the queen
    if checkQueen(board, pawn, bKing):
        return 2
    
    #check the knight
    if checkKnight(board, pawn, bKing):
        return 1
    
    return 0


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
            board_t = str(input().strip())
            board.append(board_t)
        result = waysToGiveACheck(board)
        print(result)