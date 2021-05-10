from tkinter import *


cryptage=Tk()


def validation():                                                                                                        #Fonction validation
    I=Zone_de_texte.get()                                                                                                #Insérer une information, #I variable pour information
    Affiche_code.insert(0,I)                                                                                             #Reliage des informations


cryptage.title("MultiCrypt")                                                                                             #Creation du titre
cryptage.geometry("700x500")                                                                                             #taille de la page
cryptage.iconbitmap("logo.ico")                                                                                          #Insertion du logo
cryptage.config(background="orange")                                                                                     #couleur de fond
cryptage.resizable(width=False, height=False)                                                                            # On empêche la modif de la fenêtre





Titre1= Label(cryptage, text="key")                                                                                      # Titre clé
Titre1.place(x=330,y=120)
Zone_de_texte=Entry(cryptage,width=30)                                                                                   #Zone d'entré de la clé
Zone_de_texte.place(x=250,y=200)

Titre2=Label(cryptage,text='Message')                                                                                    #Titre message
Titre2.place(x=320,y=175)
Zone_de_texte_2=Entry(cryptage,width=30)                                                                                 #Zone d'entrée du message
Zone_de_texte_2.place(x=250,y=150)




Bouton_Validation=Button(cryptage,text="Valider",command=validation)                                                     #Bouton validation
Bouton_Validation.place(x=320,y=400)





Affiche_code=Entry(cryptage,width=30)                                                                                    #Zone de résultat,Information crypter ou décrypter
Affiche_code.place(x=500,y=410)
code=Label(cryptage,text="Result")
code.place(x=570,y=360)

def select(event):                                                                                                      # Ajoute de la ListBox
    sel = Lb.selection_get()
    L.configure(text = sel)

Lb = Listbox(cryptage,font="Verdana 20 bold",width = 10, height = 20)
Lb.insert(1,"CESARD")
Lb.insert(2,"VERNAM")
Lb.insert(3,"VIGENERE")



Lb.pack(side=LEFT)

Lb.bind('<<ListboxSelect>>', select)

Lb.pack()

L = Label(cryptage,text="")
L.place(x=550,y=20)







cryptage.mainloop()