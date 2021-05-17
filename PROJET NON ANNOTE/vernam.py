# L'algorithme n'est pas terminé et nous n'avons pas réussi a l'implémenter


#import secrets
#from operator import xor

#msg='ggg'
#def Vernam(msg):
#    cle= []
#    binaire = []
#    H=[]
#    for i in msg:
#        z = ord(i)
#        y = bin(z)
#        binaire.append(y)
#    a = "".join(binaire)
#    for i in range(len(a)):
#        p = secrets.randbelow(2)                                                                                         # creation de la clé avec 0 et 1
#        cle.append(p)
#    for i in cle:
#        H.append(str(i))
#    b = "".join(H)
#    print(xor(int(a,b)))
    
#print(Vernam(msg))

