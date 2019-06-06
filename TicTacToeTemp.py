from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print (board[1] +'|'+ board[2] + '|' + board[3])
    print('-|-|-')
    print (board[4] +'|'+ board[5] + '|' + board[6])
    print('-|-|-')
    print (board[7] +'|'+ board[8] + '|' + board[9])

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    
    return (board[1] == board[2] == board[3] == mark or 
    board[4] == board[5] == board[6] == mark or
    board[7] == board[8] == board[9] == mark or
    board[1] == board[4] == board[7] == mark or
    board[2] == board[5] == board[8] == mark or
    board[3] == board[6] == board[9] == mark or
    board[1] == board[5] == board[9] == mark or
    board[3] == board[5] == board[7] == mark)

import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' ' 

def full_board_check(board):
    
    for i in range(1,9):
        if space_check(board, i):
            return False
    else:
        return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        if position not in [1,2,3,4,5,6,7,8,9] :
            print('Enter a valid number')
        elif not space_check(board, position):
            print('That position has already been taken')
    return position

def replay():
    return input('Do you want to play again say Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    TicTacToeBoard = [' ']*10
    player1_name = input('Player 1,what is your name? ')
    player2_name = input('Player 2,what is your name? ')
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first')
    play = input('Do you want to start playing type Yes or No: ')
    
    if play.lower()[0].startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(TicTacToeBoard)
            chosen_position = player_choice(TicTacToeBoard)
            place_marker(TicTacToeBoard,player1_marker,chosen_position)
            
            if win_check(TicTacToeBoard,player1_marker):
                print(f'{player1_name} has won!!!')   
                display_board(TicTacToeBoard)
                game_on = False
            else:
                if full_board_check(TicTacToeBoard):
                    print ("It's a tie")
                    display_board(TicTacToeBoard)
                    game_on = False
                else:
                    turn = 'Player 2'              
        else:
            display_board(TicTacToeBoard)
            chosen_position = player_choice(TicTacToeBoard)   
            place_marker(TicTacToeBoard,player2_marker,chosen_position)                      
                                  
            if win_check(TicTacToeBoard,player2_marker):
                display_board(TicTacToeBoard)
                print(f'{player2_name} has won!!!')                        
                game_on = False
            else:
                if full_board_check(TicTacToeBoard):
                    display_board(TicTacToeBoard)
                    print ("It's a tie")
                    game_on = False               
                else:
                    turn = 'Player 1'            
    if not replay():
        print ("Thank you for playing.")
        break                                                