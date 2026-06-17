import re

password = input("Enter your password: ")

strength = 0

# Check length
if len(password) >= 8:
    strength += 1

# Check for uppercase letters
if re.search(r"[A-Z]", password):
    strength += 1

# Check for lowercase letters
if re.search(r"[a-z]", password):
    strength += 1

# Check for digits
if re.search(r"[0-9]", password):
    strength += 1

# Check for special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

# Display strength
if strength <= 2:
    print("Weak Password ❌")
elif strength <= 4:
    print("Medium Password ⚠️")
else:
    print("Strong Password ✅")
