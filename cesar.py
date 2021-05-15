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
        
    else:
        winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(2)  # Attendre 2s
        winsound.PlaySound(None, 0)  # Interruption de la lecture
        fenetre_error = Toplevel()
        fenetre_error.title("ERREUR")
        fenetre_error.config(bg="red")
        fenetre_error.geometry("450x450")
        can = Canvas(fenetre_error,width=450,height=450,bg="white")
        img=PhotoImage(file="images\erreur.png")
        can.create_image(0,0,anchor=NW,image=img)
        can.place(x=0,y=0)
        fenetre_error.resizable(width=False, height=False)
        fenetre_error.iconbitmap("images\download.ico")    
        raise TypeError


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

    else:
        winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(2)  # Attendre 2s
        winsound.PlaySound(None, 0)  # Interruption de la lecture
        fenetre_error = Toplevel()
        fenetre_error.title("ERREUR")
        fenetre_error.config(bg="red")
        fenetre_error.geometry("450x450")
        can = Canvas(fenetre_error,width=450,height=450,bg="white")
        img=PhotoImage(file="images\erreur.png")
        can.create_image(0,0,anchor=NW,image=img)
        can.place(x=0,y=0)
        fenetre_error.resizable(width=False, height=False)
        fenetre_error.iconbitmap("images\download.ico")    
        raise TypeError