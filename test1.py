from tkinter import *


cryptage=Tk()


cryptage.title("MultiCrypt")                                                                                             #Creation du titre
cryptage.geometry("700x500")                                                                                             #taille de la page
cryptage.iconbitmap("logo.ico")                                                                                          #Insertion du logo
cryptage.config(background="orange")                                                                                     #couleur de fond

Zone_de_texte=Entry(cryptage,width=30)                                                                                   #Zone de texte
Zone_de_texte.place(x=250,y=200)
Zone_de_texte_2=Entry(cryptage,width=30)
Zone_de_texte_2.place(x=250,y=150)


Titre1= Label(cryptage, text="key")
Titre1.place(x=330,y=120)
Titre2=Label(cryptage,text='Message')
Titre2.place(x=320,y=175)

Bouton_Validation=Button(cryptage,text="Valider")
Bouton_Validation.place(x=320,y=400)

cryptage.mainloop()