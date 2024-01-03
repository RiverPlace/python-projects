alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encode_decode(text, shift, direction):
    new_text = ''
    
    for letter in text:
        index = ''
        if direction == 'encode':
            index = alphabet.index(letter) + shift
        else:
            index = alphabet.index(letter) - shift
        new_text += alphabet[index]

    print(f'{direction.title()}ed text is: {new_text}')
    
encode_decode(text, shift, direction)