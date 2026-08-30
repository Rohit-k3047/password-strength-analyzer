import secrets
import string


def generate_password(length=16):

    if not isinstance(length, int):
        raise TypeError("Password length must be an integer.")

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*()-_=+"

    # Guarantee one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(special)
    ]

    all_characters = (
        lowercase +
        uppercase +
        numbers +
        special
    )

    # Fill remaining positions
    for _ in range(length - 4):
        password.append(
            secrets.choice(all_characters)
        )

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


if __name__ == "__main__":

    password = generate_password(16)

    print("Generated password:")
    print(password)