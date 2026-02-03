password = input("Enter a password: ")

if len(password) < 8:
    print("❌ Password too short (min 8 characters)")
elif password.isdigit():
    print("❌ Password cannot be numbers only")
else:
    print("✅ Password accepted")
# Password Strength Checker