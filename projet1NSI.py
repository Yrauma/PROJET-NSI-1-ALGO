from tkinter import *
from cesar import *

cryptage=Tk()


cryptage.title("MultiCrypt")                                                                                             #Creation du titre
cryptage.geometry("700x500")                                                                                             #taille de la page
cryptage.config(bg="green")
cryptage.iconbitmap("logo.ico")                                                                                          #Insertion du logo                                                                                    #couleur de fond
cryptage.resizable(width=False, height=False)                                                                            # On empêche la modif de la fenêtre



Titre1= Label(cryptage, text="MESSAGE")                                                                                  # Titre Message
Titre1.place(x=320,y=175)
Zone_de_texte=Entry(cryptage,width=30)                                                                                   #Zone d'entré du message
Zone_de_texte.place(x=250,y=200)

Titre2=Label(cryptage,text="KEY")                                                                                        #Titre Clé
Titre2.place(x=330,y=120)
Zone_de_texte_2=Entry(cryptage,width=30)                                                                                 #Zone d'entrée de la clé
Zone_de_texte_2.place(x=250,y=150)


Affiche_code=Entry(cryptage,width=30)                                                                                    #Zone de résultat,Information crypter ou décrypter
Affiche_code.place(x=500,y=410)
code=Label(cryptage,text="Result")
code.place(x=570,y=380)

cesard="DESCRIPTION\nCESARD"
vernam="DESCRIPTION\nVERNAM"
vigenere="DESCRIPTION\nVIGENERE"

def select(event):                                                                                                      
    sel = Lb.selection_get()
    L.configure(text = sel)

#Code pour implémenter le texte de tescription avec la listbox
def description(event):
    code=Lb.selection_get()
    if code == "CESARD":
        cnv.configure(text=cesard)
    if code == "VERNAM":
        cnv.configure(text=vernam)
    if code == "VIGENERE":
        cnv.configure(text=vigenere)

Lb = Listbox(cryptage,font="Verdana 20 bold",width = 10, height = 20)
Lb.insert(1,"CESARD")
Lb.insert(2,"VERNAM")
Lb.insert(3,"VIGENERE")

Lb.pack(side=LEFT)
Lb.bind('<<ListboxSelect>>',select)
Lb.bind('<Return>',description)
Lb.pack()

L = Label(cryptage,text="",width=10,height=2,bg="white")
L.place(x=540,y=10)

# Création de la zone de description des types de cryptage
cnv = Label(cryptage,text="",width=35, height=20, bg="white")                                             
cnv.place(x=440,y=50)

# Création des CheckBouttons crypter et décrypter

def validation_cryptage_cesard():                                                                                                               
    Msg=(Zone_de_texte.get())                                                                                         
    Key=int(Zone_de_texte_2.get())
    V = crypt(Msg,Key)
    Affiche_code.insert(0,V)

def validation_decryptage_cesard():                                                                                                               
    Msg=(Zone_de_texte.get())                                                                                         
    Key=int(Zone_de_texte_2.get())
    V = decrypt(Msg,Key)
    Affiche_code.insert(0,V)


checkbox_crypter = Checkbutton(cryptage, text="CRYPTER",command=validation_cryptage_cesard,bg="orange")
checkbox_crypter.place(x=310,y=300)

checkbox_decrypter = Checkbutton(cryptage,text="DECRYPTER",command=validation_decryptage_cesard,bg="orange")
checkbox_decrypter.place(x=305,y=330)

# Création du boutton Clear

def Clear():
    Mg=(Zone_de_texte.delete(0,END))
    Z=(Zone_de_texte_2.delete(0,END))
    F=(Affiche_code.delete(0,END))
    G=(checkbox_crypter.deselect())
    H=(checkbox_decrypter.deselect())

Bouton_Supprimer=Button(cryptage,text="Clear",command=Clear)
Bouton_Supprimer.place(x=323,y=450)

cryptage.mainloop()