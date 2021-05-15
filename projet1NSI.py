from tkinter import *
from cesar import *
from vigenere import *

cryptage=Tk()

cryptage.title("MultiCrypt")                                                                                             #Creation du titre
cryptage.geometry("700x500")                                                                                             #taille de la page
cryptage.config(bg="green")
cryptage.iconbitmap("images\logo.ico")                                                                                          #Insertion du logo                                                                                    #couleur de fond
cryptage.resizable(width=False, height=False)                                                                            # On empêche la modif de la fenêtre

def select(event):
    cesard="DESCRIPTION\nCESARD"
    vernam="DESCRIPTION\nVERNAM"
    vigenere="DESCRIPTION\nVIGENERE"                                                                                                      
    code = Lb.selection_get()
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
        Titre1= Label(newWindow_1, text="MESSAGE")                                                                                  # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                                                                                   #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                                                                        #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                                                                                 #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
       
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                                                                                    #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="Result")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())   
            if Zone_de_texte_2.get() == int():                                                                                      
                Key=int(Zone_de_texte_2.get())
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
            V = crypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Implémentation du boutton décryptage
        def validation_decryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=int(Zone_de_texte_2.get())
            V = decrypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage_cesard,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage_cesard,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        #Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="Clear",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)
        
    
    if code == "VERNAM":
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
        Titre1= Label(newWindow_1, text="MESSAGE")                                                                                  # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                                                                                   #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                                                                        #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                                                                                 #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
        
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                                                                                    #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="Result")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=int(Zone_de_texte_2.get())
            V = crypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Implémentation du boutton décryptage
        def validation_decryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=int(Zone_de_texte_2.get())
            V = decrypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage_cesard,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage_cesard,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        #Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="Clear",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)
    
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
        Titre1= Label(newWindow_1, text="MESSAGE")                                                                                  # Titre Message
        Titre1.place(x=320,y=175)
        Zone_de_texte=Entry(newWindow_1,width=30)                                                                                   #Zone d'entré du message
        Zone_de_texte.place(x=250,y=200)
        
        #Zone de texte Cryptage
        Titre2=Label(newWindow_1,text="KEY")                                                                                        #Titre Clé
        Titre2.place(x=330,y=120)
        Zone_de_texte_2=Entry(newWindow_1,width=30)                                                                                 #Zone d'entrée de la clé
        Zone_de_texte_2.place(x=250,y=150)
        
        #Zone de texte Resultat 
        Affiche_code=Entry(newWindow_1,width=30)                                                                                    #Zone de résultat,Information crypter ou décrypter
        Affiche_code.place(x=500,y=410)
        code=Label(newWindow_1,text="Result")
        code.place(x=570,y=380)
        
        #Implémentation du boutton cryptage
        def validation_cryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=int(Zone_de_texte_2.get())
            V = crypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        #Implémentation du boutton décryptage
        def validation_decryptage_cesard():                                                                                                               
            Msg=(Zone_de_texte.get())                                                                                         
            Key=int(Zone_de_texte_2.get())
            V = decrypt_cesar(Msg,Key)
            Affiche_code.insert(0,V)
        
        # Checkboxs crypter, décrypter 
        checkbox_crypter = Checkbutton(newWindow_1, text="CRYPTER",command=validation_cryptage_cesard,bg="orange")
        checkbox_crypter.place(x=310,y=300) 
        checkbox_decrypter = Checkbutton(newWindow_1,text="DECRYPTER",command=validation_decryptage_cesard,bg="orange")
        checkbox_decrypter.place(x=305,y=330)
        
        #Implémentation du boutton clear
        def Clear():
            Mg=(Zone_de_texte.delete(0,END))
            Z=(Zone_de_texte_2.delete(0,END))
            F=(Affiche_code.delete(0,END))
            G=(checkbox_crypter.deselect())
            H=(checkbox_decrypter.deselect())
        
        # Création du boutton Clear
        Bouton_Supprimer=Button(newWindow_1,text="Clear",command=Clear)
        Bouton_Supprimer.place(x=323,y=450)

#Création de la ListBox
Lb = Listbox(cryptage,font="Verdana 20 bold",width = 10, height = 20)
Lb.insert(1,"CESARD")
Lb.insert(2,"VERNAM")
Lb.insert(3,"VIGENERE")

Lb.pack(side=LEFT)
Lb.bind('<<ListboxSelect>>',select)
Lb.pack(side=TOP)

cryptage.mainloop()