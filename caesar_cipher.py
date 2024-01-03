alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(text, shift):
    encrypted_text = ''
    
    for letter in text:
        shifted_index = alphabet.index(letter) + shift
        if shifted_index >= len(alphabet):
            new_index = len(alphabet) - shifted_index
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += alphabet[shifted_index]
    
    print(f'Encrypted: {encrypted_text}')
    

    
    
encrypt(text, shift)