# ALGORITHME DU CRYPTAGE VIGENERE AVEC LES DIFFERENTES POP-UP ET 
# MESSAGES DES ERREURS SI LES TYPES SOUHAITE NE SONT PAS RECONNUS

 
from cesar import decrypt_cesar
from tkinter import *
import winsound
import time

def chiffre_vigenere(msg, cle):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    i = 0
    for caractere in msg :
        if 65 <= ord(caractere) <= 90:
            debut = alpha.find(cle[i])
            pos = alpha.find(caractere)
            indice = pos+debut
            if indice > 25:
                indice -= 26
            res += alpha[indice]
            i += 1
            if i >= len(cle):
                i = 0
        else:
            def quit():
                    fenetre_error.destroy()
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
            button_quitter = Button(fenetre_error, text = 'QUIT', command=quit,bg="red")
            button_quitter.pack(side=TOP)    
            raise TypeError
    for val in cle:
        if 65<=ord(val)<=90:
            None
        else:
            def quit():
                    fenetre_error.destroy()
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
            button_quitter = Button(fenetre_error, text = 'QUIT', command=quit,bg="red")
            button_quitter.pack(side=TOP)    
            raise TypeError

    return res
    

def dechiffre_vigenere(msg, cle):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    i = 0
    for caractere in msg:
        if 65 <= ord(caractere) <= 90:
            debut = alpha.find(cle[i])
            pos = alpha.find(caractere)
            indice = pos-debut
            if indice > 25:
                indice -= 26
            res += alpha[indice]
            i += 1
            if i >= len(cle):
                i = 0
        else:
            def quit():
                    fenetre_error.destroy()
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
            button_quitter = Button(fenetre_error, text = 'QUIT', command=quit,bg="red")
            button_quitter.pack(side=TOP)    
            raise TypeError  
    for val in cle:
        if 65<=ord(val)<=90:
            None
        else:
            def quit():
                    fenetre_error.destroy()
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
            button_quitter = Button(fenetre_error, text = 'QUIT', command=quit,bg="red")
            button_quitter.pack(side=TOP)    
            raise TypeError        
    return res
