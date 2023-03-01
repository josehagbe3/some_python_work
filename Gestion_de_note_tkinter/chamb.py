
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def Ajouter():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere = ids[combomatiere.current()]
    note = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="",database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO note (code, nom, prenom, sexe, classe, matiere, notes) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val = (matricule, nom, prenom, sexe, classe, matiere, note)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note ajoutée")
        root.destroy()
        call(["python", "chambre2.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def Modifier():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere = ids[combomatiere.current()]
    note = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "update note set  nom=%s, prenom=%s, sexe=%s, classe=%s, matiere=%s, notes=%s where code=%s"
        val = (nom, prenom, sexe, classe, matiere, note, matricule)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note modifiée")
        root.destroy()
        call(["python", "chambre2.py"])

    except Exception as e:
        print(e)
        # retour
        maBase.rollback()
        maBase.close()

def Supprimer():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "delete from note where code= %s"
        val = ( matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note Supprimée")
        root.destroy()
        call(["python", "chambre2.py"])

    except Exception as e:
        print(e)
        # retour
        maBase.rollback()
        maBase.close()
#ma fenetre

root = Tk()


root.title("SCHOOL DATA")
root.geometry("1350x700+0+0")
#root.resizable(False, False)
root.configure(background= "#091821")

# Ajouter le titre

lbltitre = Label(root, borderwidth = 3, relief = SUNKEN, text ="GESTION DES NOTES DES ELEVES",
                         font = ("Sans Serif", 25), activebackground= "#2F4F4F",
                fg= "#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height = 100)

#Detail des eleves

#Matricule
lblNumero = Label(root, text="MATRICULE", font=("Arial", 18),bg="#091821",
                  fg= "white")
lblNumero.place(x=70, y= 150, width=150)
txtNumero = Entry(root, bd =4, font= ("Arial", 14))
txtNumero.place(x=250, y=150, width= 150)

#Nom
lblnom = Label(root, text="NOM", font=("Arial", 18),bg="#091821",
                  fg= "white")
lblnom.place(x=70, y= 200, width=150)
txtnom = Entry(root, bd =4, font= ("Arial", 14))
txtnom.place(x=250, y=200, width= 300)

#Prenom
lblprenom = Label(root, text="PRENOM", font=("Arial", 18),bg="#091821",
                  fg= "white")
lblprenom.place(x=70, y= 250, width=150)
txtprenom = Entry(root, bd =4, font= ("Arial", 14))
txtprenom.place(x=250, y=250, width= 300)

#sexe

valeurSexe = StringVar()

lblSexeMasculin = Radiobutton(root, text="MASCULIN", value="M", variable=valeurSexe, indicatoron=0,font=("Arial", 14),bg="#091821", fg= "#696969")
lblSexeMasculin.place(x=250, y= 300, width=130)
lblSexeFeminin = Radiobutton(root, text="FEMININ", value="F", variable=valeurSexe, indicatoron=0,font=("Arial", 14),bg="#091821", fg= "#696969")
lblSexeFeminin.place(x=450, y= 300, width=130)
# Classe
lblClasse = Label(root, text="CLASSE", font=("Arial", 14),bg="#091821", fg= "white")
lblClasse.place(x=70, y= 350, width=150)

comboClasse = ttk.Combobox(root, font=("Arial", 14))
comboClasse["values"] = ["6e", "5e", "4e", "3e", "2nde", "1ère", "Tle"]
comboClasse.place(x=250, y=350, width=130)

#Matiere

maBase = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")
meConnect = maBase.cursor()
meConnect.execute(" select * from matieres;")
ids = []
libelles = []
ids = []
libelles = []
for row in meConnect:
    ids.append(row[0])
    libelles.append(row[1])

lblmatiere = Label(root, text="MATIERE", font=("Arial", 14),bg="#091821", fg= "white")
lblmatiere.place(x=70, y= 400, width=150)
combomatiere = ttk.Combobox(root, font=("Arial", 14))
combomatiere["values"] = libelles
combomatiere.place(x=250, y=400, width= 300)

#note
lblnote = Label(root, text="NOTE", font=("Arial", 18),bg="#091821", fg= "white")
lblnote.place(x=70, y= 450, width=150)
txtnote= Entry(root, bd =4, font= ("Arial", 14))
txtnote.place(x=250, y=450, width= 300)

#enregistrer
btnenregistrer = Button(root, text= "Enregistrer", font=("Arial,16"), bg= "#02691E", fg="white", command=Ajouter)
btnenregistrer.place(x=250, y=500,width=200)

#modifier
btnmodifier = Button(root, text= "Modifier", font=("Arial,16"), bg= "#D2691E", fg="white", command=Modifier)
btnmodifier.place(x=250, y=550,width=200)

#supprimer
btnSupprimer = Button(root, text= "Supprimer", font=("Arial,16"), bg= "#D2691E", fg="white", command=Supprimer)
btnSupprimer.place(x=250, y=600,width=200)

#Table
table = ttk.Treeview(root, columns= (1, 2, 3, 4, 5, 6, 7, 8), height= 5, show= "headings")
table.place(x =560, y=150, width= 700, height= 450)#dimensions d'affichage de la table width=largeur et height=hauteur
#Entete
table.heading(1, text= "MAT")
table.heading(2, text= "NOM")
table.heading(3, text= "PRENOM")
table.heading(4, text= "SEXE")
table.heading(5, text= "CLASSE")
table.heading(6, text= "MATIERE")
table.heading(7, text= "NOTE")
table.heading(8, text= "DATE ENREGISTREMENT")

#definir les dimensions des colonnes
table.column(1,width = 80)
table.column(2,width = 80)
table.column(3,width = 80)
table.column(4,width = 80)
table.column(5,width = 80)
table.column(6,width = 80)
table.column(7,width = 80)
table.column(8,width = 160)

#afficher les informations de la table

maBase = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")# conexion à la base de donnee note_eleve
meConnect = maBase.cursor()                                                                  # manipulation de note_eleve
meConnect.execute("select n.code, n.nom, n.prenom, n.sexe, n.classe, m.libelle, n.notes, n.date_enregistrement from note n join matieres m on n.matiere = m.id")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()


#Exécution

root.mainloop()
