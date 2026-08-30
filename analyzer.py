import math

from patterns import (
    normalize_password,
    has_sequential_characters,
    has_repeated_characters,
    has_keyboard_pattern
)


def load_dictionary(filename="dictionary.txt"):

    passwords = set()

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line in file:
                password = line.strip().lower()

                if password:
                    passwords.add(password)

    except FileNotFoundError:

        print("Warning: dictionary.txt not found.")

    return passwords


def check_common_password(password, dictionary):

    normalized_password = normalize_password(password)

    for common_password in dictionary:

        if common_password in normalized_password:
            return True

    return False


def calculate_score(result):

    score = 0

    # -------------------------
    # LENGTH
    # -------------------------

    if result["length"] >= 16:
        score += 3

    elif result["length"] >= 12:
        score += 2

    elif result["length"] >= 8:
        score += 1

    else:
        result["suggestions"].append(
            "Use at least 8 characters."
        )

    # -------------------------
    # CHARACTER DIVERSITY
    # -------------------------

    if result["has_lowercase"]:
        score += 1
    else:
        result["suggestions"].append(
            "Add lowercase letters."
        )

    if result["has_uppercase"]:
        score += 1
    else:
        result["suggestions"].append(
            "Add uppercase letters."
        )

    if result["has_digit"]:
        score += 1
    else:
        result["suggestions"].append(
            "Add numbers."
        )

    if result["has_special"]:
        score += 1
    else:
        result["suggestions"].append(
            "Add special characters."
        )

    # -------------------------
    # SECURITY PENALTIES
    # -------------------------

    if result["is_common"]:
        score -= 3

    if result["has_sequence"]:
        score -= 1

    if result["has_repetition"]:
        score -= 1

    if result["has_keyboard"]:
        score -= 1

    # -------------------------
    # KEEP SCORE BETWEEN 0 AND 7
    # -------------------------

    score = max(0, min(score, 7))

    return score

def calculate_entropy(password):

    character_pool = 0

    # Lowercase letters
    if any(character.islower() for character in password):
        character_pool += 26

    # Uppercase letters
    if any(character.isupper() for character in password):
        character_pool += 26

    # Numbers
    if any(character.isdigit() for character in password):
        character_pool += 10

    # Special characters
    if any(not character.isalnum() for character in password):
        character_pool += 33

    if character_pool == 0:
        return 0

    entropy = len(password) * math.log2(character_pool)

    return round(entropy, 2)

def calculate_effective_entropy(result):

    entropy = result["entropy"]

    # Common password penalty
    if result["is_common"]:
        entropy -= 30

    # Sequential pattern penalty
    if result["has_sequence"]:
        entropy -= 10

    # Keyboard pattern penalty
    if result["has_keyboard"]:
        entropy -= 10

    # Repeated character penalty
    if result["has_repetition"]:
        entropy -= 10

    # Prevent negative entropy
    entropy = max(0, entropy)

    return round(entropy, 2)

def calculate_guesses(effective_entropy):

    if effective_entropy <= 0:
        return 1

    if effective_entropy >= 300:
        return "Astronomically large"

    guesses = 2 ** effective_entropy

    return int(guesses)

def calculate_risk_level(result):

    if result["breached"] is True:
        return "CRITICAL"

    entropy = result["effective_entropy"]

    if entropy < 20:
        return "CRITICAL"

    elif entropy < 40:
        return "HIGH"

    elif entropy < 60:
        return "MEDIUM"

    elif entropy < 80:
        return "LOW"

    else:
        return "VERY LOW"


def format_guesses(guesses):

    if guesses < 1_000:
        return str(guesses)

    elif guesses < 1_000_000:
        return f"{guesses / 1_000:.2f} thousand"

    elif guesses < 1_000_000_000:
        return f"{guesses / 1_000_000:.2f} million"

    elif guesses < 1_000_000_000_000:
        return f"{guesses / 1_000_000_000:.2f} billion"

    elif guesses < 1_000_000_000_000_000:
        return f"{guesses / 1_000_000_000_000:.2f} trillion"

    else:
        return f"{guesses:.2e}"

def analyze_password(password):

    dictionary = load_dictionary()

    result = {
        "length": len(password),

        "has_lowercase": False,
        "has_uppercase": False,
        "has_digit": False,
        "has_special": False,
        "has_keyboard": False,
        "entropy": 0,
        "effective_entropy": 0,
        "estimated_guesses": 0,
        "is_common": False,
        "has_sequence": False,
        "has_repetition": False,
        "risk_level": "",

        "normalized": "",

        "breached": None,
        "breach_count": 0,

        "score": 0,
        "strength": "",
        "suggestions": []
    }

    # Character analysis
    for character in password:

        if character.islower():
            result["has_lowercase"] = True

        elif character.isupper():
            result["has_uppercase"] = True

        elif character.isdigit():
            result["has_digit"] = True

        else:
            result["has_special"] = True

    # Normalize password
    result["normalized"] = normalize_password(password)

    # Pattern detection
    result["is_common"] = check_common_password(
        password,
        dictionary
    )

    result["has_sequence"] = has_sequential_characters(password)

    result["has_repetition"] = has_repeated_characters(password)

    result["entropy"] = calculate_entropy(password)

    result["effective_entropy"] = calculate_effective_entropy(result)

    result["estimated_guesses"] = calculate_guesses(result["effective_entropy"])

    result["risk_level"] = calculate_risk_level(result)

    result["has_keyboard"] = has_keyboard_pattern(password)

    # Suggestions
    if result["is_common"]:
        result["suggestions"].append(
            "Avoid common passwords or words."
        )

    if result["has_sequence"]:
        result["suggestions"].append(
            "Avoid sequential characters such as 123 or abc."
        )

    if result["has_repetition"]:
        result["suggestions"].append(
            "Avoid repeating the same character multiple times."
        )

    if result["has_keyboard"]:
        result["suggestions"].append(
            "Avoid keyboard patterns such as qwerty or asdf."
    )
    # Calculate final score
    result["score"] = calculate_score(result)

    # Strength classification
    if result["score"] <= 1:
        result["strength"] = "VERY WEAK"

    elif result["score"] <= 3:
        result["strength"] = "WEAK"

    elif result["score"] <= 4:
        result["strength"] = "MEDIUM"

    elif result["score"] <= 5:
        result["strength"] = "STRONG"

    else:
        result["strength"] = "VERY STRONG"

    return result
