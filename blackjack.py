import random

user_cards = []
computer_cards = []
is_game_over = False

def compare(user_score, computer_score):
    if computer_score == user_score:
        print('Draw!')
    elif computer_score == 0:
        print('Dealer wins!')
    elif user_score == 0:
        print('you win!')
    elif computer_score > 21:
        print('Dealer went over. You win.')
    elif user_score > 21:
        print('You went over. Dealer wins.')
    elif computer_score > user_score:
        print('Dealer wins.')
    else:
        print('You win!')

def deal_hand():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

for d in range(2):
    user_cards.append(deal_hand())
    computer_cards.append(deal_hand())
    
def calculate_score(cards):
    """Takes list of card values and returns '0' if 21 (blackjack), otherwise returns score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f'Your cards: {user_cards}, current score: {user_score}')    
    print(f'Dealers first card: {computer_cards[0]}')

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card. Type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_hand())
        else:
            is_game_over = True

while computer_score < 16:
    computer_cards.append(deal_hand())
    computer_score = calculate_score(computer_cards)
    
compare(user_score, computer_score)
print(f'Your cards: {user_cards}, current score: {user_score}')
print(f'Dealer cards: {computer_cards}, score: {computer_score}')