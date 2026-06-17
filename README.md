import re : mports Python's regular expression (re) module.
Used to search for patterns like uppercase letters, numbers, and special characters.

password = input("Enter your password: ")
Asks the user to enter a password and stores it in the variable password.

strength = 0
Creates a variable named strength.
It starts at 0 and increases as the password meets different requirements.

if len(password) >= 8:
    strength += 1
Checks if the password has at least 8 characters.
If yes, adds 1 point to strength.

if re.search(r"[A-Z]", password):
    strength += 1
Checks if the password contains at least one uppercase letter (A-Z).
If yes, adds 1 point.

if re.search(r"[a-z]", password):
    strength += 1
Checks if the password contains at least one lowercase letter (a-z).
If yes, adds 1 point.

if re.search(r"[0-9]", password):
    strength += 1
Checks if the password contains at least one digit (0-9).
If yes, adds 1 point.

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
Checks if the password contains at least one special character like @, #, $, !, etc.
If yes, adds 1 point.

if strength <= 2:
    print("Weak Password ❌")
elif strength <= 4:
    print("Medium Password ⚠️")
else:
    print("Strong Password ✅")
0–2 points: Weak Password ❌
3–4 points: Medium Password ⚠️
5 points: Strong Password ✅

Example
Input:
Abhinav@123
Checks:
Length ≥ 8 ✅
Uppercase (A) ✅
Lowercase (bhinav) ✅
Number (123) ✅
Special character (@) ✅
strength = 5
Output:
Plain text
Strong Password ✅
