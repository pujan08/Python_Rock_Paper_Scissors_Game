rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




print("Welcome to the Rock, Paper, Scissors Game")
print(rock,paper,scissors)
ans=int(input("please enter the number 1 for rock, 2 for paper, 3 for scissors. "))
print("your sign is")
if(ans==1):
  print(rock)
elif(ans==2):
  print(paper)
elif(ans==3):
  print(scissors)
else:
  print("You enter wrong number")

import random
randomnumber=random.randint(1,3)
computerans=int(randomnumber)

print("Computer's sign is: ")
if randomnumber==1:
  print(rock)
elif randomnumber==2:
  print(paper)
else:
  print(scissors)

if(ans==1 and randomnumber==2):
  print("You loose")
elif(ans==1 and randomnumber==3):
  print("You win")
elif(ans==2 and randomnumber==1):
  print("You win")
elif(ans==2 and randomnumber==3):
  print("You loose")
elif(ans==3 and randomnumber==1):
  print("You loose")
elif(ans==3 and randomnumber==2):
  print("You win")
elif(ans == randomnumber):
  print("Result is Draw.")
