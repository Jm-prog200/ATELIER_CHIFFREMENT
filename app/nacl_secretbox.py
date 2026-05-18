import nacl.secret
import nacl.utils

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)

message = b"Message secret avec PyNaCl !"
encrypted = box.encrypt(message)
print("Chiffre : " + encrypted.hex())

decrypted = box.decrypt(encrypted)
print("Dechiffre : " + decrypted.decode())
