import random

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

u = int(input("Press 1 for Rock, 2 for Paper, and 3 for Scissors. "))
c = random.randint(1, 3)
winner = ''

def print_hand(id):
    if id == 1:
        print(rock)
    elif id == 2:
        print(paper)
    elif id == 3:
        print(scissors)

if u > 3:
    print('Invalid number. Please select a new one.')
else:
    if u == 1 and c == 3:
        winner = 'user'
    elif u == 1 and c == 2:
        winner = 'computer'
    elif u == 2 and c == 1:
        winner = 'user'
    elif u == 2 and c == 3:
        winner = 'computer'
    elif u == 3 and c == 1:
        winner = 'computer'
    elif u == 3 and c == 2:
        winner = 'user'
    else:
        winner = 'tie'
    
    print(f"You picked")
    print_hand(u)
    print(f"Computer picked")
    print_hand(c)
    print(f"The winnder is: {winner}")