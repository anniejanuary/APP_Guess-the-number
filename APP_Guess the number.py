import random
from replit import clear
from art import logo

def difficulty ():
  '''Asks to choose difficulty level: 5 or 10 attempts'''
  global tries_left
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    tries_left = 10
    return tries_left
  elif difficulty == "hard": 
    tries_left = 5
    return tries_left

def guess_and_check (number):
  '''Asks user to guess the number and checks it against the target number'''
  global tries_left
  global tries_tried
  tries_tried = 0
  while tries_left != 0:
    guess = int(input("Make a guess: "))
    tries_left -= 1
    tries_tried += 1
    if guess == number:
      print(f"Congrats, you guessed it on {tries_tried}. try!")
      play_again()
    elif guess > number and tries_left != 0:
      print(f"Too high, guess again. Attempts remaining: {tries_left}")
    elif guess < number and tries_left != 0:
      print(f"Too low, guess again. Attempts remaining: {tries_left}")
  if tries_left == 0:
    print(f"You have 0 attempts remaining, you lost. The number was: {number}")
    play_again()

def play_again():
  '''Asks if user wants to play again'''
  if input("Would you like to play again? y or n: ") == "y":
    clear()
    new_game()
  else:
    quit()

def new_game():
  '''Initializes a new game'''
  print(logo)
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100) # in randint both 1 and 100 can show up
                                 # or number = randint(1,100) if above I wrote: from random import randint
  difficulty()
  print(f"Attempts remaining: {tries_left}")
  guess_and_check(number)
  
new_game()
