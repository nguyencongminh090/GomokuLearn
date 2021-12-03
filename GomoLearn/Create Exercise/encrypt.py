from cryptography.fernet import Fernet
import json


def load_key(key):
    return open(key + '.key', "rb").read()


def encrypt(fn: str):
    key = Fernet.generate_key()

    with open(fn, 'rb') as f:
        data = f.read()
        f.close()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data).decode() + '\n'

    fn = fn.split('.')[0]
    fn = fn + '.ecr'
    with open(fn, 'wb') as f:
        f.write(encrypted.encode())
        f.write(key)
        f.close()
    pass


def decrypt(fn: str):
    with open(fn, 'rb') as f:
        data = f.readline().decode().split('\n')[0]
        key = f.readline()
        fernet = Fernet(key)
        decrypt_text = fernet.decrypt(data.encode()).decode()
        print('Decrypt:', decrypt_text)
        f.close()
    return decrypt_text


encrypt('Data.json')
decrypt('Data.ecr')
