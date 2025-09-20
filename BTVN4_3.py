p, q, e = 17, 23, 5
n = p * q
phi = (p - 1) * (q - 1)


for d in range(1, phi):
    if (d * e) % phi == 1:
        break

P = "LeDucKien"
m = [ord(c) for c in P]  
c = [pow(x, e, n) for x in m]  
g = [pow(y, d, n) for y in c]
G = ''.join(chr(x) for x in g)

print("n =", n, "phi =", phi, "d =", d)
print("Mã gốc:", P)
print("Dãy số:", m)
print("Bản mã:", c)
print("Giải mã:", G)
