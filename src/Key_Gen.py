from cryptography.fernet import Fernet

# Generate a key (do this once and share the key securely)
key = Fernet.generate_key()
print(key)

# Save the key in a secure place
with open('secret.key', 'wb') as key_file:
    key_file.write(key)
