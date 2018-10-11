"""
An all too short keyword encryption program.
"""

def validator(mode, check = ""):
    while not check.isalpha(): check = input(mode).upper()
global check; mode = validator("d - decode, other - encode"); message, key, en, dore  = validator("Message: "), validator("Keyword: "), "", -1 if mode == "d" else 1
for i in range(len(message)): en+=chr(((ord(message[i]) + ((ord(key[i%len(key)])) * dore) - 25) % 26) + 65)
print (en)
