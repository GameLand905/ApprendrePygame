##################################################################################
# LECON 0.1
# les bases de Python et de PyGame
#
# les buts principaux :
#   - voir les lignes de programmes qui reviennent toujours en PyGame
#           par exemple 'import pygame'
#   - voir ce qu'est l'appel a une fonction
#           par exemple 'pygame.display.set_caption("une fenetre vide")'
#   - voir ce qu'est une variable
#           un nom 'en francais' donne a un chiffre (la hauteur de la fenetre),
#                                        un groupe de chiffre (la couleur de la fenetre )
#                                        ou carrement un truc plus complexe ('Fenetre')         

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

pygame.time.delay(3000)