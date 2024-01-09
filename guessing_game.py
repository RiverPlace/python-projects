from random import randint

print('Welcome to the number printing game!')
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = randint(1, 101)
game_over = False

if difficulty == 'easy':
    lives = 10
else:
    lives = 5
    
while lives > 0:
    print(f'You have {lives} attempts remaining to guess teh number.')
    lives -= 1
    guess = int(input('Make a guess: '))
    
    if guess == number:
        print('You win!')
        break
    elif guess > number:
        print('Too high.')
    else:
        print('Too low.')
    
    print('Guess again.')

if lives == 0:
    print("You're out of lives!")