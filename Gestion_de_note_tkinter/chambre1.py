from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

#fonction connecter
def seconnecter():
    surnom = txtnomutilisateur.get()
    mdp = txtmdp.get()
    if (surnom == "" and mdp == ""):
        messagebox.showerror("", "Il faut entrer les données")
        txtmdp.delete("0", "end")
        txtnomutilisateur.delete("0", "end")
    elif (surnom == "admin" and mdp == "admin"):
        messagebox.showinfo("", "Bienvenue")
        txtnomutilisateur.delete("0", "end")
        txtmdp.delete("0", "end")
        root.destroy()
        call(["python", "chambre2.py "])
    else:
        messagebox.showwarning("", "Erreur de connexion")
        txtmdp.delete("0", "end")
        txtnomutilisateur.delete("0", "end")


#ma fenetre

root = Tk()

root.title(" Fenetre de connexion")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure( background= "#091821")

# Ajouter des titres

lbltitre = Label(root, borderwidth= 6, relief= SUNKEN,text = "Formulaire de connexion ", font= ("Sans Serif", 25),background= "#091821", fg= "white")
lbltitre.place(x=0, y=0, width= 400)

lblnomutilisateur = Label(root, text= "Nom d'utilisateur:", font=("Arial", 9), bg= "#091821", fg= "white")
lblnomutilisateur.place(x = 5, y = 100, width= 150)
txtnomutilisateur = Entry(root, bd= 4, font=("Arial", 13))
txtnomutilisateur.place(x=150, y=100, width=200, height=30)

lblmp = Label(root,text="Mot de passe:", font=("Arial",12), bg="#091821", fg="white")
lblmp.place(x = 5, y = 150, width= 150)
txtmdp = Entry(root, show="*", bd=4, font=("Arial", 13))
txtmdp.place(x = 150, y = 150, width=200, height=30)

#Bouton se connecter
btnenregistrer = Button(root, text="connexion", font=("Arial", 16),
                        bg="#FF4500", fg="white", command=seconnecter())
btnenregistrer.place(x = 150, y = 200, width=200)





#Exécution
root.mainloop()