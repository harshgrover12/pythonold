import os, binascii





salt = 'aaef2d3f4d77ac66e9c5a6c3d8f921d1'.encode("utf-8")
passwd = "AdminPassword".encode("utf-8")
key = pbkdf2_hmac("sha512", passwd, salt, 38000, 128)
print("Derived key:", binascii.hexlify(key))