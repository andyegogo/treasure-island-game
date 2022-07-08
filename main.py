print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



#Write your code below this line 👇
reply1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
reply1 = reply1.lower()

if reply1 == "left":
  reply2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to   wait for a boat. Type 'swim' to swim across.\n")
  reply2 = reply2.lower()
  
  if reply2 == "wait":
    reply3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    reply3 = reply3.lower()
    
    if reply3 == "red":
      print("You've been burned by fire. Game Over!!!!")
    elif reply3 == "yellow":
      print("You found the treasure! You win!!!!")
    elif reply3 == "blue":
      print("You've been eaten by beasts, Game Over!!!!")
    else:
      print("GAME OVER!!!")
  else:
    print("You've been attacked by trout. Game Over!!!!")
    
else:
  print("Yov've fallen in a hole. Game Over!!!!")

  

