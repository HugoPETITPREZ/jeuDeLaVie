
from gui import Gui
from damier import Damier

interface = Gui()
interface.start()


y = input("Longeur ?")
x = input("Largeur ?")



nbgen = input("nb gen ?")

# Je n'arrive pas à importer la class Damier
for i in range(nbgen):
    damier.update()
    interface.updateGrid(damier.grid)


# Tentative de sauvegarde
#def Save (self) :
    #Save = input("Sauvegarde ? (0/1)")
        #while Save != 0 and Save != 1
            #Save = input("Sauvegarde ? (0/1)")
        #return Save



