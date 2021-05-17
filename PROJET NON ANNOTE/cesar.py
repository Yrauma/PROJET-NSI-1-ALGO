from tkinter import *
import winsound
import time

def crypt_cesar(mot,clé):
    liste=[]
    for l in mot:
        if 65 <= ord(l) <= 90:
            for i in range(len(mot)):
                cmpt=mot[i]
                decr=chr((ord(cmpt)+clé-65)%26+65)
                liste.append(decr)
            return liste

        elif 97<=ord(l) <=122:
            for i in range(len(mot)):
                cmpt=mot[i]
                decr=chr((ord(cmpt)+clé-97)%26+97)
                liste.append(decr)
            return liste

def decrypt_cesar(mot ,clé):
    liste=[]
    for l in mot:
        if 65 <= ord(l) <= 90:
            for i in range(len(mot)):
                cmpt=mot[i]
                decr=chr((ord(cmpt)-clé-65)%26+65)
                liste.append(decr)
            return liste

        elif 97<=ord(l) <=122:
            for i in range(len(mot)):
                cmpt=mot[i]
                decr=chr((ord(cmpt)-clé-97)%26+97)
                liste.append(decr)
            return liste