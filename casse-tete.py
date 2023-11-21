from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def decrypt_message(ciphertext, key):
    key_bytes = key.encode('utf-8')
    ciphertext_bytes = base64.b64decode(ciphertext)

    # Utilisation de AES en mode CBC avec IV nul (par défaut)
    cipher = Cipher(algorithms.AES(key_bytes), modes.CFB8(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext_bytes) + decryptor.finalize()

    return decrypted_data.decode('utf-8')

# Message et clé
message = "Ay4kCPEb4xgmXCBYYD/5kPFUYfU1zdJAucIwpNVQLQjeQ081R2uW9jy8qA==*8BFyo1Z3F3R/q+qTOISNzA==*G/sCnG7H/qfgJBHGXk6NbA==*bY08cXs8ZOb/b5mstzA5LA=="
key = "FCC"
key = key[:16].ljust(16, ' ')


# Séparation des parties du message
parts = message.split('*')

# Décryptage de chaque partie
decrypted_parts = [decrypt_message(part, key) for part in parts]

# Affichage des résultats
for i, decrypted_part in enumerate(decrypted_parts):
    print(f"Partie {i + 1}: {decrypted_part}")
