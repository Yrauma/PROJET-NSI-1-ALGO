from cesar import decrypt_cesar
from tkinter import *
import winsound
import time

def chiffre_vigenere(msg, cle):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_1 = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    i = 0
    for caractere in msg :
        if 65 <= ord(caractere) <= 90:    
            debut = alphabet.find(cle[i])
            pos = alphabet.find(caractere)
            indice = pos+debut
            if indice > 25:
                indice -= 26
            res += alphabet[indice]
            i += 1
            if i >= len(cle):
                i = 0
        
        elif 97<=ord(caractere) <=122:      
            debut = alphabet_1.find(cle[i])
            pos = alphabet_1.find(caractere)
            indice = pos+debut
            if indice > 25:
                indice -= 26
            res += alphabet_1[indice]
            i += 1
            if i >= len(cle):
                i = 0
        else:
            def quit():
                    fenetre_error.destroy()
            winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(2)  
            winsound.PlaySound(None, 0)  
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
        if 65<=ord(val)<=90 or 97<=ord(val)<=122:
            None

        else:
            def quit():
                    fenetre_error.destroy()
            winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(2)  
            winsound.PlaySound(None, 0)  
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_1 = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    i = 0
    for caractere in msg:
        if 65 <= ord(caractere) <= 90:
            debut = alphabet.find(cle[i])
            pos = alphabet.find(caractere)
            indice = pos-debut
            if indice > 25:
                indice -= 26
            res += alphabet[indice]
            i += 1
            if i >= len(cle):
                i = 0

        elif 97<=ord(caractere) <=122:
            debut = alphabet_1.find(cle[i])
            pos = alphabet_1.find(caractere)
            indice = pos-debut
            if indice > 25:
                indice -= 26
            res += alphabet_1[indice]
            i += 1
            if i >= len(cle):
                i = 0

        else:
            def quit():
                    fenetre_error.destroy()
            winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(2)  
            winsound.PlaySound(None, 0)  
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
        if 65<=ord(val)<=90 or 97<=ord(val)<=122:
            None
        else:
            def quit():
                    fenetre_error.destroy()
            winsound.PlaySound('Error_sound_windows', winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(2) 
            winsound.PlaySound(None, 0)  
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