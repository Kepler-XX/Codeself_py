import rsa
from binascii import b2a_hex, a2b_hex

text = '123456'


def encrypt(text):
    with open('./public.pem', 'rb') as f:
        pubkey_str = f.read()
    pubkey = rsa.PublicKey.load_pkcs1(pubkey_str)
    ciphertext = rsa.encrypt(text.encode(), pubkey)
    encryptext = str(b2a_hex(ciphertext).decode('utf-8'))
    return encryptext


def decrypt(text):
    with open('./private.pem', 'rb') as f:
        prikey_str = f.read()
    prikey = rsa.PrivateKey.load_pkcs1(prikey_str)
    decrypt_text = rsa.decrypt(a2b_hex(text), prikey)
    decryptext = str(decrypt_text.decode('utf-8'))
    return decryptext


print(f'--encrypt--{encrypt(text)}')
print(f'--decrypt--{decrypt(text)}')