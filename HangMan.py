# Program to play hangman

import random as rand
import turtle
import os
from time import sleep

world = turtle.Screen()

world.bgcolor('green')

K = turtle.Turtle()

K.pencolor('black')

K.fillcolor('black')

K.speed(0)

K.hideturtle()

for i in range(2):

  K.begin_fill()

  K.forward(100)

  K.left(90)

  K.forward(5)

  K.left(90)

  K.end_fill()

K.forward(55)

K.left(90)

for i in range(2):

  K.begin_fill()

  K.forward(100)

  K.left(90)

  K.forward(5)

  K.left(90)

  K.end_fill()

K.forward(100)

K.right(90)

for i in range(2):

  K.begin_fill()

  K.forward(25)

  K.left(90)

  K.forward(5)

  K.left(90)

  K.end_fill()

for i in range(2):

  K.begin_fill()

  K.left(90)

  K.forward(5)

  K.left(90)

  K.forward(5)

  K.end_fill()

gameType = input('Would you like to play against the computer (type Computer) or against a Friend (type Friend): ')

if gameType.upper() == "COMPUTER": 
  list1 = ['word', 'stuff']
  list2 = ['another', 'things']
  list3 = ['alex piper', 'alex piper']
  
  level = int(input('Input the level 1-3. 1 is the easiest and 3 is the hardest: '))
  
  if level == 1: 
    print('Level 1: Short Words')
    word = list(rand.choice(list1))
    #print(word)
    
  elif level == 2: 
    print('Level 2: Long Words')
    #print(word)
    word = list(rand.choice(list2))
    
  elif level == 3: 
    print('Level 3: Phrases')
    print("This level may have spaces but you don't need to guess the spaces") 
    word = list(rand.choice(list3))
    #print(word)
    
elif gameType.upper() == "FRIEND": 
  user_word = input("Have your opponent enter their word: ")
  print("Game will start in 5 seconds")
  # Clearing the Screen
  sleep(5)
  os.system('clear')
  user_word = user_word.lower()
  word = list(user_word)
  
guess_word = []
space = " "

for i in range(len(word)): 
    guess_word.append("_")
if space in word: 
  c = word.count(space)
  spot = -1
  for i in range(c): 
    spot = word.index(space, spot+1)
    if guess_word[spot] == "_":
        guess_word[spot] = space  
  
print(guess_word)

all_guesses = []
count = 0 
state = False 
while(state == False):  
  guess = input('Please guess a letter: ').replace(" ", "")
  guess = guess.lower()
  if len(guess) > 1: 
    print("Error, you can only guess one letter at a time.")
  elif guess in all_guesses: 
    print('You have already guessed that letter')
    #print('Guess list', all_guesses)
  elif guess in word: 
    c = word.count(guess)
    spot = -1; 
    for i in range(c): 
        spot = word.index(guess, spot+1)
        if guess_word[spot] == "_":
            guess_word[spot] = guess  
    print(guess_word)
  else: 
    count = count + 1 
    if count == 1: 
      print('draw head')
      K.forward(25)
      K.left(180)
      K.circle(10)
    elif count == 2: 
      print('draw body')
      K.left(90)
      K.penup()
      K.forward(20)
      K.pendown()
      K.forward(50)
      K.backward(30)
    elif count == 3: 
      print('draw left arm')
      K.right(115)
      K.forward(20)
      K.backward(20)
      K.right(130)
    elif count == 4: 
      print('draw right arm')
      K.forward(20)
      K.backward(20)
      K.right(115)
    elif count == 5: 
      print('draw left leg')
      K.right(75)
      K.forward(20)
      K.backward(20)
      K.left(150)
    elif count == 6: 
      print('draw right leg')
      K.forward(20)
      K.backward(20)
      print('Game over, you died')
      state = True
      
  if guess_word == word: 
    print('You win!')
    state = True  
  all_guesses.append(guess)
  
  
