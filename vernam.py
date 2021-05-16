import secrets
from operator import xor

msg='ggg'
def Vernam(msg):
    cle= []
    binaire = []
    for i in msg:
        z = ord(i)
        y = bin(z)
        binaire.append(y)
    a = "".join(binaire)
    print(a)
    for i in range(len(a)):
        p = secrets.randbelow(2)                                                                                         # creation de la clé avec 0 et 1
        cle.append(p)
    b = "".join(cle)
    print(xor(a,b))

print(Vernam(msg))