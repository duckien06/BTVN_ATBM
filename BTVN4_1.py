
plaintext = "leduckien"
k = 9 

ciphertext = ""
for ch in plaintext:
    code = ord(ch) - ord('a')
    encrypted_code = (code + k) % 26
    ciphertext += chr(encrypted_code + ord('a'))

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
