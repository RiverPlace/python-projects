import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("Please enter the number of letters: "))
num_numbers = int(input("Please enter the number of numbers: "))
num_symbols = int(input("Please enter the number of symbols: "))

letters = random.sample(letters, num_letters)
numbers = random.sample(numbers, num_numbers)
symbols = random.sample(symbols, num_symbols)

temp_password = letters + numbers + symbols
random.shuffle(temp_password)
new_password = "".join(temp_password)

print(f"Your new password is: {new_password}")