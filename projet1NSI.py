# PROJET N°1 NSI : THEME : ALGORITHMIQUE;
# VIAL AMAURY TLEB
# LARBAOUI RIYAD TLEB

from tkinter import *
from cesar import *
from vigenere import *
from vernam import *

cryptage=Tk()

cryptage.title("MultiCrypt")                                                          # Creation du titre
cryptage.geometry("700x500")                                                          # Taille de la page
cryptage.config(bg="green")                                                           # Ajout des descriptions      
cryptage.iconbitmap("images\logo.ico")                                                # Insertion du logo      
cryptage.resizable(width=False, height=False)                                         # On empêche la modif de la fenêtre

# Création de la fonction qui est reliée aux évènements de clicks de la ListBox
def select(event):
    cesard="Date de Parution : \nIXème siècle\n\nType : \nSymétrique et par Substitution.\n On utilise un décalage créer par une clé\nde cryptage sous forme de CHIFFRES.\n\n Description du fonctionnement : \n La clé doit être connue par le crypteur et le\ndécrypteur.\n↓\n Msg :     A L ' A I D E\n Position : 1,12,1,9,4,5\n Chiffré :    C  N ' C K F G"
    vernam="Date de Parution : \n1917\n\nType : \nSymétrique et par l'opération XOR.\n On transforme notre message en binaire\npuis on l'additionne en XOR avec la clé choisie\nLe message crypté sera en binaire et il faut faire\nl'opération inverse pour déchiffrer le lessage\n\n Description du fonctionnement : \n La clé doit être connue par le crypteur et le\ndécrypteur.\n↓\n Msg:A\nMsg en binaire:01000001\n Key :01001110\n Chiffré0001111"
    vigenere="Date de Parution : \n1586\n\nType : \nSymétrique et par Substitution.\n On utilise un décalage créer par une clé\nde cryptage sous forme de LETTRES.\n\n Description du fonctionnement : \n La clé doit être connue par le crypteur et le\ndécrypteur.\n↓\n         Msg  :  A L ' A I D E\n            Key :     V  I   G  E  N  E\n Decalage :      22, 9 ,7,  5, 14, 5\n Chiffre :         W  U  H  M  R  J"                                                                                                      
    code = Lb.selection_get()

    # CODE CESARD
    if code == "CESARD":
        newWindow_1 = Toplevel(cryptage)
        newWindow_1.geometry("700x500")
        newWindow_1.iconbitmap("images\logo.ico")
        newWindow_1.resizable(width=False, height=False)
        newWindow_1.title("CESARD")
        newWindow_1.config(bg="green")
        
        #Code pour implémenter le texte de tescription avec la listbox
        cnv = Label(newWindow_1,text="",width=35, height=20, bg="white")                                             
        cnv.place(x=440,y=50)
        cnv.configure(text=cesard)
        
        # Zone de texte Message
        Titre1= Label(newWindow_1, text="MESSAGE")                                     # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                                      #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                           #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                                    #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
       
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                                      #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="RESULT")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage():                                                                                                               
            Msg=(Zone_de_texte.get())
            try:                                                                                
                Key=int((Zone_de_texte_2.get()))
                V = crypt_cesar(Msg,Key)
                Affiche_code.insert(0,V)
            except:
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
           
        
        #Implémentation du boutton décryptage
        def validation_decryptage(): 
            Msg=(Zone_de_texte.get())
            try:                                                                                                                                                                                           
                Key=int((Zone_de_texte_2.get()))
                V = decrypt_cesar(Msg,Key)
                Affiche_code.insert(0,V)
            except:
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
        
        
        #Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        #Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="CLEAR",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)
        
    # CODE VERMAN
    if code == "VERMAN":
        newWindow_1 = Toplevel(cryptage)
        newWindow_1.geometry("700x500")
        newWindow_1.iconbitmap("images\logo.ico")
        newWindow_1.resizable(width=False, height=False)
        newWindow_1.title("VERNAM")
        newWindow_1.config(bg="green")


        #Code pour implémenter le texte de tescription avec la listbox
        cnv = Label(newWindow_1,text="",width=35, height=20, bg="white")                                             
        cnv.place(x=440,y=50)
        cnv.configure(text=vernam)
        
        # Zone de texte Message
        Titre1= Label(newWindow_1, text="MESSAGE")                            # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                             #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                  #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                           #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
        
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                              #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="RESULT")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                     
            Key=(Zone_de_texte_2.get())
            V = crypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Implémentation du boutton décryptage
        def validation_decryptage():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=(Zone_de_texte_2.get())
            V = decrypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        #Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="CLEAR",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)

    # CODE VIGENERE
    if code == "VIGENERE":
        newWindow_1 = Toplevel(cryptage)
        newWindow_1.geometry("700x500")
        newWindow_1.iconbitmap("images\logo.ico")
        newWindow_1.resizable(width=False, height=False)
        newWindow_1.title("VIGENERE")
        newWindow_1.config(bg="green")
        
        #Code pour implémenter le texte de tescription avec la listbox
        cnv = Label(newWindow_1,text="",width=35, height=20, bg="white")                                             
        cnv.place(x=440,y=50)
        cnv.configure(text=vigenere)
        
        # Zone de texte Message
        Titre1= Label(newWindow_1, text="MESSAGE")                                 # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                                  #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                        #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                                 #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
        
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                                   #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="RESULT")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage():                                                                                               
            Msg=(Zone_de_texte.get())
            Key=(Zone_de_texte_2.get())
            V = chiffre_vigenere(Msg,Key)
            Affiche_code.insert(0,V) 


        #Implémentation du boutton décryptage
        def validation_decryptage():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=(Zone_de_texte_2.get())
            V = dechiffre_vigenere(Msg,Key)
            Affiche_code.insert(0,V)

        
        # Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        # Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="CLEAR",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)

#Création de la ListBox
Lb = Listbox(cryptage,font="Verdana 20 bold",width = 10, height = 20)
Lb.insert(1,"CESARD")
Lb.insert(2,"VIGENERE")
Lb.insert(3,"VERMAN")

Lb.pack(side=LEFT)
Lb.bind('<<ListboxSelect>>',select)
Lb.pack(side=TOP)

cryptage.mainloop()