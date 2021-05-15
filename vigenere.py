def Vigenere(msg, cle):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    i = 0
    for caractere in msg:
        debut = alpha.find(cle[i])
        pos = alpha.find(caractere)
        indice = pos+debut
        if indice > 25:
            indice -= 26
        res += alpha[indice]
        i += 1
        if i >= len(cle):
            i = 0
    return res

print(Vigenere("ABCDEFGHIJ", "EBAEBAEBAEBA"))