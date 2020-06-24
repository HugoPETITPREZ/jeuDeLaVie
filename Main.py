from gui import Gui

interface = Gui()
interface.start()

x = input("Largeur ?")
y = input("Longeur ?")

damier = Damier(x,y)

nbgen = input("nb gen ?")
if ...

for i in range(nbgen):
    damier.update()
    interface.updateGrid(damier.grid)

save = input("Sauvegarde ? (0/1)")
if ....

