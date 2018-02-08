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


def findPiece(board, piece):
    point = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == piece:
                point.append(i)
                point.append(j)
                return point
    return -1

def swap(board, x):
    aux = board[0][x]
    board[0] = "".join(board[0][0:x] + board[1][x] + board[0][x+1:8])
    board[1] = "".join(board[1][0:x] + aux + board[1][x+1:8])

def checkBishop(bishop, bKing, bPiece):

    for i in range(8):
        point = [bishop[0] - i, bishop[1] - i]
        if point[1] >= 0 and point[1] < 8 and point[0] >= 0 and point[1] < 8:
            if point[0] == bPiece[0] and point[1] == bPiece[1]:
                return False
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True
        else:
            break
    
    for i in range(8):
        point = [bishop[0] - i, bishop[1] + i]
        if point[1] >= 0 and point[1] < 8 and point[0] >= 0 and point[1] < 8:
            if point[0] == bPiece[0] and point[1] == bPiece[1]:
                return False
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True
        else:
            break
    
    for i in range(8):
        point = [bishop[0] + i, bishop[1] - i]
        if point[1] >= 0 and point[1] < 8 and point[0] >= 0 and point[1] < 8:
            if point[0] == bPiece[0] and point[1] == bPiece[1]:
                return False
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True
        else:
            break

    for i in range(8):
        point = [bishop[0] + i, bishop[1] + i]
        if point[1] >= 0 and point[1] < 8 and point[0] >= 0 and point[1] < 8:
            if point[0] == bPiece[0] and point[1] == bPiece[1]:
                return False
            if point[0] == bKing[0] and point[1] == bKing[1]:
                return True
        else:
            break

    return False

def checkRook(rook, bKing, bPiece):
    if bPiece[0] == rook[0]:
        return False
    
    if bPiece[1] == rook[1]:
        return False

    #checks horizontal
    if rook[0] == bKing[0]:
        return True
    #checks vertical
    if rook[1] == bKing[1]:
        return True
    
    return False


def checkQueen(queen, bKing, bPiece):
    if checkRook(queen, bKing, bPiece):
        return True
    
    return checkBishop(queen, bKing, bPiece)

#cheks all possible posittions of the kight
def checkKnight(pawn, bKing):

    y = pawn[0] + 1
    x = pawn[1] - 2

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 2
    x = pawn[1] - 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    y = pawn[0] - 1
    x = pawn[1] - 2

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] - 2
    x = pawn[1] - 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 1
    x = pawn[1] + 2

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] + 2
    x = pawn[1] + 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    y = pawn[0] - 1
    x = pawn[1] + 2

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = pawn[0] - 2
    x = pawn[1] + 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    return False

#checks all possible moves of the king
def checkKing(king, bKing):
    y = king[0] + 1
    x = king[1]

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = king[0] + 1
    x = king[1] - 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    y = king[0]
    x = king[1] - 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = king[0] - 1 
    x = king[1] - 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    y = king[0] - 1
    x = king[1]

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = king[0] - 1
    x = king[1] + 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True

    y = king[0]
    x = king[1] + 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    y = king[0] + 1 
    x = king[1] + 1

    if x >= 0  and x < 8 and y >= 0 and y < 8:
        if bKing[0] == y and bKing[1] == x:
            return True
    
    return False


def decideWay(cont, bKing):
    point = [-1, -1]

    #find other white pieces position if they exits
    wQueen = findPiece(board, "Q")
    
    #checks white queen
    if wQueen != -1:
        if checkQueen(wQueen, bKing, point):
            cont += 1
            return cont

    wRook = findPiece(board, "R")

    #checks white rook
    if wRook != -1:
        if checkRook(wRook, bKing, point):
            cont += 1
            return cont
    
    wBishop = findPiece(board, "B")
    
    #checks white bishop
    if wBishop != -1:
        if checkBishop(wBishop, bKing, point):
            cont += 1
            return cont

    wKinght = findPiece(board, "N")

    if wKinght != -1:
        if checkKnight(wKinght, bKing):
            cont += 1
            return cont
    
    return cont

def waysToGiveACheck(board):
    # Complete this function
    cont = 0

    #find position of the pawn to promote next
    pawn = findPawn(board)

    #find position of the black king to check the ways to check
    bKing = findPiece(board, "k")

    #find position of the white king
    wKing = findPiece(board, "K")

    #checks if the white king checks the black king
    if checkKing(wKing, bKing):
        cont += 1

    #promote the pawn
    swap(board, pawn[1])
    pawn[0] = 0
    
    #find other black pieces position if they exits
    bQueen = findPiece(board, "q")

    if bQueen != -1:
        if checkQueen(pawn, bKing, bQueen):
            return cont + 2
        else:
            return cont
        
        if checkKnight(pawn, bKing):
            return cont + 1
        else:
            return cont

    bRook = findPiece(board, "r")

    if bRook != -1:
        if checkQueen(pawn, bKing, bRook):
            return cont + 2
        else:
            return cont
        
        if checkKnight(pawn, bKing):
            return cont + 1
        else:
            return cont
    
    bBishop = findPiece(board, "b")

    if bBishop != -1:
        if checkQueen(pawn, bKing, bBishop):
            return cont + 2
        else:
            return cont
        
        if checkKnight(pawn, bKing):
            return cont + 1
        else:
            return cont


    bKinght = findPiece(board, "n")

    if bKinght != -1:
        if checkQueen(pawn, bKing, bKinght):
            return cont + 2
        else:
            return cont
        
        if checkKnight(pawn, bKing):
            return cont + 1
        else:
            return cont

    #cont other checks
    cont = decideWay(cont, bKing)

    point = [-1, -1]

    #check the queen
    if checkQueen(pawn, bKing, point):
        return cont + 2
    
    #check the knight
    if checkKnight(pawn, bKing):
        return cont + 1
    
    return cont


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
            board_t = str(input().strip())
            board.append(board_t)
        result = waysToGiveACheck(board)
        print(result)