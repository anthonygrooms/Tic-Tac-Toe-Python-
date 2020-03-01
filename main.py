import time, random

#Print the gameboard
def printGameBoard():
  print("[",end="")
  index = 0

  for item in gameboard:

    print(item,end="")
    
    index+=1
    if index % 3 == 0:
      print("]\n",end="")
      if index < 8:
        print("[",end="")
    else:
      print(", ",end="")

#Check if there exists a tic tac toe solution for parametr s
def checkMatch(s):
  if gameboard[0]==gameboard[1]==gameboard[2]==s or gameboard[3]==gameboard[4]==gameboard[5]==s or gameboard[6]==gameboard[7]==gameboard[8]==s or gameboard[0]==gameboard[3]==gameboard[6]==s or gameboard[1]==gameboard[4]==gameboard[7]==s or gameboard[2]==gameboard[5]==gameboard[8]==s or gameboard[0]==gameboard[4]==gameboard[8]==s or gameboard[6]==gameboard[4]==gameboard[2]==s:
    return True
  else:
    return False

def checkTie():
  #Check if there is a tie by seeing if no number exist in the gameboard (i.e. filled with X's and O's)
  for i in range(1,10):
    if i in gameboard:
      return False
  return True

#Check if there is a winner
def checkWinner():
  
  if checkMatch("X"):
    return "Player"
  elif checkMatch("O"):
    return "CPU"
  elif checkTie():
    return "Tie"
  else:
    return None

while True:
  #Create a gameboard
  gameboard = [1,2,3,4,5,6,7,8,9]

  winner = False

  #Loop the game until there is a winner
  while not(winner):
    printGameBoard()

    if checkWinner()!=None:
      break

    player = -1 #Force the player variable to -1 so we can enter the player input loop

    #Keep asking the player for a number from 1 to 9 until they correctly do so
    while player == -1 or player not in range(1,10) or type(gameboard[player-1])is not int:
      #Try to convert input into an int. If this causes any error, do nothing
      try:
        player = int(input("Enter a number from 1-9: "))
      except:
        None

    #insert an x at the correct slot
    gameboard[player-1]='X'

    print()
    printGameBoard()

    if checkWinner()!=None:
      break

    print("Awaiting CPU... ",end="", flush=True)
    time.sleep(.5)

    #Get the cpu input. Force the input to be a number that is not taken
    cpu = random.randint(1,9)
    while type(gameboard[cpu-1]) is not int:
      cpu = random.randint(1,9)
    print(cpu)

    #insert a O at the correct slot
    print()
    gameboard[cpu-1]='O'

  #End the round
  result = checkWinner()
  if result!="Tied":
    print("\n{} wins.".format(result))
  else:
    print("It is tied")
    
  #Ask if player wants to play again, end the game if input is anything other than yes
  if input("Play again? Enter yes to continue: ").lower()!="yes":
    break
  print()

print("Goodbye")