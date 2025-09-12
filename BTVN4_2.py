plaintext = "LeDucKien"
k = 9  
ciphertext = ""

for ch in plaintext:
    if ch.isalpha():
        p_val = ord(ch.upper()) - ord('A')
        c_val = (p_val + k) % 26
        ciphertext += chr(c_val + ord('A'))
    else:
        ciphertext += ch

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
