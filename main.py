"""
Dice Rolling Game
Author: Andrew Nguyen and John Garden

Original assignment by: Alex Wolfe

Create your own program using what you have learned throughout the year.

Use tutorials and online resources to your ability to make this program the best you can!
"""
#Imports
import random
#Imports
#Functions
def rules():
  print("\nThis works like a game of black jack, but with \"dice\" instead cards.  You can choose between three dice types, D10, D12, and D20, in order to get as close to 100 as you can without going over.  You will not be playing alone however, as the program will also be trying to beat you, so you must get as close to 100 as you can if want a chance winning.  If you are ready to end and feel you have gotten as close to 100 as you can, type \"end\" to end your turn and see if the computer can beat you.  When prompted with dice you would like to use, type either \"d10,\" \"d12,\" \"d20,\" to continue playing, or \"end\" to end the game.\n")

def player_d10():
  #generates a random number from 1 to 10
  temp_score = random.randint(1,10)
  return temp_score

def begin():
  print("Start")

def player_d12():
  #generates a random number from 1 to 12
  temp_score = random.randint(1,12)
  return temp_score

def player_d20():
  #generates a random number from 1 to 20
  temp_score = random.randint(1,20) 
  return temp_score
#Functions #print(player_score + player_d10())
#preset variables
dice = 0
com_play = "yes"
game = "yes"
roll = 0
player_play = "yes"
player_score = 0
com_score = 0
prob = 0
#preset variables
#code
while game != "begin":
  game = input("Type \"rules\" if you would like to view the rules of the game \n\nType \"begin\" if would like to play the game\n")
  if game == "rules":
    rules()
  if game == "begin":
    begin()
    while dice != "end" and player_score < 100:
      #this is the loop for the player to where 
      dice = input("\n\nWhat type of dice would you like to roll? ")
      if dice == "d10":
        roll = player_d10()
        player_score = int(player_score) + int(roll)
        print ("You rolled a/an " + str(roll))
        print("Your score is " + str(player_score))
      if dice == "d12":
        roll = player_d12()
        print ("You rolled a/an " + str(roll))
        player_score = int(player_score) + int(roll)
        print("Your score is " + str(player_score))
      if dice == "d20":
        roll = player_d20()
        print ("You rolled a/an " + str(roll))
        player_score = int(player_score) + int(roll)
        print("Your score is " + str(player_score))
print("\n\nYour final score is " + str(player_score))
if player_score > 100:
  print("Sorry, but you have lost this round.")
if player_score == 100:
  print("Congratulations! You have won!")
if player_score < 100:
  while com_score < 70:
    com_score = int(com_score) + player_d20()
  while com_score < 90:
    com_score = com_score + player_d12()
  if com_score == 91:
    prob = random.randint(1,10)
    if prob > 1:
      com_score = com_score + player_d10()
  if com_score == 92:
    prob = random.randint(1,10)
    if prob > 2:
      com_score = com_score + player_d10()
  if com_score == 93:
    prob = random.randint(1,10)
    if prob > 3:
      com_score = com_score + player_d10()
  if com_score == 94:
    prob = random.randint(1,10)
    if prob > 4:
      com_score = com_score + player_d10()
  if com_score == 95:
    prob = random.randint(1,10)
    if prob > 5:
      com_score = com_score + player_d10()
  if com_score == 96:
    prob = random.randint(1,10)
    if prob > 6:
      com_score = com_score + player_d10()
  if com_score == 97:
    prob = random.randint(1,10)
    if prob > 7:
      com_score = com_score + player_d10()
  if com_score == 98:
    prob = random.randint(1,10)
    if prob > 8:
      com_score = com_score + player_d10()
  if com_score == 99:
    prob = random.randint(1,10)
    if prob > 9:
      com_score = com_score + player_d10()
  print("The computer's final score is " + str(com_score))
  if com_score > 100:
    print("Congratulations! You have won! ")
  if player_score < com_score and com_score < 101:
    print("Sorry, but you have lost this round. ")
  if player_score > com_score and player_score < 101:
    print("Congratulations! You have won! ")
  if com_score == player_score:
    print("Oops, there has been a tie. ")