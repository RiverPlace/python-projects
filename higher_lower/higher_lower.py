""" REQUIREMENTS
1. Print logo
2. Write 1st comparison description
3. Print 'vs' logo
4. Write 2nd comparison description
5. Get user input on who they think has the highest follower count
6. If correct: 
    - their choice is sent to 1st comparison spot
    - new 2nd comparison is displayed 
    - score is increased by 1
7. If incorrect, they lose the game
    - score is displayed
"""

from art import logo, vs
from game_data import data
import random

comparisons = {
    'a': {},
    'b': {},
}
score = 0
game_is_over = False

def get_person():
    return random.choice(data)

def make_person_string(person, key):
    return f'Compare {key.title()}: {person['name']}, a {person['description']}, from {person['country']}.'

def compare(guess):
    highest = max(comparisons, key=comparisons.get)
    
    if highest == guess:
        return True

print(logo)

person_a = get_person()

while not game_is_over:
    comparisons['a'] = person_a['follower_count']
    person_a_string = make_person_string(person_a, 'A')
    print(person_a_string)

    print(vs)

    person_b = get_person()
    comparisons['b'] = person_b['follower_count']
    person_a_string = make_person_string(person_b, 'B')
    print(person_a_string)

    guess = input("Who has more followers? Type 'a' or 'b': \n")
    player_won = compare(guess)
    if player_won:
        score += 1
        print(f'You got it right! Score: {score}\n')
        if guess == 'b':
            person_a = person_b
    else:
        game_is_over = True
        print(f'You got it wrong. Your got {score} right.\n')
