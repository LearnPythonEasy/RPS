#!/bin/python3

from random import randint

#Rock Paper Scissors Game
#Created by Nate (http://github.com/ACA30)

while True:
    player = input('rock (r), paper (p) or scissors (s): ')

    if(player == 'r'):
      print('O', end=' ')
  
    elif(player == 'p'):
      print('___', end=' ')
  
    elif(player == 's'):
      print('8<', end=' ')
  
    else:
      print('??')
  
    print('vs', end=' ')

    chosen = randint(1,3)

    if(chosen == 1):
      computer = 'r'
      print('O')
  
    elif(chosen == 2):
      computer = 'p'
      print('___')
  
    else:
      computer = 's'
      print('>8')

    if(player == computer):
      print('DRAW!')
  
    elif(player == 'r' and computer == 's'):
      print('Player wins!')
  
    elif(player == 'r' and computer == 'p'):
      print('Computer wins!')
  
    elif(player == 'p' and computer == 'r'):
      print('Player wins!')
  
    elif(player == 'p' and computer == 's'):
      print('Computer wins!')

    elif(player == 's' and computer == 'p'):
      print('Player wins!')
  
    elif(player == "s" and computer == 'r'):
      print('Computer wins!')

    else:
      print('Huh? Something broke! Please restart the program!')

    response = input('Would you like to play again? y or n: ')
    if response == 'n':
        print('')
        print('')
        print('Thank you for playing the Rock Paper Scissors Game!')
        print('Created by Nate - http://github.com/ACA30')
        print('License can be found at: https://github.com/LearnPythonEasy/RPS/blob/master/LICENSE')
        print('')
        print('')
        break
