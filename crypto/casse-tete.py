def decrypt_cesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        # Vérifiez si le caractère est imprimable dans la plage ASCII spécifiée
        if 32 <= ord(char) <= 127:
            # Décalez le caractère en sens inverse
            decrypted_char = chr((ord(char) - shift - 32) % 96 + 32)
            decrypted_text += decrypted_char
    return decrypted_text

# Exemple d'utilisation
ciphertext = "rCJAE@4@56"
for i in range(96):
    decrypted_text = decrypt_cesar_cipher(ciphertext, i)
    print(decrypted_text)
