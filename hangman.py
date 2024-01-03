import random

# Step 1
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False

display = []
for _ in range(len(chosen_word)):
    display.append('_')
    
def check_guess():
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            
while not end_of_game:
    guess = input('Please pick a random letter: ').lower()
    
    check_guess()
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose.')
    
    if '_' not in display:
        end_of_game = True
        print('You win.')