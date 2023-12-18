print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? '))
tip = input('What percentage tip would you like to give? 5, 12, or 15? ')
people = int(input('How many people split the bill? '))

multiplier = 1 + (int(tip) / 100)
total_bill = bill * multiplier
per_person = total_bill / people
print(f'Each person should pay ${round(per_person, 2)}')