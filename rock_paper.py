import random

print('welcome come to game ')
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissor
scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list = [paper,scissor,rock]
game = int(input('what do you choose ? type 0 for rock 1 for paper and 2 scissor:'))
if game ==0:
   print(rock)
elif game ==1:
    print(paper)
elif game ==2:
     print(scissor)
print('computer choose')
computer_choose=(random.choice(list))
print(computer_choose)
if computer_choose== game:
    print('tie')
elif (computer_choose == paper and game==2 or
      computer_choose == rock and game == 1 or
      computer_choose == scissor and game == 0):
      print('you win')
else:
    print('you loose')

