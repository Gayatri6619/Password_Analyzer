import re

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase
if re.search(r"[A-Z]", password):
    score += 1

# Check lowercase
if re.search(r"[a-z]", password):
    score += 1

# Check number
if re.search(r"[0-9]", password):
    score += 1

# Check special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nPassword Analysis")
print("-----------------")

if score <= 2:
    print("Strength: Weak")
elif score == 3 or score == 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

print("\nSuggestions:")
if len(password) < 8:
    print("- Use at least 8 characters.")
if not re.search(r"[A-Z]", password):
    print("- Add an uppercase letter.")
if not re.search(r"[a-z]", password):
    print("- Add a lowercase letter.")
if not re.search(r"[0-9]", password):
    print("- Add a number.")
if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("- Add a special character.")