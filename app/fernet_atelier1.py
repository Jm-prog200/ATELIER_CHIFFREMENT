import os
from cryptography.fernet import Fernet

key = os.environ.get("FERNET_KEY")
if not key:
    raise ValueError("FERNET_KEY not found in environment variables!")

fernet = Fernet(key.encode())

message = b"Message secret !"
token = fernet.encrypt(message)
print("Chiffre : " + token.decode())

decrypted = fernet.decrypt(token)
print("Dechiffre : " + decrypted.decode())
