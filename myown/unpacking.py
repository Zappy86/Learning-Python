import hashlib as lib

banana = lib.sha256(input("Password1: ").encode("utf-8")).digest()

banana2 = lib.sha256(input("Password2: ").encode("utf-8")).digest()

print((banana))
print((banana2))

if (banana) == (banana2): print("Ya!")