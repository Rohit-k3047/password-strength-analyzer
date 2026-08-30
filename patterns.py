def normalize_password(password):

    replacements = {
        "@": "a",
        "4": "a",
        "3": "e",
        "0": "o",
        "1": "i",
        "!": "i",
        "5": "s",
        "$": "s",
        "7": "t"
    }

    normalized = ""

    for character in password.lower():

        if character in replacements:
            normalized += replacements[character]

        else:
            normalized += character

    return normalized

def has_sequential_characters(password):

    password = password.lower()

    for i in range(len(password) - 2):

        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        # Increasing sequence: abc, 123, xyz
        if second == first + 1 and third == second + 1:
            return True

        # Decreasing sequence: cba, 321, zyx
        if second == first - 1 and third == second - 1:
            return True

    return False

def has_repeated_characters(password):

    for i in range(len(password) - 2):

        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False
def has_keyboard_pattern(password):

    password = password.lower()

    keyboard_patterns = [
        "qwerty",
        "asdf",
        "zxcv",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "qazwsx",
        "wsxedc",
        "edcrfv"
    ]

    for pattern in keyboard_patterns:

        if pattern in password:
            return True

    return False