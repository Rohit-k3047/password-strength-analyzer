from analyzer import analyze_password, format_guesses
from generator import generate_password
# Get password from user
password = input("Enter your password: ")

# Analyze password
result = analyze_password(password)

# Display result

print("\n========================================")
print("      PASSWORD SECURITY REPORT")
print("========================================")

print("Strength :", result["strength"])
print("Score    :", result["score"], "/ 7")
print("Risk     :", result["risk_level"])

print("\nEntropy")
print("  Theoretical :", result["entropy"], "bits")
print("  Effective   :", result["effective_entropy"], "bits")

print("\nSecurity Checks")
print("  Common Password :", result["is_common"])
print("  Sequence        :", result["has_sequence"])
print("  Repetition      :", result["has_repetition"])
print("  Keyboard Pattern:", result["has_keyboard"])
print("  Compromised     :", result["breached"])

if result["breached"] is True:
    print("  Times Seen      :", result["breach_count"])

elif result["breached"] is False:
    print("  Times Seen      : 0")

else:
    print("  Breach Check    : UNKNOWN")


print("\nRecommendations")

if result["suggestions"]:

    for suggestion in result["suggestions"]:
        print(" -", suggestion)

else:
    print(" - No basic improvements needed.")


print("\nGenerated secure password:")
print(generate_password(16))