import json
from cryptography.fernet import Fernet


def load_key(key):
    return open(key + '.key', "rb").read()


def encrypt(fn: str):
    key = Fernet.generate_key()

    with open(fn, 'rb') as file:
        dt = file.read()
        file.close()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(dt).decode() + '\n'

    fn = fn.split('.')[0]
    fn = fn + '.ecr'
    with open(fn, 'wb') as file:
        file.write(encrypted.encode())
        file.write(key)
        file.close()
    pass


def decrypt(fn: str):
    with open(fn, 'rb') as file:
        dt = file.readline().decode().split('\n')[0]
        key = file.readline()
        fernet = Fernet(key)
        decrypt_text = fernet.decrypt(dt.encode()).decode()
        file.close()
    return decrypt_text


f = open('Data.json', 'r')
data = json.load(f)
f.close()
k = open('Data.json', 'w')
while True:
    name = input('Exercise Name: ')
    image_name = input('Image name: ')
    problem = input('Problem: ')
    solution = input('Solution: ').split(', ')
    # Init
    ex = data['Ex']
    lts = {
        'image': image_name,
        'problem': problem,
        'solution': solution
    }
    data['Ex'].append(name)
    data[name] = lts
    chk = input('Exit? --> ')
    if chk.upper() == 'Y':
        break

json.dump(data, k)
k.close()
encrypt('Data.json')
print(decrypt('Data.ecr'))
