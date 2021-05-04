from tkinter import *


cryptage=Tk()


def validation():                                                                                                        #Fonction validation
    I=Zone_de_texte.get()                                                                                                #Insérer une information, #I variable pour information
    Affiche_code.insert(0,I)                                                                                             #Reliage des informations


cryptage.title("MultiCrypt")                                                                                             #Creation du titre
cryptage.geometry("700x500")                                                                                             #taille de la page
cryptage.iconbitmap("logo.ico")                                                                                          #Insertion du logo
cryptage.config(background="orange")                                                                                     #couleur de fond





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


cryptage.mainloop()