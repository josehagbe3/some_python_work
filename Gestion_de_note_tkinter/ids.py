import mysql.connector
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
#Matiere

maBase = mysql.connector.connect(host="localhost", user="root", password="", database="note_eleve")
meConnect = maBase.cursor()
meConnect.execute(" select * from matieres;")
ids = []
libelles = []
for row in meConnect:
    ids.append(row[0])
    libelles.append(row[1])

print(ids)
print(libelles)
maBase.close()




