import random

# Step 1
word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')
    
def check_guess():
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

end_of_game = False
while not end_of_game:
    guess = input('Please pick a random letter: ').lower()
    
    check_guess()
    print(display)
    
    if '_' not in display:
        end_of_game = True
        print('You win.')