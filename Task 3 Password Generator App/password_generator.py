import random
import string

# Allowed special characters as per policy
SPECIAL_CHARS = "#!@$&*/?"

# Store last 3 generated passwords
password_history = []


def is_valid(password, login_id, first_name, last_name):
    """Check password against defined policy rules."""
    # Rule 1: Length between 8 and 15
    if not (8 <= len(password) <= 15):
        return False
    
    # Rule 2: At least 2 alphabetic characters
    if sum(c.isalpha() for c in password) < 2:
        return False

    # Rule 3: Cannot contain login_id, first_name, or last_name
    lowered = password.lower()
    if (login_id.lower() in lowered or
        first_name.lower() in lowered or
        last_name.lower() in lowered):
        return False

    # Rule 4: Cannot repeat one of the last 3 passwords
    if password in password_history:
        return False
    
    return True


def generate_password(login_id, first_name, last_name, length):
    """Generate a password until all policy rules are satisfied."""
    while True:
        # Ensure at least 1 lowercase, 1 uppercase, 1 digit, 1 special char
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(SPECIAL_CHARS)  # ✅ Mandatory symbol
        ]

        # Fill the rest with random allowed chars
        all_chars = string.ascii_letters + string.digits + SPECIAL_CHARS
        password += random.choices(all_chars, k=length - len(password))

        # Shuffle characters so it looks random
        random.shuffle(password)
        password = "".join(password)

        # Validate against policy
        if is_valid(password, login_id, first_name, last_name):
            # Maintain history of last 3 passwords
            password_history.append(password)
            if len(password_history) > 3:
                password_history.pop(0)
            return password


def main():
    print("🔐 Secure Password Generator (Policy Enforced)\n")
    login_id = input("Enter login ID: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()

    while True:
        try:
            length = int(input("Enter desired password length (8–15): "))
            if not (8 <= length <= 15):
                print("❌ Length must be between 8 and 15.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        password = generate_password(login_id, first_name, last_name, length)
        print(f"\n✅ Generated Secure Password: {password}")

        again = input("\nGenerate another password? (yes/no): ").lower()
        if again != "yes":
            print("👋 Stay secure. Goodbye!")
            break


if __name__ == "__main__":
    main()
