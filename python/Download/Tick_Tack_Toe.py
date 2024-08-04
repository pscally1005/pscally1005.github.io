from array import array
from os import system
import random
import getch

# 2 player or 1 player vs computer
def mode() :
    system('clear')
    print('\nWelcome to Tic-Tac-Toe!')
    print('\nWould you like to play 1P or 2P?', end = '')
    print('\nPlease enter either "1" or "2": ', end = ' ')
    m = getch.getch()
    while (m.isnumeric() == False) or (int(m) < 1) or (int(m) > 2) :
        system('clear')
        print('\nWelcome to Tic-Tac-Toe!')
        print('\nERROR: Mode type invalid', end = '')
        print('\nWould you like to play 1P or 2P?', end = '')
        print('\nPlease enter either "1" or "2": ', end = ' ')
        m = getch.getch()
    return m

# user inputs size of the board
def input_size(m) :
    system('clear')
    print('\nWelcome to Tic-Tac-Toe!\n')
    print(str(m) + 'P mode selected')
    print('\nPlease Enter a Board Size from 3 to 9: ', end = ' ')
    size = getch.getch()
    while (size.isnumeric() == False) or (int(size) < 3) or (int(size) > 9) :
        system('clear')
        print('\nWelcome to Tic-Tac-Toe!\n')
        print(str(m) + 'P mode selected')
        print('\nERROR: Board size invalid', end = '')
        print('\nPlease Enter a Board Size from 3 to 9: ', end = ' ')
        size = getch.getch()
    return size

# prints the board every time a move is made
def board(b, m) :
    system('clear')
    print('\nWelcome to Tic-Tac-Toe!\n')
    print(str(m) + 'P mode selected')
    print(str(len(b)) + 'x' + str(len(b)) + ' board selected\n')

    if int(m) == 1 :
        print('You win by connecting ' + str(len(b)) + ' X\'s in a row')
        print('You lose if the computer connects ' + str(len(b)) + ' O\'s in a row\n')
    elif int(m) == 2 :
        print('P1 wins by connecting ' + str(len(b)) + ' X\'s in a row.')
        print('P2 wins by connecting ' + str(len(b)) + ' O\'s in a row\n')

    print('+', end = '')
    for x in b :    print('-', end = '')
    print('+')

    i = 0
    for x in b :
        j = 0
        print('|', end = '')
        for y in b[i] :
            print(b[i][j], end = '')
            j = j+1
        i = i+1
        print('|')
    
    print('+', end = '')
    for x in b :    print('-', end = '')
    print('+')

# code for user to input a move
def user(b, m, symbol) :
    if int(m) == 1 :    print('\nPlease enter a location for X (ex: 0,0):', end = ' ')
    elif int(m) == 2 :  print('\nPlease enter a location for ' + str(symbol) + ' (ex: 0,0) :', end = ' ')
    move = input()

    while (len(move) != 3) \
        or (move[1] != ',') \
        or (move[0].isnumeric() == False or move[2].isnumeric() == False) \
        or (int(move[0]) < 0 or int(move[0]) > len(b)-1) \
        or (int(move[2]) < 0 or int(move[2]) > len(b)-1) \
        or b[int(move[0])][int(move[2])] != ' ' :

        board(b, m)
        print('\nERROR: Input is invalid', end = '')
        if int(m) == 1 :    print('\nPlease enter a location for X (ex: 0,0):', end = ' ')
        elif int(m) == 2 :  print('\nPlease enter a location for ' + str(symbol) + ' (ex: 0,0) :', end = ' ')
        move = input()

    [i, j] = [move[0], move[2]]
    b[int(i)][int(j)] = symbol
    board(b, m)
    return b

# random move of bot
def enemy(b, m) :
    i = random.randint(0,len(b)-1)
    j = random.randint(0,len(b)-1)
    while b[int(i)][int(j)] != ' ' :
        i = random.randint(0,len(b)-1)
        j = random.randint(0,len(b)-1)
    b[i][j] = 'O'
    board(b, m)
    return b

def check_win(b, m) :
    # check for row win or loss
    flag_X = True
    flag_O = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[i][j] != 'X' : flag_X = False
            if b[i][j] != 'O' : flag_O = False
            j = j+1
        if flag_X == True :
            print('\nYou Win') if int(m) == 1 else print('\nP1 Wins')
            return True
        elif flag_O == True :
            print('\nYou Lose') if int(m) == 1 else print('\nP2 Wins')
            return True
        flag_X = True
        flag_O = True
        i = i+1

    # check for column win or loss
    flag_X = True
    flag_O = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[j][i] != 'X' : flag_X = False
            if b[j][i] != 'O' : flag_O = False
            j = j+1
        if flag_X == True :
            print('\nYou Win') if int(m) == 1 else print('\nP1 Wins')
            return True
        elif flag_O == True :
            print('\nYou Lose') if int(m) == 1 else print('\nP2 Wins')
            return True
        flag_X = True
        flag_O = True
        i = i+1

    # check for main diagonal win or loss
    i = 0
    flag_X = True
    flag_O = True
    for x in b :
        if b[i][i] != 'X' : flag_X = False
        if b[i][i] != 'O' : flag_O = False
        i = i+1
    if flag_X == True :
        print('\nYou Win') if int(m) == 1 else print('\nP1 Wins')
        return True
    elif flag_O == True :
        print('\nYou Lose') if int(m) == 1 else print('\nP2 Wins')
        return True

    # check for secondary diagonal win or loss
    i = 0
    j = len(b)-1-i
    flag_X = True
    flag_O = True
    for x in b :
        if b[i][j] != 'X' : flag_X = False
        if b[i][j] != 'O' : flag_O = False
        i = i+1
        j = j-1
    if flag_X == True :
        print('\nYou Win') if int(m) == 1 else print('\nP1 Wins')
        return True
    elif flag_O == True :
        print('\nYou Lose') if int(m) == 1 else print('\nP2 Wins')
        return True
    
    # check for tie game
    full = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[i][j] == ' ' :
               full = False
               break
            j = j+1
        i = i+1
    if full == True :
        print('\nTie Game')
        return True

    return False

def main() :
    m = mode()
    size = input_size(m)
    b = [ [' ']*int(size) for i in range(int(size))]
    board(b, m)
    end = False
    while end == False :
        b = user(b, m, 'X')
        end = check_win(b, m)
        if(end == True) :   break

        if int(m) == 1 :    b = enemy(b, m)
        elif int(m) == 2 :  b = user(b, m, 'O')

        end = check_win(b, m)
        if(end == True) :   break

if __name__ == "__main__" :
    main()