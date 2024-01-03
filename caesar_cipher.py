alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(text, shift):
    encrypted_text = ''
    
    for letter in text:
        shifted_index = alphabet.index(letter) + shift
        encrypted_text += alphabet[shifted_index]
    
    print(f'Encrypted text: {encrypted_text}')

def decrypt(text, shift):
    decrypted_text = ''
    
    for letter in text:
        restored_index = alphabet.index(letter) - shift
        decrypted_text += alphabet[restored_index]
        
    print(f'Decrypted text: {decrypted_text}')
    
if direction == 'encrypt':
    encrypt(text, shift)
elif direction == 'decrypt':
    decrypt(text, shift)