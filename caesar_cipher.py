def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        # Check if character is an alphabet
        if char.isalpha():
            # Determine ASCII offset
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            if mode == "encrypt":
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                new_char = chr((ord(char) - start - shift) % 26 + start)

            result += new_char
        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result


# ===== Main Program =====
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'E' for Encryption or 'D' for Decryption: ").upper()

if choice == 'E':
    encrypted_text = caesar_cipher(message, shift, "encrypt")
    print("Encrypted Text:", encrypted_text)

elif choice == 'D':
    decrypted_text = caesar_cipher(message, shift, "decrypt")
    print("Decrypted Text:", decrypted_text)

else:
    print("Invalid choice! Please select E or D.")

