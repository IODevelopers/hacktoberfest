'''
#1
a. Print your name using python
b. Print your email using python
c. Reverse your email, reverse your name, combine it and then hash it with MD5

Using python-3.6
'''

import hashlib

def main():
    name = "Fajar Maulana Firdaus"
    email = "fajarmf78@gmail.com"
    print(name + "\n" + email)
    joined = name+email
    hashed = hashlib.md5(joined.encode('utf-8'))
    print((name)[::-1] + "\n" + (email)[::-1] + "\n" + joined + "\n" + hashed.hexdigest())

main()