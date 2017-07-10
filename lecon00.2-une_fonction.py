##################################################################################
# LECON 0.2
# les bases de Python et de PyGame
#
# les buts principaux :
#   - creer une fonction
#   - faire varier une variable (si,si)
#           en comptant le temps qui s'ecoule depuis le lancement du programme
#   - prendre conscience des choses sont simples
#           en 3 lignes, en affiche du texte a l'ecran
#   - prendre conscience des choses sont complexes
#           bah, il faut un truc appele 'font' pour afficher les textes
#           il y a une notion informatique de 'type' assez fondamentale 
#               la fonction Python 'str' transforme un chiffre en texte...  
#   - decouvrir l'Horloge
#           cela servira plus tard, pour le nombre d'image par secondes (FPS)
#   - decourvrir la boucle While (tant que)
#   - decouvrir la gestion de l'ecran
#           on efface tout pour afficher quelquecose de nouveau, sinon...
#   - ecrire son premier bug
#           le programme ne finit jamais... il pourrait bloquer l'ordinateur         

# on dit a Python qu'on utilise Pygame
import pygame

# rien a comprendre, pygame a besoin de cette ligne 
pygame.init()

# les informations sur la fenetre de jeu
#   la couleur du fond de la couleur, du noir car 0 de rouge, 0 de rouge, 0 de bleu
#   le bleu 'pur' serait (0,0,255) car le bleu est le 3eme chiffre et 255 est la valeur maximum
#   le blanc serait (255,255,255)
#   etc...
Couleur_du_fond_RVB = (0,0,0)

#   et la taille de la fenetre en pixels
Hauteur_de_la_fenetre = 300
Largeur_de_la_fenetre = 400
#   (x,y) c'est la facon dont Python stocke les coordonnees
Taille_de_la_fenetre = (Largeur_de_la_fenetre,Hauteur_de_la_fenetre)

# c'est la facon dont PyGame creer une fenetre pour l'afficher sur l'ecran
Fenetre = pygame.display.set_mode(Taille_de_la_fenetre)

# 'caption', ca veut dire 'etiquette' en gros.
# 'set_caption', ca veut 'mettre dans l'etiquette
pygame.display.set_caption("une fenetre vide")

# 'fill' veut dire 'remplir'
#     on remplit donc la fenetre de la couleur Couleur_du_fond_RVB
Fenetre.fill(Couleur_du_fond_RVB)

# cette ligne attend 3000 millisecondes avant de passer a la suivante
#   3000 millisecondes, cela fait 3 secondes
#   et vu qu'il n'y a pas de ligne suivante, le programme se termine : la fenetre se ferme

##############################################################################
##############################################################################
##############################################################################
Horloge = pygame.time.Clock()
Couleur_du_texte_RVB  = (255, 255, 255)

Nombre_de_millisecondes_ecoulee = 0

font = pygame.font.Font(None, 40)
#
##############################################################################
#

def Affiche_les_millisecondes(millisecondes) :
    Les_millisecondes_en_texte = str(millisecondes)
    Texte_a_afficher = font.render(Les_millisecondes_en_texte, 1, Couleur_du_texte_RVB)
    Fenetre.blit(  Texte_a_afficher, (50,50))
#
#############################################################################
#

while True:
    # 'fill' veut dire 'remplir'
    #     on remplit donc la fenetre de la couleur Couleur_du_fond_RVB
    Fenetre.fill(Couleur_du_fond_RVB)
    
    # on attend un peu pour avoir le bon nombre de FPS
    # 'tick' attend AU MOINS un certain nombre de millisecondes
    # et retourne le nombre de millisecondes reellement ecoule 
     
    Nombre_de_millisecondes_entre_deux_ticks= Horloge.tick(1000)
    Nombre_de_millisecondes_ecoulee =  Nombre_de_millisecondes_ecoulee +Nombre_de_millisecondes_entre_deux_ticks
    Affiche_les_millisecondes(Nombre_de_millisecondes_ecoulee)
    
    # rien a comprendre 
    # ca met a jour les choses a afficher a l'ecran
    pygame.display.flip()

game.time.delay(3000)