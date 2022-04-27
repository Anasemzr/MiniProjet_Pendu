from tkinter import Tk,Button,Label,Entry,Toplevel
from random import choice

window= Tk()
window.geometry("700x400")
window.config(background="#F4F499")
mot=[]
def creer_mot():
    global mot,mot_final,mot_dico,compteur
    mot_final=[]
    mot.clear()
    mot_dico=choice(dico_mot)
    compteur=10
    vie["text"] = compteur

    for i in range(len(mot_dico)):
        mot.append(mot_dico[i])
        mot_final.append("*")

    lbl["text"]=mot_final

def recherche_mot(event):
    global mot,mot_final,mot_dico,compteur
    lettre=answer.get()
    lettre=lettre.upper()
    answer.delete(-1)
    if lettre in mot:
        i=mot.count(lettre)
        if i>1:
            for o in range(i):
                nb=mot.index(lettre)
                mot[nb]="*"
                mot_final[nb]=lettre
        else:
            nb = mot.index(lettre)
            mot[nb] = "*"
            mot_final[nb] = lettre

        lbl["text"]=mot_final
    else:
        compteur-=1
        vie["text"]=compteur
        if compteur==0:
            game_finish(False)

    if "".join(mot_final) == mot_dico:
        game_finish(True)

def game_finish(bool):
    fenetre=Toplevel(window)
    fenetre.geometry("200x200")

    if bool:
        label=Label(fenetre,text="YOU WIN",bg="green",fg="white")
        fenetre.config(background="green")
    else:
        label=Label(fenetre,text="GAME OVER",bg="black",fg="red")
        fenetre.config(background="black")

    label.pack(expand=True)




lbl=Label(window,text="PENDU",font=(("Arial"),30),bg="#F4F499")
lbl.pack(expand=True)

vie=Label(window,text="5",font=(("Arial"),60),fg="red",bg="#F4F499")
vie.place(x=550,y=150)

answer=Entry(window)
answer.pack(expand=True)

btn=Button(window,text="VALIDER",command=lambda:recherche_mot("<Return>"))
btn.place(x=330,y=350)

w=window.winfo_reqwidth()

btn=Button(window,text="START",width=int(w/2),command=creer_mot)
btn.place(x=0,y=10)

dico_mot=("PATATE","DINOSAURE","MONSTRE","MACHINE","ROBOT","MEXIQUE","SOLEIL","SOLEIL","ORDINATEUR")


window.bind("<Return>",recherche_mot)
window.mainloop()