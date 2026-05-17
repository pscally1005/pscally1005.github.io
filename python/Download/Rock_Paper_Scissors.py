from os import system
import random
import getch

# Header at top of program
def top() :
    system('clear')
    print('\nWelcome to Rock-Paper-Scissors!\n')
    print('Enter "0" for Rock')
    print('Enter "1 for Paper')
    print('Enter "2" for Scissors')

# Code for user to enter a move
def enter():
    print('\nPlease Enter a Number: ', end=' ')
    play = getch.getch().decode()

    while play not in ['0', '1', '2']:
        top()
        print('\nError: Input is not valid')
        print('\nPlease Enter a Number: ', end=' ')
        play = getch.getch().decode()

    top()

    if play == '0':
        print('\nYou entered: Rock')
    elif play == '1':
        print('\nYou entered: Paper')
    else:
        print('\nYou entered: Scissors')

    return play

# Code for enemy responding move
def bot_move() :
    bot = random.randint(0,2)
    print('Enemy Plays:', end = ' ')
    if bot == 0:
        print('Rock')
    elif bot == 1:
        print('Paper')
    elif bot == 2:
        print('Scissors')
    else :
        print('ERROR')
    return bot

# Returns Win, Loss, or Tie
def win_conditions(play, bot) :
    condition = 'ERROR'
    if (int(play) + 1) % 3 == bot :
        condition = 'Loss'
    elif (int(play) + 2) % 3 == bot :
        condition = 'Win'
    elif (int(play)) % 3 == bot :
        condition = 'Tie'
    return condition

# Main code
top()
play = enter()
bot = bot_move()
print('Game Outcome: ' + win_conditions(play, bot))
print('\nEnd of Game')
