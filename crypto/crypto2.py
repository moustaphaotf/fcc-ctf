def decrypt_cesar(ciphertext, shift):
    result = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                result += chr((shifted - ord('A')) % 26 + ord('A'))
            else:
                result += chr((shifted - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result

def brute_force_decrypt(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_cesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Message crypté
ciphertext = "UEZIB RQUHO CTILY ZYAW PLBO"

# Décryptage en utilisant la force brute
brute_force_decrypt(ciphertext)
