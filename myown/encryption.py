import hashlib

password = hashlib.sha256(input("Enter password: ").encode("utf-8")).hexdigest()

with open("password.txt", "w") as f:
    f.write(password)

with open("password.txt", "r") as f:
    guess = hashlib.sha256(input("Enter password: ").encode("utf-8")).hexdigest()