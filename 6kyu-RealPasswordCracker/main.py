import hashlib
from itertools import product


def password_cracker(hash):
    c = 'abcdefghijklmnopqrstuvwxyz' # range(a-z)
    if hash == hashlib.sha1(''.encode()).hexdigest():
        return "" 
    for i in range(2,6):  
        for item in product(c,repeat = i): # all combinations
            if hash == hashlib.sha1(''.join(item).encode()).hexdigest():
                return ''.join(item)

