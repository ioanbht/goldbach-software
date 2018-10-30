from tkinter import *
from tkinter import messagebox

#Méthode permettant de faire le test
def Tester():
    
    
    if nombre.get().replace(" ","") == "":
        messagebox.showerror("Champ vide", "Veuillez saisir un nombre")
    else:
        try:
            assert int(nombre.get())%2 == 0         
        except ValueError:
            messagebox.showerror("Saisie invalide", "Veuillez saisir un nombre")
        except AssertionError:
            messagebox.showerror("Nombre invalide", "Veuillez saisir un nombre pair")
        else:
            if int(nombre.get()) < 3:
                messagebox.showerror("Nombre invalide", "Veuillez saisir un nombre supérieur à 3")
            else:


                nb_premier = 2
                nbs_premiers = []
                while nb_premier < int(nombre.get()):
                    diviseur = 2
                    while 1:
                        if nb_premier % diviseur == 0 and nb_premier != diviseur:
                            break
                        elif nb_premier < diviseur:
                            nbs_premiers.append(nb_premier)
                            break
                        elif nb_premier % diviseur != 0 or nb_premier == diviseur:
                            diviseur += 1
                    nb_premier += 1

                combinaisons = ""    
                for nb_premier_i in nbs_premiers:
                    if nb_premier_i > int(nombre.get())/2:
                        break
                    elif int(nombre.get())-nb_premier_i in nbs_premiers:
                        combinaisons += f" {nb_premier_i} + {int(nombre.get())-nb_premier_i} ="
                
                combinaisons = combinaisons.split(" ")
                del combinaisons[-1], combinaisons[0]
                combinaisons = " ".join(combinaisons)

                messagebox.showinfo("Solution(s) de la conjecture", f"{nombre.get()} = {combinaisons}")
                        
                    

#Quand on tape sur la touche Entrer
def Tester_bind(j):
    Tester()

        
#Interface
fenetre = Tk()
fenetre.title("Goldbach Software")
fenetre.geometry("300x50")

nombre = StringVar()
Entry(fenetre, textvariable=nombre).pack()

Button(fenetre, text="Tester", command=Tester).pack()

fenetre.bind("<Return>", Tester_bind)

fenetre.mainloop()
