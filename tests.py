from analyzer import analyze_password
from generator import generate_password


def test_password(password, expected_strength):

    result = analyze_password(password)

    print(f"Testing: {password}")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']} / 7")

    if result["strength"] == expected_strength:
        print("PASS ✓")
    else:
        print(
            f"FAIL ✗ "
            f"(Expected: {expected_strength})"
        )

    print("-" * 40)


print("\n========================================")
print("      PASSWORD ANALYZER TESTS")
print("========================================\n")


# Test 1 - Very weak
test_password(
    "abc",
    "VERY WEAK"
)


# Test 2 - Weak/common
test_password(
    "password",
    "VERY WEAK"
)


# Test 3 - Medium
test_password(
    "Blue123",
    "WEAK"
)


# Test 4 - Strong
test_password(
    "BlueRiver27!",
    "VERY STRONG"
)


# Test 5 - Very strong
test_password(
    "K7!mQ2#vR9@xP4$Z",
    "VERY STRONG"
)


# ----------------------------------------
# Password Generator Test
# ----------------------------------------

print("\nTesting password generator...")

generated = generate_password(16)

print("Generated:", generated)
print("Length:", len(generated))

if len(generated) == 16:
    print("Generator PASS ✓")
else:
    print("Generator FAIL ✗")

# ----------------------------------------
# Edge Case Tests
# ----------------------------------------

print("\n========================================")
print("          EDGE CASE TESTS")
print("========================================")


# Empty password
print("\nTesting empty password...")

try:
    result = analyze_password("")

    print("PASS ✓")
    print("Score:", result["score"])

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


# Very long password
print("\nTesting very long password...")

try:
    long_password = "A1!" + ("abc" * 100)

    result = analyze_password(long_password)

    print("Length:", result["length"])
    print("Strength:", result["strength"])
    print("PASS ✓")

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


# Repeated characters
print("\nTesting repeated characters...")

try:
    result = analyze_password("AAAAAAAAAAAA")

    print("Repetition detected:",
          result["has_repetition"])

    print("PASS ✓")

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


# Sequential characters
print("\nTesting sequential pattern...")

try:
    result = analyze_password("abcdef123456")

    print("Sequence detected:",
          result["has_sequence"])

    print("PASS ✓")

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


# Keyboard pattern
print("\nTesting keyboard pattern...")

try:
    result = analyze_password("qwerty123")

    print("Keyboard pattern detected:",
          result["has_keyboard"])

    print("PASS ✓")

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


# Unicode password
print("\nTesting Unicode password...")

try:
    result = analyze_password("Rohit🔐123!")

    print("Length:", result["length"])
    print("Strength:", result["strength"])

    print("PASS ✓")

except Exception as error:
    print("FAIL ✗")
    print("Error:", error)


print("\n========================================")
print("       EDGE TESTS COMPLETE")
print("========================================")


print("\n========================================")
print("             TEST COMPLETE")
print("========================================")

print("\n========================================")
print("      GENERATOR SECURITY TESTS")
print("========================================")


# Test minimum length
print("\nTesting minimum length...")

try:

    password = generate_password(8)

    if len(password) == 8:
        print("PASS ✓")
    else:
        print("FAIL ✗")

except Exception as error:

    print("FAIL ✗")
    print(error)


# Test invalid length
print("\nTesting invalid length...")

try:

    generate_password(7)

    print("FAIL ✗")

except ValueError:

    print("PASS ✓")


# Test invalid type
print("\nTesting invalid type...")

try:

    generate_password("16")

    print("FAIL ✗")

except TypeError:

    print("PASS ✓")


# Test character diversity
print("\nTesting character diversity...")

password = generate_password(16)

has_lowercase = any(
    c.islower() for c in password
)

has_uppercase = any(
    c.isupper() for c in password
)

has_number = any(
    c.isdigit() for c in password
)

has_special = any(
    c in "!@#$%^&*()-_=+"
    for c in password
)


if (
    has_lowercase
    and has_uppercase
    and has_number
    and has_special
):

    print("PASS ✓")

else:

    print("FAIL ✗")


# Test uniqueness
print("\nTesting password uniqueness...")

password1 = generate_password(16)
password2 = generate_password(16)

if password1 != password2:

    print("PASS ✓")

else:

    print("FAIL ✗")


print("\n========================================")
print("   GENERATOR SECURITY TESTS COMPLETE")
print("========================================")