'''
TicTacToe AI using minimax algorithm through depth first search
and alpha-beta pruning to optimize the program
By: Oren Leung
'''
from os import system
import math
import time
import platform

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')

def printBoard(board):
    print("     |     |   ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("     |     |   ")
    print("-----------------")
    print("     |     |   ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("     |     |   ")
    print("-----------------")
    print("     |     |   ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("     |     |   ")
    return

def empty(board):
    emptyCell = []
    for i in range(0,9):
        if board[i] == " ":
            emptyCell.append(i)
    return emptyCell
    
def boardWin(symbol,board):
    for i in range(0,3):
        if board[0+i*3] == symbol and board[1+i*3] == symbol and board[2+i*3] == symbol:
            return True
    for j in range(0,3):
        if board[0+j] == symbol and board[3+j] == symbol and board[6+j] == symbol:
            return True
    if board[4] == symbol:
        if board[0] == symbol and board[8] == symbol:
            return True
        elif board[2] == symbol and board[6] == symbol:
            return True
    else:
        return False

def insertPiece(board,move,symbol):
    board[move] = symbol
    return board

def getScore(depth):
    score = 1
    for i in range(10-depth,0,-1):
        score *= i
    return score

def minimax(state, intial, depth, symbol,alpha,beta):
    if boardWin("X",state):
        return getScore(depth)
    elif boardWin("O",state):
        return -getScore(depth)
    elif depth == 9:
        return 0
  
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"

    idealPath = 0
    maxEval = -math.inf
    minEval = math.inf

    if symbol == "X":
        for cell in empty(state):
            newState = state.copy()
            newState = insertPiece(newState,cell,"X")
            eval = minimax(newState,intial,depth+1,"X",alpha,beta)
            if depth == intial:
                if eval > maxEval:
                    idealPath = cell
            maxEval = max(maxEval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        if depth == intial :
            return idealPath
        else:
            return maxEval
    else:
        for cell in empty(state):
            newState = state.copy()
            newState = insertPiece(newState,cell,"O")
            eval = minimax(newState,intial,depth+1,"O",alpha,beta)
            minEval = min(minEval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

def compMove(board):
    depth = len(empty(board))
    initalLayer = 9 - depth
    if depth == 0:
        return
    else:
        cMove = minimax(board,initalLayer,initalLayer,"O",-math.inf,math.inf)
        insertPiece(board,cMove,"X")
        clean()
        print("Computer's Move")
        printBoard(board)
        return

def playerMove(board):
    emptyCell = empty(board)
    while True:
        pMove = int(input("Please Enter a Move: ")) - 1
        if pMove not in emptyCell:
            print("Please Enter a Valid Move!")
        else:
            break
    insertPiece(board,pMove,"O")
    clean()
    print("Human's Move")
    printBoard(board)
    return

def main():
    play = input("Do you want to play Tic Tac Toe with me?(Yes/No): ").lower()
    humanCounter = 0
    comCounter = 0
    clean()
    print("Use your number pad to enter your move like the following example")
    printBoard(["1","2","3","4","5","6","7","8","9"])
    time.sleep(4)
    clean()
    while play == "yes":
        board = [" "," "," "," "," "," "," "," "," "]
        printBoard(board)
        while len(empty(board)) > 0:
            playerMove(board)
            compMove(board)
            if boardWin("O",board):
                print("Human Won!")
                humanCounter += 1
                break
            elif boardWin("X",board):
                print("Computer Rule!")
                comCounter += 1
                break
            elif len(empty(board)) == 0:
                print("Tie")
                break
        print("Computer Wins: " + str(comCounter))
        print("Human Wins: " + str(humanCounter))
        play = input("Do you want to play again?(Yes/No): ").lower()
    print("Thanks for trying to beat me!")

if __name__ == "__main__":
    main()
