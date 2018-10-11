"""
A slightly better readable program 
"""

# used to get and validate user input
def validator(toprint, check=""):
    """Validates that a user's input is capitalized and asks again if not"""
    # checks to see if mode isn't alphabetic and asks the user for input if not
    while not check.isalpha():
        check = input(toprint)
    # returns the user's input capitalized
    return check.upper()


# main
while True:
    # prints UI
    print("""
                        #############################
                        #                           #
                        #    What mode would you    #
                        #      like to use?         #
                        #                           #
                        #    e - encode             #
                        #    d - decode             #
                        #    q - quit               #
                        #                           #
                        #############################
    """)
    # assigns mode so it can be referenced in the next line
    mode = "none"
    # Asks for User input in till they give a valid response
    while mode != "E" and mode != "D" and mode != "Q":
        mode = validator("")
    # quits if the user selected Q
    if mode == "Q":
        exit()
    # gets user message and keyword inputs as well as defining en
    message, key, en = validator("Message: "), validator("Keyword: "), ""
    # sets algorithm to encrypt or decrypt
    dore = -1 if mode == "D" else 1
    # loops each letter in message
    for i in range(len(message)):
        # adds a letter in message and a letter in keyword
        en += chr(((ord(message[i]) + ((ord(key[i % len(key)])) * dore) + dore)
                   % 26) +65)
    # prints output
    print(en)
