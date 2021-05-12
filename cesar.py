def crypt(mot,clé):
    liste=[]
    for i in range(len(mot)):
        cmpt=mot[i]
        decr=chr((ord(cmpt)+clé-96)%26+96)
        liste.append(decr)
    return liste

def decrypt(mot ,clé):
    liste=[]
    for i in range(len(mot)):
        cmpt=mot[i]
        decr=chr((ord(cmpt)-clé-96)%26+96)
        liste.append(decr)
    return liste