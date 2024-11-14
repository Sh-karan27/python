password = str(input("Enter yopur passord: "))

password_len = len(password)


if password_len < 6 :
    strength="Weak"
elif password_len <=10:
    strength="Medium"
else: strength = "Strong"

print("Passord strength is", strength)