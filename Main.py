import Damier
from gui import Gui

interface = Gui()
interface.start()

x = input("Largeur ?")
y = input("Longeur ?")


nbgen = input("nb gen ?")


for i in range(nbgen):
    Damier.update()
    interface.updateGrid(Damier.grid)


    save = input("Sauvegarde ? (0/1)")


def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x, 0, c_x, height, width=1, fill='black')
        c_x += c


def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0, c_y, width, c_y, width=1, fill='black')
        c_y += c

def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)


def go():
    "démarrage de l'animation"
    global flag
    if flag == 0:
        flag = 1
        play()


def stop():
    "arrêt de l'animation"
    global flag
    flag = 0

def play(): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
    global flag, vitesse
    v=0
    while v!= width/c:
        w=0
        while w!= height/c:
            x=v*c
            y=w*c


            compt_viv = 0
            if dico_case[x - c, y - c] == 1:
                compt_viv += 1
            if dico_case[x - c, y] == 1:
                compt_viv += 1
            if dico_case[x - c, y + c] == 1:
                compt_viv += 1
            if dico_case[x, y - c] == 1:
                compt_viv += 1
            if dico_case[x, y + c] == 1:
                compt_viv += 1
            if dico_case[x + c, y - c] == 1:
                compt_viv += 1
            if dico_case[x + c, y] == 1:
                compt_viv += 1
            if dico_case[x + c, y + c] == 1:
                compt_viv += 1
            dico_etat[x, y] = compt_viv

        w += 1
        v += 1
    redessiner()
    if flag > 0:
        fen1.after(vitesse, play)



