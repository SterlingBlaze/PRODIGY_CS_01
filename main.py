def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine whether to shift forwards or backwards
            shift_direction = 1 if char.islower() else -1
            # Convert the character to its ASCII code, shift it, then convert back to a character
            encrypted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift * shift_direction) % 26) + ord('a' if char.islower() else 'A'))
            encrypted_text += encrypted_char
        else:
            # If it's not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

def main():
    message = input("Enter message: ")
    shift = int(input("Enter shift value (a number between 1 and 25): "))
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, -shift)  # Decrypt by shifting back by the same amount
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
