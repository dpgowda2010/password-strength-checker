
import getpass
import string

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "iloveyou"
}


def check_password(password):
    score = 0
    suggestions = []

    # 1. Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Use at least 12 characters.")
    else:
        suggestions.append("Use a longer password (12+ characters).")

    # 2. Check character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Consider including a number.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Consider including a symbol.")

    # 3. Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common, predictable passwords.")

    # 4. Display result
    print("\n--- Password Security Report ---")
    print(f"Length: {len(password)} characters")
    print(f"Score: {score}/6")

    if password.lower() in COMMON_PASSWORDS:
        print("Strength: Very weak")
    elif len(password) < 8 or score <= 2:
        print("Strength: Weak")
    elif score <= 4 or len(password) < 12:
        print("Strength: Moderate")
    else:
        print("Strength: Strong (basic checks only)")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Good job! All basic checks passed.")

    print("\nNote: This is an educational checker,")
    print("not a guarantee of password security.")


def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter a test password: ")

    if not password:
        print("Please enter a password.")
        return

    check_password(password)


if __name__ == "__main__":
    main()

